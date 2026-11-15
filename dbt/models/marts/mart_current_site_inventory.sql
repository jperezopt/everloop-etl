WITH restocks AS (
    SELECT
        site_id,
        SUM(CASE WHEN LOWER(TRIM(action)) IN ('initial', 'extras', 'staff')
                 THEN total_cups ELSE 0 END) AS cups_restocked,
        SUM(CASE WHEN LOWER(TRIM(action)) = 'excess'
                 THEN -total_cups ELSE 0 END) AS cups_removed
    FROM {{ ref('stg_cup_stock_updates') }}
    WHERE LOWER(TRIM(action)) IN ('initial', 'extras', 'staff', 'excess')
    GROUP BY site_id
),

transactions AS (
    SELECT
        site_id,
        SUM(CASE WHEN action = 'Borrowed' THEN cup_count ELSE 0 END) AS cups_borrowed,
        SUM(CASE WHEN action = 'Returned' THEN cup_count ELSE 0 END) AS cups_returned
    FROM {{ ref('stg_user_history') }}
    GROUP BY site_id
)

SELECT
    restocks.site_id,
    sites.site_name,
    restocks.cups_restocked,
    COALESCE(transactions.cups_borrowed, 0) AS cups_borrowed,
    COALESCE(transactions.cups_returned, 0) AS cups_returned,
    restocks.cups_restocked
        - restocks.cups_removed
        - COALESCE(transactions.cups_borrowed, 0)
        + COALESCE(transactions.cups_returned, 0) AS current_stock
FROM restocks
LEFT JOIN transactions
    ON restocks.site_id = transactions.site_id
LEFT JOIN {{ ref('stg_sites') }} AS sites
    ON restocks.site_id = sites.site_id
ORDER BY restocks.site_id