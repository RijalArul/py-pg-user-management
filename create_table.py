import psycopg2


def create_users_table():
    conn = psycopg2.connect(
        dbname="g2g-user-management",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute("""
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

    CREATE TABLE IF NOT EXISTS users (
        uuid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        deleted_at TIMESTAMPTZ
    );
""")


    cursor.execute("""
        CREATE OR REPLACE FUNCTION enforce_lowercase_email()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.email = LOWER(NEW.email);
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
    """)

    cursor.execute("""
        CREATE TRIGGER lowercase_email_trigger
        BEFORE INSERT OR UPDATE ON users
        FOR EACH ROW
        EXECUTE FUNCTION enforce_lowercase_email();
    """)
    conn.commit()
    print("Table created successfully!")
    cursor.close()
    conn.close()
