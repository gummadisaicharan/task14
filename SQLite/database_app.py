import sqlite3
import os

# -----------------------------
# Get the folder where this script is located
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create database path inside same folder
db_path = os.path.join(BASE_DIR, "internship.db")

# -----------------------------
# Connect to database
# -----------------------------
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print(f"📁 Database created at: {db_path}")

# -----------------------------
# Create table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
""")

conn.commit()

# -----------------------------
# Insert sample data
# -----------------------------
try:
    cursor.execute(
        "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
        ("Sai", 22, "sai@email.com")
    )
    conn.commit()
    print("✅ Sample user inserted.")
except sqlite3.IntegrityError:
    print("⚠ Sample user already exists.")

# -----------------------------
# Close connection
# -----------------------------
conn.close()
print("🔒 Database connection closed.")
import sqlite3
import os

# -----------------------------
# Get the folder where this script is located
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create database path inside same folder
db_path = os.path.join(BASE_DIR, "internship.db")

# -----------------------------
# Connect to database
# -----------------------------
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print(f"📁 Database created at: {db_path}")

# -----------------------------
# Create table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
""")

conn.commit()

# -----------------------------
# Insert sample data
# -----------------------------
try:
    cursor.execute(
        "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
        ("Sai", 22, "sai@email.com")
    )
    conn.commit()
    print("✅ Sample user inserted.")
except sqlite3.IntegrityError:
    print("⚠ Sample user already exists.")

# -----------------------------
# Close connection
# -----------------------------
conn.close()
print("🔒 Database connection closed.")
