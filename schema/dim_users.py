import duckdb

con = duckdb.connect("database/zomato.db")

with open("schema/dim_users.sql", "r") as f:
    sql = f.read()

con.execute(sql)

print("✅ Tables Created Successfully!")

print(con.sql("SHOW TABLES"))

con.close()