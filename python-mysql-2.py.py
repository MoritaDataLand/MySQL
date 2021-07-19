  
'''
 * @channel Morita DataLand
 * @author Morita Tarvirdians
 * @email tarvirdians.morita@gmail.com
 * @desc MySQL Python Tutorial
'''

import mysql.connector

db = mysql.connector.connect(host = "localhost", 
                            user= "root",
                            password = "root123",
                            auth_plugin='mysql_native_password',
                            db='CUSTOMER'
                            )

mycursor = db.cursor()


customers_data = [
    ("Lisa", "Lisa@gmail.com", "A02", "Los angles"),
    ("Peter", "Peter@mail.com", "A02", "New York" ),
    ("Joe", "Joe123@ymail.com", "B01", "New York" ),
    ("Lia", "LLiaaa@ymail.com", "B01", "Washington" )
]

items_data = [
    ("A01", "black", "Nike"),
    ("B01", "white", "Adidas"),
    ("A02", "blue", "Nike"),
    ("C01", "green", "Reebok")
]

Q1 = "CREATE TABLE Items (item_id VARCHAR(50) PRIMARY KEY, color VARCHAR(50), brand_name varchar(50))"
Q2 = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), email VARCHAR(100), item_FK VARCHAR(50), FOREIGN KEY(item_FK) REFERENCES Items(item_id), city VARCHAR(50))"

# mycursor.execute(Q1)
# mycursor.execute(Q2)
# mycursor.execute("SHOW TABLES")
# for i in mycursor.fetchall():
#     print(i)

Q3 = "INSERT INTO Items (item_id, color, brand_name) VALUES (%s, %s, %s)"
Q4 = "INSERT INTO customers (name , email, item_FK, city) VALUES (%s, %s, %s, %s)"

# for i in items_data:
#     mycursor.execute(Q3, i)

# mycursor.executemany(Q4, customers_data)

# db.commit()

Q5 = "SELECT customers.name AS customers_name, customers.city AS city, Items.brand_name as favorite_brand\
    FROM customers \
    RIGHT JOIN Items ON customers.item_FK = Items.item_id"

mycursor.execute(Q5)

for i in mycursor.fetchall():
    print(i)
