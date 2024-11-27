import psycopg2
from email_validator import validate_email, EmailNotValidError

def insert_users():
    users_to_insert = [
        {"username": "Alice", "email": "alice@example.com"},
        {"username": "Bob", "email": "bob@example.com"},
        {"username": "Charlie", "email": "Charlie@example.com"},
        {"username": "Dave", "email": "dave@example"},
        {"username": "Dave", "email": "daVVe@gmail.com"},
        {"username": "Eve", "email": "eve@example.com"}
    ]

    conn = psycopg2.connect(
        dbname="g2g-user-management",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    cursor = conn.cursor()

    for user in users_to_insert:
        try:
            email = validate_email(user['email']).email
            cursor.execute(
                "INSERT INTO users (username, email) VALUES (%s, %s)",
                (user['username'], email)
            )
        except EmailNotValidError as e:
            print(f"Invalid email '{user['email']}': {e}")
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print(f"Failed to insert user {user}: {e}")
        else:
            conn.commit()
            print(f"User {user['username']} inserted successfully!")

    cursor.close()
    conn.close()
