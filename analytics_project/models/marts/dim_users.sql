{{ config(materialized='table') }}

select
    user_id,
    user_name,
    email,
    created_at
from {{ ref('stg_users') }}
