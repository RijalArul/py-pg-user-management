import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_or_replace_database():
    conn = psycopg2.connect(
        dbname="g2g-user-management",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    cursor.execute("DROP DATABASE IF EXISTS user_management;")
    print("Existing database dropped (if it existed).")

    cursor.execute("CREATE DATABASE user_management;")
    print("Database created successfully!")
    cursor.close()
    conn.close()
