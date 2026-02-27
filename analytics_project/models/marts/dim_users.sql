{{ config(materialized='incremental') }}

select
    user_id,
    user_name,
    email,
    created_at
from {{ ref('stg_users') }}

{% if is_incremental() %}
  where created_at > (select max(created_at) from {{ this }})
{% endif %}