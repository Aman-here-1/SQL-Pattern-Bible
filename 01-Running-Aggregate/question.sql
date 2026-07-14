SELECT
    event_date,
    COUNT(DISTINCT user_id) AS dau
FROM app_open_events
WHERE event_date >= current_date - INTERVAL '30 days'
GROUP BY event_date
ORDER BY event_date;