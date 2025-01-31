import string
import random
import mysql.connector
a=string.ascii_letters
b=string.digits
c=string.punctuation
d=a+b+c
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rohan2309",
  database="mydatabase"
)
mycursor = conn.cursor()
n=int(input("Enter the length of password"))
password = "".join(random.choices(d, k=n))
print("Generated Password:", password)
sql = "INSERT INTO password (a) VALUES (%s)"
val = (password,)  
mycursor.execute(sql, val)
conn.commit()
conn.close()
print("Password stored in database successfully!")