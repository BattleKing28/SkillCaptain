import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="2803")

cursor = mydb.cursor()

cursor.execute("use test;")

cursor.execute("CREATE TABLE emp1(Name varchar(50), Age int)")
try:
    cursor.execute("INSERT INTO emp1 VALUES ('Nick' , 25)")
    cursor.execute("INSERT INTO emp1 VALUES ('James' , 28)")
except Exception as err:
    print(f"Error {str(err)}")

cursor.execute("SELECT * FROM emp1")
results = cursor.fetchall()

print(results)

mydb.close()
