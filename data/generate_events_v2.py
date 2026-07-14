import duckdb
import random
from pathlib import Path
from datetime import datetime, timedelta

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "database" / "zomato.db"

con = duckdb.connect(str(DB_PATH))

TOTAL_USERS = 10000

cities = ["Lucknow","Kanpur","Agra","Noida","Varanasi"]
devices = ["Android","iOS"]
foods = ["Pizza","Burger","Biryani","Chinese","Cake","Coffee"]

print("Generating Events...")

today = datetime.now()

ids = {
    "event":1,"search":1,"view":1,"menu":1,"cart":1,
    "checkout":1,"payment":1,"order":1,"delivery":1
}

batch = {
    "app":[], "search":[], "view":[], "menu":[],
    "cart":[], "checkout":[], "payment":[],
    "order":[], "delivery":[]
}

BATCH_SIZE = 5000

def flush():
    if batch["app"]:
        con.executemany("INSERT INTO app_open_events VALUES (?,?,?,?,?,?,?,?)", batch["app"])
        batch["app"].clear()
    if batch["search"]:
        con.executemany("INSERT INTO search_events VALUES (?,?,?,?,?,?,?)", batch["search"])
        batch["search"].clear()
    if batch["view"]:
        con.executemany("INSERT INTO restaurant_view_events VALUES (?,?,?,?,?,?)", batch["view"])
        batch["view"].clear()
    if batch["menu"]:
        con.executemany("INSERT INTO menu_view_events VALUES (?,?,?,?,?,?)", batch["menu"])
        batch["menu"].clear()
    if batch["cart"]:
        con.executemany("INSERT INTO cart_events VALUES (?,?,?,?,?,?,?)", batch["cart"])
        batch["cart"].clear()
    if batch["checkout"]:
        con.executemany("INSERT INTO checkout_events VALUES (?,?,?,?,?,?)", batch["checkout"])
        batch["checkout"].clear()
    if batch["payment"]:
        con.executemany("INSERT INTO payment_events VALUES (?,?,?,?,?,?,?)", batch["payment"])
        batch["payment"].clear()
    if batch["order"]:
        con.executemany("INSERT INTO order_events VALUES (?,?,?,?,?,?)", batch["order"])
        batch["order"].clear()
    if batch["delivery"]:
        con.executemany("INSERT INTO delivery_events VALUES (?,?,?,?,?,?)", batch["delivery"])
        batch["delivery"].clear()

for user in range(1, TOTAL_USERS + 1):
    if user % 500 == 0:
        print(f"Processed Users: {user}")

    for s in range(random.randint(5,12)):
        session = f"S{user}_{s}"
        ts = today - timedelta(days=random.randint(0,30),
                               hours=random.randint(0,23),
                               minutes=random.randint(0,59))
        d = ts.date()
        city = random.choice(cities)
        device = random.choice(devices)
        restaurant = random.randint(1,500)

        batch["app"].append((ids["event"],user,session,device,"9.2.1",ts,d,city))
        ids["event"] += 1

        if random.random() > 0.85:
            continue

        batch["search"].append((ids["search"],user,session,random.choice(foods),ts,d,city))
        ids["search"] += 1

        if random.random() > 0.80:
            continue

        batch["view"].append((ids["view"],user,restaurant,session,ts,d))
        ids["view"] += 1

        if random.random() > 0.75:
            continue

        batch["menu"].append((ids["menu"],user,restaurant,session,ts,d))
        ids["menu"] += 1

        if random.random() > 0.55:
            continue

        batch["cart"].append((ids["cart"],user,restaurant,session,
                              random.randint(250,1200),ts,d))
        ids["cart"] += 1

        if random.random() > 0.90:
            continue

        batch["checkout"].append((ids["checkout"],user,restaurant,session,ts,d))
        ids["checkout"] += 1

        if random.random() > 0.95:
            continue

        oid = ids["order"]

        batch["payment"].append((ids["payment"],user,oid,
                                 random.choice(["UPI","Card","Wallet","COD"]),
                                 "SUCCESS",ts,d))
        ids["payment"] += 1

        batch["order"].append((oid,oid,user,restaurant,ts,d))
        ids["order"] += 1

        batch["delivery"].append((ids["delivery"],oid,
                                  random.randint(1,500),
                                  "DELIVERED",
                                  ts + timedelta(minutes=random.randint(20,50)),
                                  d))
        ids["delivery"] += 1

        if len(batch["app"]) >= BATCH_SIZE:
            flush()

flush()
con.close()

print("Done.")
