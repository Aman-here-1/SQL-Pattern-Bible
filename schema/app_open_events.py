import duckdb
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DB_PATH = ROOT / "database" / "zomato.db"

SQL_FILE = Path(__file__).with_suffix(".sql")

con = duckdb.connect(DB_PATH)

con.execute(SQL_FILE.read_text())

print("✅ app_open_events Created Successfully!")

print(
    con.execute("""
        SHOW TABLES
    """).fetchdf()
)

con.close()