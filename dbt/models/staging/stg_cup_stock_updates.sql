SELECT
    JSON_VALUE(raw_payload, '$.Action') AS action,
    SAFE_CAST(JSON_VALUE(raw_payload, '$.Site[0]') AS INT64) AS site_id,
    SAFE_CAST(JSON_VALUE(raw_payload, '$."Total Cups"') AS INT64) AS total_cups
FROM `everloop-analytics.raw.cup_stock_updates`