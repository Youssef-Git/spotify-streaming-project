{{ config(
    materialized='table',
    schema='gold'
) }}

select
    country,
    platform,
    genre,
    event_date,
    event_hour,
    count(*) as total_plays,
    count(distinct user_id) as unique_listeners,
    round(avg(listen_percentage), 2) as avg_listen_percentage,
    round(sum(case when is_skipped then 1 else 0 end) * 100.0 / count(*), 2) as skip_rate
from {{ ref('stg_spotify_events') }}
group by country, platform, genre, event_date, event_hour
order by event_date, event_hour