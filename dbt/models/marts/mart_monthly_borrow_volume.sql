SELECT
    DATE_TRUNC(DATE(uh.created_at), MONTH) AS borrow_month,
    SUM(uh.cup_count) AS cups_borrowed,
    uh.site_id,
    s.site_name
FROM {{ref('stg_user_history')}} AS uh
LEFT JOIN {{ref('stg_sites')}} AS s
    ON uh.site_id = s.site_id
WHERE action = "Borrowed"
GROUP BY borrow_month, uh.site_id, s.site_name