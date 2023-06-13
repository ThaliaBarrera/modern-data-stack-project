select
    order_id,
    customer_id,
    order_status,
    order_approved_at as order_date
from {{ source('raw_data', 'orders') }}