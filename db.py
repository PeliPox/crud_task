import psycopg2

def get_connection():
    return psycopg2.connect(
        host='localhost',
        database='crud_mini',
        user='postgres',
        password='admin'
    )

conn = get_connection()
print("OK")
conn.close()