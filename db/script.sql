CREATE TABLE IF NOT EXISTS Cards (
cardId INTEGER PRIMARY KEY,
name TEXT NOT NULL,
description TEXT,
type TEXT,
imgURL TEXT
);

CREATE TABLE IF NOT EXISTS users(
    userid INTEGER PRIMARY KEY, --primary key for users
    username TEXT NOT NULL, -- username column for storing usernames
    pword TEXT NOT NULL, -- password column for storing passwords
    email TEXT NOT NULL, -- email for user
    bio TEXT NOT NULL,
    pfp TEXT NOT NULL
);
------------------
