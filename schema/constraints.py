import duckdb
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DB_PATH = ROOT / "database" / "zomato.db"

SQL_FILE = ROOT / "schema" / "04_constraints.sql"

con = duckdb.connect(DB_PATH)

con.execute(SQL_FILE.read_text())

print("✅ Indexes Created Successfully")

con.close()