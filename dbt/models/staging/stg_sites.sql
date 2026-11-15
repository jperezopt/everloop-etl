SELECT
    JSON_VALUE(raw_payload, '$.Name') as site_name,
    SAFE_CAST(JSON_VALUE(raw_payload, '$.id') as INT64) as site_id
FROM `everloop-analytics.raw.sites`