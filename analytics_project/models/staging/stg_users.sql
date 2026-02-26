select
    user_id,
    user_name,
    email,
    created_at
from {{ source('analytics', 'raw_users') }}
where email is not null
