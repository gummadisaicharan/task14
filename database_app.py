import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
""")

# Insert user (Parameterized Query)
def insert_user(name, age, email):
    cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
                   (name, age, email))
    conn.commit()
    print("User inserted successfully.")

# Fetch all users
def fetch_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("\nUser Records:")
    for row in rows:
        print(row)

# Update user
def update_user(user_id, new_age):
    cursor.execute("UPDATE users SET age = ? WHERE id = ?",
                   (new_age, user_id))
    conn.commit()
    print("User updated successfully.")

# Delete user
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?",
                   (user_id,))
    conn.commit()
    print("User deleted successfully.")

# Sample Operations
insert_user("Sai", 22, "sai@email.com")
insert_user("Charan", 23, "charan@email.com")

fetch_users()

update_user(1, 25)
delete_user(2)

fetch_users()

# Close connection
conn.close()
