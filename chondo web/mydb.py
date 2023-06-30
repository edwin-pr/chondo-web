import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydb"
)

print(mydb)

#mydb = mysql.connector.connect(
  #host="localhost",
  #user="myusername",
  #passwd="mypassword"
#)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydb")

#mycursor.execute("SHOW DATABASES")

#mycursor.execute("CREATE TABLE customers1 (name VARCHAR(255), phonenumber INT(15), idno INT(10), address VARCHAR(255))")

#mycursor.execute("SHOW TABLES")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "records inserted.")
for x in mycursor:
  print(x)