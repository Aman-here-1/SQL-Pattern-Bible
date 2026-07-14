import duckdb

con = duckdb.connect("database/zomato.db")

tables = [
    "app_open_events",
    "search_events",
    "restaurant_view_events",
    "menu_view_events",
    "cart_events",
    "checkout_events",
    "payment_events",
    "order_events",
    "delivery_events"
]

for t in tables:
    con.execute(f"DELETE FROM {t}")

con.close()

print("✅ Event tables cleaned")