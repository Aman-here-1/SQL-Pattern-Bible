SELECT
customer_id,
order_date,
amount,

SUM(amount)
OVER
(
PARTITION BY customer_id
ORDER BY order_date
)
AS running_total

FROM orders;