import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9900",
    database="assignments"
)
mycursor = mydb.cursor()
#mycursor.execute("create table data (name VARCHAR(255), address VARCHAR(255))")
query = "insert into data(name, address) values (%s, %s)"
val = ("Sandeep Roy", "Bangalore")
mycursor.execute(query, val)
mydb.commit()
print(mycursor.rowcount, "Record Inserted")
