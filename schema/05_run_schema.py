import duckdb

con = duckdb.connect("database/zomato.db")

with open("schema/01_create_tables.sql", "r") as f:
    sql = f.read()

con.execute(sql)

print("✅ Tables Created Successfully!")

print(con.sql("SHOW TABLES"))

con.close()