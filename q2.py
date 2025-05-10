from mysql.connector import connect 
conn = connect( host="localhost", user="root", port=3307, password="123456", database="lab" ) 
cur = conn.cursor() 
cur.execute(""" create or replace view dept_sal as select dept_name,sum(salary) as sal_total from instructor group by dept_name; """) 
conn.commit() 
conn.close() 
print("dept_sal view created successfully")