-- =====================================================
-- TABLE : app_open_events
-- GRAIN : One Row = One App Open Event
-- PURPOSE : Track every app launch
-- =====================================================

CREATE TABLE IF NOT EXISTS app_open_events (

    event_id BIGINT PRIMARY KEY,

    user_id INTEGER NOT NULL,

    session_id VARCHAR,

    device_type VARCHAR,

    app_version VARCHAR,

    event_timestamp TIMESTAMP,

    event_date DATE,

    city VARCHAR,

    FOREIGN KEY(user_id)
    REFERENCES dim_users(user_id)

);