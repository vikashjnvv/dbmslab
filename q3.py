from mysql.connector import connect
conn = connect(
host="localhost",
user="root",
port=3307,
password="123456",
database="lab"
)
cur = conn.cursor()
cur.execute("create role if not exists 'student';")
conn.commit()
conn.close()
print("role student created successfully")
