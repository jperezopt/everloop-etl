SELECT
    JSON_VALUE(raw_payload, '$.Action') AS action,
    SAFE_CAST(JSON_VALUE(raw_payload, '$.Site[0]') AS INT64) AS site_id,
    SAFE_CAST(JSON_VALUE(raw_payload, '$.Count') AS INT64) AS cup_count,
    SAFE_CAST(JSON_VALUE(raw_payload, '$.created_at') AS TIMESTAMP) AS created_at
FROM `everloop-analytics.raw.user_history`
-- temp latest snapshot
WHERE extracted_at = DATE '2026-11-03'
  AND JSON_VALUE(raw_payload, '$.Action') IN ('Borrowed', 'Returned')