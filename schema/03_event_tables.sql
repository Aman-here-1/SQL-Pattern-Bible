-- =====================================================
-- APP OPEN EVENTS
-- =====================================================

CREATE TABLE IF NOT EXISTS app_open_events (

    event_id BIGINT PRIMARY KEY,

    user_id INTEGER NOT NULL,

    session_id VARCHAR,

    event_timestamp TIMESTAMP,

    event_date DATE,

    device_type VARCHAR,

    city VARCHAR

);

-- =====================================================
-- SEARCH EVENTS
-- =====================================================

CREATE TABLE IF NOT EXISTS search_events (

    search_id BIGINT PRIMARY KEY,

    user_id INTEGER,

    session_id VARCHAR,

    search_query VARCHAR,

    event_timestamp TIMESTAMP,

    event_date DATE,

    city VARCHAR

);

-- =====================================================
-- RESTAURANT VIEW EVENTS
-- =====================================================

CREATE TABLE IF NOT EXISTS restaurant_view_events (

    view_id BIGINT PRIMARY KEY,

    user_id INTEGER,

    restaurant_id INTEGER,

    session_id VARCHAR,

    event_timestamp TIMESTAMP,

    event_date DATE

);

-- =====================================================
-- MENU VIEW EVENTS
-- =====================================================

CREATE TABLE IF NOT EXISTS menu_view_events (

    menu_view_id BIGINT PRIMARY KEY,

    user_id INTEGER,

    restaurant_id INTEGER,

    session_id VARCHAR,

    event_timestamp TIMESTAMP,

    event_date DATE

);

-- =====================================================
-- CART EVENTS
-- =====================================================

CREATE TABLE IF NOT EXISTS cart_events (

    cart_id BIGINT PRIMARY KEY,

    user_id INTEGER,

    restaurant_id INTEGER,

    session_id VARCHAR,

    cart_value DECIMAL(10,2),

    event_timestamp TIMESTAMP,

    event_date DATE

);

-- =====================================================
-- CHECKOUT EVENTS
-- =====================================================

CREATE TABLE IF NOT EXISTS checkout_events (

    checkout_id BIGINT PRIMARY KEY,

    user_id INTEGER,

    restaurant_id INTEGER,

    session_id VARCHAR,

    event_timestamp TIMESTAMP,

    event_date DATE

);

-- =====================================================
-- PAYMENT EVENTS
-- =====================================================

CREATE TABLE IF NOT EXISTS payment_events (

    payment_event_id BIGINT PRIMARY KEY,

    user_id INTEGER,

    order_id BIGINT,

    payment_method VARCHAR,

    payment_status VARCHAR,

    event_timestamp TIMESTAMP,

    event_date DATE

);

-- =====================================================
-- ORDER EVENTS
-- =====================================================

CREATE TABLE IF NOT EXISTS order_events (

    order_event_id BIGINT PRIMARY KEY,

    order_id BIGINT,

    user_id INTEGER,

    restaurant_id INTEGER,

    event_timestamp TIMESTAMP,

    event_date DATE

);

-- =====================================================
-- DELIVERY EVENTS
-- =====================================================

CREATE TABLE IF NOT EXISTS delivery_events (

    delivery_event_id BIGINT PRIMARY KEY,

    order_id BIGINT,

    delivery_partner_id INTEGER,

    delivery_status VARCHAR,

    event_timestamp TIMESTAMP,

    event_date DATE

);