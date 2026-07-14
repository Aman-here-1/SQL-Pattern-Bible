-- Last 30 days ka DAU trend nikalo.
SELECT
    event_date,
    COUNT(DISTINCT user_id) AS dau
FROM app_open_events
WHERE event_date >= current_date - INTERVAL '30 days'
GROUP BY event_date
ORDER BY event_date;

-- Last 30 days ka WAU trend nikalo.

select date_trunc('week', event_date) as weeks, count(distinct user_id) as wou from app_open_events
where event_date >= current_date - INTERVAL '30 days'
group by 1
order by 1 asc;


-- Last 6 months ka MAU trend nikalo.
select 
date_trunc('month', event_date) as months,
-- date_format(date_parse(event_date, '%Y-%m-%d'), '%Y-%m') as month_year,
-- date_format(event_date, '%Y-%m-%d') as event_dates,
count(distinct user_id) as mau from app_open_events
where event_date >= current_date - INTERVAL '6 months'
group by 1
order by 1 asc;


-- "Hamare users kitne sticky hain?"
-- Stickiness = DAU / MAU
WITH daily_active_users AS (
    SELECT
        DATE_TRUNC('month', event_date) AS month_start,
        AVG(dau) AS avg_dau
    FROM
    (
        SELECT
            event_date,
            COUNT(DISTINCT user_id) AS dau
        FROM app_open_events
        GROUP BY event_date
    ) d
    GROUP BY 1
),
monthly_active_users AS (
    SELECT
        DATE_TRUNC('month', event_date) AS month_start,
        COUNT(DISTINCT user_id) AS mau
    FROM app_open_events
    GROUP BY 1
)
SELECT 
    d.month_start,
    ROUND(d.avg_dau,2) AS avg_dau,
    m.mau,
    ROUND(
        (d.avg_dau * 100.0) / m.mau,
        2
    ) AS stickiness_percent
FROM daily_active_users d
JOIN monthly_active_users m
ON d.month_start = m.month_start
ORDER BY d.month_start;

-- Top 5 Cities by Stickiness

WITH daily_active_users AS (

    SELECT

        city,

        DATE_TRUNC('month', event_date) AS month_start,

        AVG(dau) AS avg_dau

    FROM (

        SELECT

            event_date,

            city,

            COUNT(DISTINCT user_id) AS dau

        FROM app_open_events

        GROUP BY
            event_date,
            city

    ) d

    GROUP BY
        city,
        month_start

),

monthly_active_users AS (

    SELECT

        city,

        DATE_TRUNC('month', event_date) AS month_start,

        COUNT(DISTINCT user_id) AS mau

    FROM app_open_events

    GROUP BY
        city,
        month_start

)

SELECT

    d.city,

    d.month_start,

    ROUND(d.avg_dau,2) AS avg_dau,

    m.mau,

    ROUND(
        d.avg_dau * 100.0 / m.mau,
        2
    ) AS stickiness_percent

FROM daily_active_users d

JOIN monthly_active_users m

ON d.city = m.city
AND d.month_start = m.month_start

ORDER BY
    stickiness_percent DESC

LIMIT 5;