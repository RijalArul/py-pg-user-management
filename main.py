from create_database import create_or_replace_database
from create_table import create_users_table
from insert_users import insert_users

def main():
    print("Starting the user management setup...")
    
    print("\nStep 1: Creating or replacing the database...")
    create_or_replace_database()
    
    print("\nStep 2: Creating the users table...")
    create_users_table()

    print("\nStep 3: Inserting user data...")
    insert_users()
    
    print("\nAll steps completed successfully!")

if __name__ == "__main__":
    main()
