from mysql.connector import connect
conn = connect(
host="localhost",
user="root",
port=3307,
password="123456",
database="lab"
)
cur = conn.cursor()
cur.execute("grant select on faculty to student;")
conn.commit()
conn.close()
print("role student granted select privileges successfully")
