import duckdb
from pathlib import Path

# Project Root
ROOT = Path(__file__).resolve().parent.parent

# Database Path
DB_PATH = ROOT / "database" / "zomato.db"

print("Database Path:", DB_PATH)

con = duckdb.connect(str(DB_PATH))

print("\n========== TABLES ==========")
print(con.sql("SHOW TABLES").fetchdf())

print("\n========== USERS ==========")
print(con.sql("SELECT COUNT(*) AS total_users FROM dim_users").fetchdf())

print("\n========== RESTAURANTS ==========")
print(con.sql("SELECT COUNT(*) AS total_restaurants FROM dim_restaurants").fetchdf())

con.close()