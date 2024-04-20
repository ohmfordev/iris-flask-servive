import psycopg2 


def connect_db():
    conn = psycopg2.connect(database = "dpu_database", 
                            user = "postgres", 
                            host= '127.0.0.1',
                            password = "admin",
                            port = 5432)    