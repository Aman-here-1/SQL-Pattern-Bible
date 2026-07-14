import duckdb
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DB_PATH = ROOT / "database" / "zomato.db"

SQL_FILE = ROOT / "schema" / "03_event_tables.sql"

con = duckdb.connect(DB_PATH)

con.execute(SQL_FILE.read_text())

print("✅ Event Tables Created Successfully!")

print(con.execute("SHOW TABLES").fetchdf())

con.close()