import duckdb
from pathlib import Path

# Project Root
ROOT = Path(__file__).resolve().parent.parent

# Database Path
DB_PATH = ROOT / "database" / "zomato.db"

# SQL File
SQL_FILE = Path(__file__).with_suffix(".sql")

# Connect Database
con = duckdb.connect(DB_PATH)

# Execute SQL
con.execute(SQL_FILE.read_text())

print("✅ dim_restaurants Created Successfully!")

# Verify Tables
print(
    con.execute("""
    SHOW TABLES
    """).fetchdf()
)

con.close()