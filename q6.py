from mysql.connector import connect
conn = connect(
host="localhost",
user="root",
port=3307,
password="123456",
database="lab"
)
cur = conn.cursor()
cur.execute(""" 
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'new_user'@'%';
""")
conn.commit()
conn.close()
print("All privileges and grant option revoked from 'new_user'.")
