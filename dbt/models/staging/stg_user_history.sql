SELECT
    JSON_VALUE(raw_payload, '$.Action') AS action,
    SAFE_CAST(JSON_VALUE(raw_payload, '$.Site[0]') AS INT64) AS site_id,
    SAFE_CAST(JSON_VALUE(raw_payload, '$.Count') AS INT64) AS cup_count
FROM `everloop-analytics.raw.user_history`
WHERE extracted_at = CURRENT_DATE()
  AND JSON_VALUE(raw_payload, '$.Action') IN ('Borrowed', 'Returned')