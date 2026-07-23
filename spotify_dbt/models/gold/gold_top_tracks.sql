{{ config(
    materialized='table',
    schema='gold'
) }}

select
    track_name,
    artist_name,
    genre,
    count(*) as total_plays,
    round(avg(listen_percentage), 2) as avg_listen_percentage,
    sum(case when is_skipped then 1 else 0 end) as total_skips,
    round(sum(case when is_skipped then 1 else 0 end) * 100.0 / count(*), 2) as skip_rate
from {{ ref('stg_spotify_events') }}
group by track_name, artist_name, genre
order by total_plays desc