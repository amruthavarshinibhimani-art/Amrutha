import sqlite3


DATABASE = "events.db"


def create_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT,
            event_type TEXT,
            event_date TEXT,
            guests INTEGER,
            budget REAL,
            venue TEXT,
            preferences TEXT
        )
    """)

    connection.commit()

    connection.close()


def save_event(
    event_name,
    event_type,
    event_date,
    guests,
    budget,
    venue,
    preferences
):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO events
        (
            event_name,
            event_type,
            event_date,
            guests,
            budget,
            venue,
            preferences
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        event_name,
        event_type,
        event_date,
        guests,
        budget,
        venue,
        preferences
    ))

    connection.commit()

    connection.close()