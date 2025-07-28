import mysql.connector
import os
from datetime import datetime

LOG_FILE = "expense_log.txt"

# --- DB CONNECTION ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",         
    password="Ruchi@2004", 
    database="expenses_db",
    port = 3307
)
cursor = conn.cursor()

# SQL table creation
cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    description VARCHAR(255),
    amount DECIMAL(10,2),
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
)
''')
conn.commit()

# Functions

def log_entry(entry):
    with open(LOG_FILE, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {entry}\n")

def delete_log_file():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print("Log file deleted.")

def reset_tables():
    cursor.execute("DELETE FROM expenses")
    cursor.execute("DELETE FROM categories")
    cursor.execute("ALTER TABLE expenses AUTO_INCREMENT = 1")
    cursor.execute("ALTER TABLE categories AUTO_INCREMENT = 1")
    conn.commit()
    delete_log_file()
    print("Tables cleared and AUTO_INCREMENT reset.")

def add_category():
    name = input("Enter new category name: ").strip()
    try:
        cursor.execute("INSERT INTO categories (name) VALUES (%s)", (name,))
        conn.commit()
        print("Category added.")
        log_entry(f"Category added: {name}")
    except mysql.connector.IntegrityError:
        print("Category already exists.")


def delete_category(category_id):
    confirm = input("Are you sure you want to delete this category? (y/n): ").lower()
    if confirm == 'y':
        cursor.execute("DELETE FROM categories WHERE id = %s", (category_id,))
        conn.commit()
        print("Category deleted.")
    else:
        print("Deletion canceled.")


def add_expense(category_id):
    description = input("Enter expense description: ").strip()
    amount = input("Enter amount: ").strip()
    try:
        amount = float(amount)
        cursor.execute(
            "INSERT INTO expenses (category_id, description, amount) VALUES (%s, %s, %s)",
            (category_id, description, amount)
        )
        conn.commit()
        print("Expense added.")
        log_entry(f"Expense added: Category ID {category_id}, Description: {description}, Amount: {amount}")
    except ValueError:
        print("Invalid amount. Must be a number.")


def display_categories():
    try:
        cursor.execute("SELECT id, name FROM categories ORDER BY id")
        categories = cursor.fetchall()
        if not categories:
            print("No categories found.")
            return

        print("\nCategories:")
        for cat in categories:
            print(f"{cat[0]}. {cat[1]}")
        print("0. Add New Category")
        print("-1. Back to Main Menu")

        choice = input("Select a category by ID: ").strip()

        if choice == '0':
            add_category()
        elif choice == '-1':
            return
        else:
            try:
                category_id = int(choice)
                category_ids = [c[0] for c in categories]
                if category_id in category_ids:
                    category_actions(category_id)
                else:
                    print("Invalid category ID.")
            except ValueError:
                print("Invalid input.")
    except Exception as e:
        print("Error:", e)


def category_actions(category_id):
    while True:
        print("\nOptions for category ID", category_id)
        print("1. Add Expense")
        print("2. Delete Category")
        print("3. Back")
        action = input("Choose an action: ").strip()

        if action == '1':
            add_expense(category_id)
        elif action == '2':
            delete_category(category_id)
            break
        elif action == '3':
            break
        else:
            print("Invalid option.")

def display_expenses():
    try:
        cursor.execute('''
            SELECT e.id, c.name AS category, e.description, e.amount
            FROM expenses e
            JOIN categories c ON e.category_id = c.id
            ORDER BY e.id
        ''')
        expenses = cursor.fetchall()

        if not expenses:
            print("No expenses recorded.")
            return

        print("\nExpenses:")
        print("{:<5} {:<15} {:<30} {:>10}".format("ID", "Category", "Description", "Amount"))
        print("-" * 65)
        for exp in expenses:
            print("{:<5} {:<15} {:<30} {:>10.2f}".format(exp[0], exp[1], exp[2], exp[3]))

    except Exception as e:
        print("Error retrieving expenses:", e)


def main_menu():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. View Categories")
        print("2. Add Category")
        print("3. View Expenses")
        print("4. Reset tables")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            display_categories()
        elif choice == '2':
            add_category()
        elif choice == '3':
            display_expenses()
        elif choice == '4':
            reset_tables()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid selection.")


# Start the app
main_menu()
