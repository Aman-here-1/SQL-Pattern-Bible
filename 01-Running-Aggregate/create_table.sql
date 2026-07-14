CREATE TABLE orders
(
    customer_id INT,
    order_date DATE,
    amount INT
);


CREATE TABLE order (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    city VARCHAR(50),
    revenue DECIMAL(10,2)
);