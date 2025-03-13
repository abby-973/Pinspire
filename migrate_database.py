import sqlite3

# Connect to SQLite database
db_name = "pinspire.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

print(f"Connected to database '{db_name}' successfully")

# List of tables to migrate
tables = {
    "Users": """
        CREATE TABLE Users (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            FName TEXT NOT NULL,
            LName TEXT NOT NULL,
            Email TEXT UNIQUE NOT NULL,
            Username TEXT UNIQUE NOT NULL,
            CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """,
    "Pins": """
        CREATE TABLE Pins (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            ImgUrl TEXT NOT NULL,
            Title TEXT NOT NULL,
            Description TEXT,
            CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """,
    "Boards": """
        CREATE TABLE Boards (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            CoverImgUrl TEXT NOT NULL,
            Title TEXT NOT NULL,
            UserId INTEGER NOT NULL,
            CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (UserId) REFERENCES Users(Id) ON DELETE CASCADE
        )
    """,
    "BoardPins": """
        CREATE TABLE BoardPins (
            BoardId INTEGER,
            PinId INTEGER,
            CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (BoardId, PinId),
            FOREIGN KEY (BoardId) REFERENCES Boards(Id) ON DELETE CASCADE,
            FOREIGN KEY (PinId) REFERENCES Pins(Id) ON DELETE CASCADE
        )
    """,
    "Comments": """
        CREATE TABLE Comments (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Text TEXT NOT NULL,
            PinId INTEGER NOT NULL,
            UserId INTEGER NOT NULL,
            CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (PinId) REFERENCES Pins(Id) ON DELETE CASCADE,
            FOREIGN KEY (UserId) REFERENCES Users(Id) ON DELETE CASCADE
        )
    """
}

# Function to migrate a table
def migrate_table(table_name, create_statement):
    try:
        print(f"\nMigrating table: {table_name}...")

        # Rename old table
        cursor.execute(f"ALTER TABLE {table_name} RENAME TO {table_name}_old")

        # Create new table with CreatedDate column
        cursor.execute(create_statement)

        # Copy data into new table (excluding CreatedDate, which will default to current timestamp)
        column_names = [row[1] for row in cursor.execute(f"PRAGMA table_info({table_name}_old)")]
        columns_to_copy = ", ".join(column_names)  # All columns except CreatedDate

        cursor.execute(f"INSERT INTO {table_name} ({columns_to_copy}) SELECT {columns_to_copy} FROM {table_name}_old")

        # Drop old table
        cursor.execute(f"DROP TABLE {table_name}_old")

        print(f"{table_name} migrated successfully!")
    except Exception as e:
        print(f"Error migrating {table_name}: {e}")

# Run migration for each table
for table, sql in tables.items():
    migrate_table(table, sql)

# Commit changes and close connection
conn.commit()
conn.close()

print("\nDatabase migration completed successfully!")
