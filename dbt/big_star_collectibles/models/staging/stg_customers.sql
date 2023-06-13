select
    customer_id,
    customer_state,
    customer_city
from {{ source('raw_data', 'customers') }}
