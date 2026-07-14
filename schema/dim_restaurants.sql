CREATE TABLE dim_restaurants (

    restaurant_id INTEGER PRIMARY KEY,

    restaurant_name VARCHAR NOT NULL,

    city VARCHAR,

    locality VARCHAR,

    cuisine VARCHAR,

    avg_cost_for_two INTEGER,

    rating DECIMAL(2,1),

    is_active BOOLEAN,

    opening_time TIME,

    closing_time TIME,

    created_at TIMESTAMP

);