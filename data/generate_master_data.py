import duckdb
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("en_IN")

con = duckdb.connect("database/zomato.db")

# -----------------------------
# USERS
# -----------------------------

cities = [
    "Lucknow",
    "Kanpur",
    "Varanasi",
    "Prayagraj",
    "Agra",
    "Noida"
]

channels = [
    "Organic",
    "Google Ads",
    "Instagram",
    "Facebook",
    "Referral"
]

devices = [
    "Android",
    "iOS"
]

users = []

for i in range(1,10001):

    signup = fake.date_between("-365d","today")

    users.append(

        (
            i,
            fake.name(),
            f"user{i}@gmail.com",
            fake.msisdn()[:10],
            random.choice(["Male","Female"]),
            random.randint(18,60),
            random.choice(cities),
            signup,
            random.choice(channels),
            random.choice(devices),
            random.choice([True,False]),
            datetime.now()
        )

    )

con.executemany("""

INSERT INTO dim_users
VALUES (?,?,?,?,?,?,?,?,?,?,?,?)

""",users)

print("Users Inserted :",len(users))

# -----------------------------
# RESTAURANTS
# -----------------------------

cuisines = [
    "North Indian",
    "South Indian",
    "Chinese",
    "Pizza",
    "Burger",
    "Biryani",
    "Cafe"
]

restaurants=[]

for i in range(1,501):

    restaurants.append(

        (
            i,
            fake.company(),
            random.choice(cities),
            fake.street_name(),
            random.choice(cuisines),
            random.randint(200,1200),
            round(random.uniform(3.2,4.9),1),
            True,
            "09:00:00",
            "23:00:00",
            datetime.now()
        )

    )

con.executemany("""

INSERT INTO dim_restaurants
VALUES (?,?,?,?,?,?,?,?,?,?,?)

""",restaurants)

print("Restaurants Inserted :",len(restaurants))

con.close()

print("Master Data Generated Successfully ✅")