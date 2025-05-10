from mysql.connector import connect 
conn = connect( host="localhost", user="root", port=3307, password="123456", database="lab" ) 
cur = conn.cursor() 
cur.execute(""" create or replace view faculty as select id, name, dept_name from instructor; """) 
conn.commit() 
conn.close() 
print("faculty view created successfully")
