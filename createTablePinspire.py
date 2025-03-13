import sqlite3

# Connect to SQLite database (creates if it doesn't exist)
db_name = "pinspire.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

print(f"Connected to database '{db_name}' successfully")

# Create Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    FName TEXT NOT NULL,
    LName TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    Username TEXT UNIQUE NOT NULL
);
''')

# Create Pins table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pins (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    ImgUrl TEXT NOT NULL,
    Title TEXT NOT NULL,
    Description TEXT
);
''')

# Create Boards table with a foreign key referencing Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Boards (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    CoverImgUrl TEXT NOT NULL,
    Title TEXT NOT NULL,
    UserId INTEGER NOT NULL,
    FOREIGN KEY (UserId) REFERENCES Users(Id) ON DELETE CASCADE
);
''')

# Create BoardPins table with foreign keys referencing Boards and Pins
cursor.execute('''
CREATE TABLE IF NOT EXISTS BoardPins (
    BoardId INTEGER,
    PinId INTEGER,
    PRIMARY KEY (BoardId, PinId),
    FOREIGN KEY (BoardId) REFERENCES Boards(Id) ON DELETE CASCADE,
    FOREIGN KEY (PinId) REFERENCES Pins(Id) ON DELETE CASCADE
);
''')

# Create Comments table with foreign keys referencing Pins and Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Comments (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Text TEXT NOT NULL,
    PinId INTEGER NOT NULL,
    UserId INTEGER NOT NULL,
    FOREIGN KEY (PinId) REFERENCES Pins(Id) ON DELETE CASCADE,
    FOREIGN KEY (UserId) REFERENCES Users(Id) ON DELETE CASCADE
);
''')

print("Tables created successfully!")

# Commit changes and close connection
conn.commit()
conn.close()

print(f"Database '{db_name}' setup completed!")
