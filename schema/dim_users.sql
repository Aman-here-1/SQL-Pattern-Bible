-- =====================================================
-- PRODUCT ANALYTICS
-- Dimension Table : Users
-- Grain : One Row = One User
-- =====================================================

CREATE TABLE dim_users (

    user_id INTEGER PRIMARY KEY,

    user_name VARCHAR NOT NULL,

    email VARCHAR UNIQUE,

    phone VARCHAR,

    gender VARCHAR,

    age INTEGER,

    city VARCHAR,

    signup_date DATE,

    acquisition_channel VARCHAR,

    device_type VARCHAR,

    is_premium BOOLEAN,

    created_at TIMESTAMP

);