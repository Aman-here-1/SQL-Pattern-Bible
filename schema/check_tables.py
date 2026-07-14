import duckdb

con = duckdb.connect("database/zomato.db")

print(con.sql("SHOW TABLES"))

con.close()