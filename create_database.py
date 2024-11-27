import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_or_replace_database():
    try:
        conn = psycopg2.connect(
            dbname="postgres",  
            user="postgres",
            password="postgres",
            host="localhost"
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 
        cursor = conn.cursor()

        cursor.execute("DROP DATABASE IF EXISTS \"g2g-user-management\";")
        print("Existing database dropped (if it existed).")

        cursor.execute("CREATE DATABASE \"g2g-user-management\";")
        print("Database 'g2g-user-management' created successfully!")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

