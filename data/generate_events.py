import duckdb
import random
from pathlib import Path
from datetime import datetime, timedelta

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "database" / "zomato.db"

con = duckdb.connect(str(DB_PATH))

TOTAL_USERS = 10000

cities = [
    "Lucknow",
    "Kanpur",
    "Agra",
    "Noida",
    "Varanasi"
]

devices = [
    "Android",
    "iOS"
]

foods = [
    "Pizza",
    "Burger",
    "Biryani",
    "Chinese",
    "Cake",
    "Coffee"
]

print("Generating Events...")

event_id = 1
search_id = 1
view_id = 1
menu_id = 1
cart_id = 1
checkout_id = 1
payment_id = 1
order_event_id = 1
delivery_event_id = 1


app_rows = []
search_rows = []
view_rows = []
menu_rows = []
cart_rows = []
checkout_rows = []
payment_rows = []
order_rows = []
delivery_rows = []


today = datetime.now()

for user in range(1, TOTAL_USERS + 1):

    if user % 500 == 0:
        print(f"Users Processed : {user}")

    sessions = random.randint(5, 12)

    for s in range(sessions):

        session = f"S{user}_{s}"

        ts = today - timedelta(
            days=random.randint(0,30),
            hours=random.randint(0,23),
            minutes=random.randint(0,59)
        )

        city = random.choice(cities)

        restaurant = random.randint(1,500)

        device = random.choice(devices)

        event_date = ts.date()