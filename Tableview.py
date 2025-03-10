import sqlite3
from tabulate import tabulate

def display_all_tables(db_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Get all table names from the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if not tables:
        print("No tables found in the database.")
        return

    # Iterate over each table and display its contents
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")

        # Fetch all records from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Fetch column names
        column_names = [description[0] for description in cursor.description]

        # Display the table
        if rows:
            print(tabulate(rows, headers=column_names, tablefmt="grid"))
        else:
            print(f"No records found in table {table_name}")

    # Close the database connection
    conn.close()

# Example usage with your database
db_name = "database.db"  # Your actual database file
display_all_tables(db_name)
