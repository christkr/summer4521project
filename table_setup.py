import mysql.connector

with mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql123",
    database="Groceries"
) as conn:
    cur = conn.cursor()
    query = "CREATE USER 'test'@'localhost' IDENTIFIED BY 'password';"
    cur.execute(query)
    cur.execute("FLUSH PRIVILEGES;")
    cur.execute("GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT on *.* TO 'test'@'localhost';")
    cur.execute("FLUSH PRIVILEGES;")

