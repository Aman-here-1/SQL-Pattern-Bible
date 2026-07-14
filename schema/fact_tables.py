import duckdb
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DB_PATH = ROOT / "database" / "zomato.db"

SQL_FILE = ROOT / "schema" / "02_fact_tables.sql"

con = duckdb.connect(DB_PATH)

con.execute(SQL_FILE.read_text())

print("✅ Fact Tables Created Successfully!")

print(con.execute("SHOW TABLES").fetchdf())

con.close()