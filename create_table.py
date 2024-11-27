import psycopg2

def create_users_table():
    conn = psycopg2.connect(
        dbname="g2g-user-management",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS users;")
    print("Existing users table dropped (if it existed).")

    cursor.execute("""
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

        CREATE TABLE IF NOT EXISTS users (
            uuid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            deleted_at TIMESTAMP
        );
    """)
    print("Users table created successfully.")
    conn.commit()
    cursor.close()
    conn.close()