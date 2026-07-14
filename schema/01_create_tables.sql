-- ==========================================
-- SQL Pattern Bible
-- Product Analytics Database
-- ==========================================

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    full_name VARCHAR,
    email VARCHAR,
    phone VARCHAR,
    gender VARCHAR,
    city VARCHAR,
    signup_date DATE,
    acquisition_channel VARCHAR,
    is_gold_member BOOLEAN
);

CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY,
    restaurant_name VARCHAR,
    city VARCHAR,
    cuisine VARCHAR,
    rating DECIMAL(2,1),
    cost_for_two INTEGER,
    is_active BOOLEAN
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    restaurant_id INTEGER,
    order_time TIMESTAMP,
    order_status VARCHAR,
    subtotal DECIMAL(10,2),
    delivery_fee DECIMAL(10,2),
    platform_fee DECIMAL(10,2),
    discount DECIMAL(10,2),
    total_amount DECIMAL(10,2),
    payment_method VARCHAR
);