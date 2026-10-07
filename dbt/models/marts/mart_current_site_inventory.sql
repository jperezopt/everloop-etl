WITH restocks AS (
    SELECT
        site_id,
        SUM(total_cups) AS cups_restocked
    FROM {{ ref('stg_cup_stock_updates') }}
    WHERE LOWER(action) IN ('initial stock', 'feed in', 'for staff extras')
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
    restocks.cups_restocked,
    COALESCE(transactions.cups_borrowed, 0) AS cups_borrowed,
    COALESCE(transactions.cups_returned, 0) AS cups_returned,
    restocks.cups_restocked
        - COALESCE(transactions.cups_borrowed, 0)
        + COALESCE(transactions.cups_returned, 0) AS current_stock
FROM restocks
LEFT JOIN transactions
    ON restocks.site_id = transactions.site_id
ORDER BY restocks.site_id