-- =====================================================
-- ZOMATO PRODUCT ANALYTICS
-- FACT TABLES
-- =====================================================

---------------------------------------------------------
-- FACT ORDERS
---------------------------------------------------------

CREATE TABLE IF NOT EXISTS fact_orders (

    order_id BIGINT PRIMARY KEY,

    user_id INTEGER NOT NULL,

    restaurant_id INTEGER NOT NULL,

    order_timestamp TIMESTAMP,

    order_date DATE,

    order_status VARCHAR,

    order_amount DECIMAL(10,2),

    delivery_fee DECIMAL(10,2),

    platform_fee DECIMAL(10,2),

    discount_amount DECIMAL(10,2),

    tax_amount DECIMAL(10,2),

    final_amount DECIMAL(10,2),

    payment_method VARCHAR,

    payment_status VARCHAR,

    delivery_partner_id INTEGER,

    delivery_time_minutes INTEGER,

    customer_rating INTEGER,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

---------------------------------------------------------
-- FACT PAYMENTS
---------------------------------------------------------

CREATE TABLE IF NOT EXISTS fact_payments (

    payment_id BIGINT PRIMARY KEY,

    order_id BIGINT,

    user_id INTEGER,

    payment_method VARCHAR,

    payment_gateway VARCHAR,

    payment_status VARCHAR,

    payment_amount DECIMAL(10,2),

    payment_timestamp TIMESTAMP,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

---------------------------------------------------------
-- FACT DELIVERIES
---------------------------------------------------------

CREATE TABLE IF NOT EXISTS fact_deliveries (

    delivery_id BIGINT PRIMARY KEY,

    order_id BIGINT,

    delivery_partner_id INTEGER,

    pickup_time TIMESTAMP,

    delivered_time TIMESTAMP,

    delivery_duration_minutes INTEGER,

    delivery_status VARCHAR,

    customer_rating INTEGER,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);