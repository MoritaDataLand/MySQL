import mysql.connector

# connect to mysql
db = mysql.connector.connect(host="localhost",
                            user ="root",
                            password="root123",
                            db = "school")

mycursor = db.cursor()

# create database
mycursor.execute("CREATE DATABASE school")

# create table
mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age smallint)")

# insert into table
sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
values = ("Andy", 24)

mycursor.execute(sql,values)
db.commit()
print(mycursor.rowcount, "row was inserted")

# update table
mycursor.execute("UPDATE students SET age = 22 WHERE name='Andy'")
db.commit()

# delete from table
mycursor.execute("DELETE FROM students WHERE name='John'")
db.commit()

# select all from the table
mycursor.execute("SELECT * FROM students")
for x in mycursor.fetchall():
    print(x)