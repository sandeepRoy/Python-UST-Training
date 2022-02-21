import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9900",
    database="assignments"
)
mycursor = mydb.cursor()
#mycursor.execute("create table data (name VARCHAR(255), address VARCHAR(255))")

#Insert into table

#Without Optimizing- Wildcard %s
#query = "insert into data(name, address) values (%s, %s)"

#With Optimizing
query = 'insert into data(name, address) values ( "Name2 Surname2", "Hauj Khas, New Delhi")'

#Update value in table
#Optimized
#query = 'explain update data set name = "Roy Sandeep", address = "Indranagar, Bangalore"'

mycursor.execute(query)
mydb.commit()
print(mycursor.rowcount, "Record Inserted")