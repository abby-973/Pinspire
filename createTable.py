
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.db')
print("Connected to database successfully")

# Create tables
conn.execute('''
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    username TEXT UNIQUE NOT NULL
);
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS pins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT
);
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS board (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cover_image TEXT NOT NULL,
    title TEXT NOT NULL
);
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS boardPins (
    board_id INTEGER,
    pin_id INTEGER,
    PRIMARY KEY (board_id, pin_id),
    FOREIGN KEY (board_id) REFERENCES board(id) ON DELETE CASCADE,
    FOREIGN KEY (pin_id) REFERENCES pins(id) ON DELETE CASCADE
);
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    pin_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (pin_id) REFERENCES pins(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
);
''')

print("Tables created successfully!")

# Close connection
conn.close()
