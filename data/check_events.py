import duckdb
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "database" / "zomato.db"

con = duckdb.connect(str(DB_PATH))

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

print("\n================ EVENT COUNTS ================\n")

for t in tables:

    cnt = con.execute(f"""
        SELECT COUNT(*)
        FROM {t}
    """).fetchone()[0]

    print(f"{t:<30} {cnt:,}")

con.close()