# 📌 Task 14 – Database Operations Using SQLite

## 🧑‍💻 Python Developer Internship


## 📖 Project Overview

This project demonstrates how to perform basic database operations using **SQLite in Python**.

The objective of this task was to understand how backend systems store and manage data using a relational database. In this project, I implemented CRUD operations (Create, Read, Update, Delete) using Python’s built-in `sqlite3` module.

Through this task, I learned how databases interact with applications and how structured data is stored securely.


## 🎯 Learning Objectives

* Understand what SQLite is and how it works
* Connect Python to a database file
* Create tables programmatically
* Perform CRUD operations
* Use parameterized queries to prevent SQL injection
* Commit and close database connections properly
* Handle database errors using exception handling

---

## 🛠 Technologies Used

* Python 3
* sqlite3 (Built-in Python module)
* SQLite Database (.db file)
* DB Browser for SQLite (for viewing database file)

---

## 📂 Project Structure

```
Task-14-SQLite/
│
├── database_app.py      # Main Python script
├── internship.db        # SQLite database file (auto-generated)
└── README.md            # Project documentation
```

---

## 🗄 What is SQLite?

SQLite is a lightweight, serverless relational database management system.

Unlike other databases (like MySQL or PostgreSQL), SQLite does not require installation of a separate server. The entire database is stored in a single `.db` file.

It is commonly used for:

* Small applications
* Learning database fundamentals
* Embedded systems
* Local application storage

---

## 🔄 What is CRUD?

CRUD represents the four main database operations:

* **Create** → Insert new records
* **Read** → Retrieve existing records
* **Update** → Modify existing records
* **Delete** → Remove records

This project implements all four operations using SQL queries inside Python.

---

## 🔍 Implementation Details

### 1️⃣ Database Connection

The database is created automatically in the same folder as the Python file using:

```python
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
```

If the file does not exist, SQLite automatically creates it.

---

### 2️⃣ Table Creation

The project creates a table named `users` with the following structure:

| Column | Type    | Constraint                |
| ------ | ------- | ------------------------- |
| id     | INTEGER | PRIMARY KEY AUTOINCREMENT |
| name   | TEXT    | NOT NULL                  |
| age    | INTEGER | —                         |
| email  | TEXT    | UNIQUE                    |

* `PRIMARY KEY AUTOINCREMENT` automatically generates unique IDs.
* `UNIQUE` constraint prevents duplicate emails.

---

### 3️⃣ Insert Operation (Create)

Records are inserted using parameterized queries:

```python
cursor.execute(
    "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
    (name, age, email)
)
```

This ensures secure insertion of data.

---

### 4️⃣ Fetch Operation (Read)

```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
```

This retrieves all user records and displays them neatly.

---

### 5️⃣ Update Operation

```python
cursor.execute(
    "UPDATE users SET age = ? WHERE id = ?",
    (new_age, user_id)
)
```

This updates specific user records based on ID.

---

### 6️⃣ Delete Operation

```python
cursor.execute(
    "DELETE FROM users WHERE id = ?",
    (user_id,)
)
```

This removes selected records from the table.

---

## 🔐 Why Parameterized Queries?

Parameterized queries are used to:

* Prevent SQL Injection attacks
* Safely handle user input
* Improve database security

Instead of directly inserting values into SQL strings, placeholders (`?`) are used.

---

## 💾 Commit and Close

After performing insert, update, or delete operations:

```python
conn.commit()
```

This saves changes permanently.

Finally:

```python
conn.close()
```

This safely closes the database connection and prevents data corruption.

---

## ⚠ Error Handling

The project uses `try-except` blocks to handle:

* Duplicate email errors (UNIQUE constraint)
* Invalid update/delete operations
* Unexpected database errors

This prevents the application from crashing and improves reliability.

---

## 🆚 SQL vs NoSQL (Basic Understanding)

| SQL               | NoSQL              |
| ----------------- | ------------------ |
| Structured tables | Flexible structure |
| Fixed schema      | Dynamic schema     |
| Relational        | Non-relational     |
| Example: SQLite   | Example: MongoDB   |

SQLite is a relational SQL-based database.

---

## 🚀 How to Run the Project

1. Make sure Python 3 is installed.
2. Open terminal in the project folder.
3. Run:

```
python database_app.py
```

4. The `internship.db` file will be automatically created in the same folder.
5. You can open the file using DB Browser for SQLite to view stored data.

---

## 🎓 Learning Outcome

After completing this task, I now understand:

* How backend systems store structured data
* How relational databases work
* How to write secure SQL queries
* The importance of constraints like PRIMARY KEY and UNIQUE
* How applications manage data internally

This task helped me gain foundational knowledge in backend development and database management.

## 🔮 Future Improvements

In future versions, I plan to:

* Add a menu-driven interface for user interaction
* Add input validation
* Connect the database to a web application (Flask/Django)
* Implement logging for better debugging

## ✅ Conclusion

This task provided practical experience in handling databases using Python. It strengthened my understanding of backend data storage and real-world CRUD operations.

Completing this project helped me move one step closer to becoming confident in backend development.

ng your developer identity 😌
