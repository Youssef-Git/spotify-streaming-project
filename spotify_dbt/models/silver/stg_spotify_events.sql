{{ config(
    materialized='table',
    schema='silver'
) }}

with source as (
    select * from workspace.bronze.spotify_events
),

cleaned as (
    select
        event_id,
        user_id,
        track_id,
        track_name,
        artist_name,
        genre,
        duration_ms,
        listened_ms,
        round(listened_ms / duration_ms * 100, 2) as listen_percentage,
        case when listened_ms / duration_ms >= 0.8 then false else true end as is_skipped,
        to_timestamp(timestamp) as event_timestamp,
        date(to_timestamp(timestamp)) as event_date,
        hour(to_timestamp(timestamp)) as event_hour,
        platform,
        country
    from source
),

de_dup as (
    select *,
        row_number() over (partition by event_id order by event_timestamp) as rn
    from cleaned
)

select * except(rn)
from de_dup
where rn = 1