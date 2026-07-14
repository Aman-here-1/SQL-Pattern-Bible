CREATE INDEX IF NOT EXISTS idx_user
ON app_open_events(user_id);

CREATE INDEX IF NOT EXISTS idx_search_user
ON search_events(user_id);

CREATE INDEX IF NOT EXISTS idx_restaurant_user
ON restaurant_view_events(user_id);

CREATE INDEX IF NOT EXISTS idx_menu_user
ON menu_view_events(user_id);

CREATE INDEX IF NOT EXISTS idx_cart_user
ON cart_events(user_id);

CREATE INDEX IF NOT EXISTS idx_payment_user
ON payment_events(user_id);

CREATE INDEX IF NOT EXISTS idx_order_user
ON order_events(user_id);