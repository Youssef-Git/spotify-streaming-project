{{ config(
    materialized='table',
    schema='gold'
) }}

select
    artist_name,
    genre,
    count(*) as total_plays,
    count(distinct track_name) as unique_tracks_played,
    round(avg(listen_percentage), 2) as avg_listen_percentage,
    round(sum(case when is_skipped then 1 else 0 end) * 100.0 / count(*), 2) as skip_rate
from {{ ref('stg_spotify_events') }}
group by artist_name, genre
order by total_plays desc