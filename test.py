import psycopg2
try:
    conn = psycopg2.connect(
        host="localhost",
        database="moviedb",
        user="root",
        password="root",
        port=5432)
except:
    print("I am unable to connect to the database.")
    
print(conn)