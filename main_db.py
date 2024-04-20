import psycopg2 

conn = psycopg2.connect(database = "dpu_database", 
                        user = "postgres", 
                        host= '127.0.0.1',
                        password = "admin",
                        port = 5432)


cur = conn.cursor()
cur.execute('SELECT * FROM public.students ORDER BY id ASC;')
rows = cur.fetchall()
conn.commit()
conn.close()
for row in rows:
    print(row)