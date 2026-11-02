SELECT
    DATE_TRUNC(DATE(created_at), MONTH) AS borrow_month,
    site_id,
    SUM(cup_count) AS cups_borrowed
FROM {{ref('stg_user_history')}}
WHERE action = "Borrowed"
GROUP BY borrow_month, site_id
