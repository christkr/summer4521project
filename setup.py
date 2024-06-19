import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql123"
)

my_cursor = mydb.cursor()
create_table = """CREATE TABLE """
my_cursor.execute("CREATE DATABASE IF NOT EXISTS Groceries;")
