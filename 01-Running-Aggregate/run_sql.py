import duckdb
from pathlib import Path

# Project Root
ROOT = Path(__file__).resolve().parent.parent

# Database Path
DB_PATH = ROOT / "database" / "zomato.db"

# SQL File
SQL_FILE = Path(__file__).resolve().parent / "question.sql"

con = duckdb.connect(str(DB_PATH))

query = SQL_FILE.read_text()

print(con.sql(query).fetchdf())

con.close()