import sqlite3

DB_NAME = "db/usuarios.db"

def connect_to_database():
    """Connect to the SQLite database specified by db_name."""
    try:
        connection = sqlite3.connect(DB_NAME)
        print(f"Connected to database: {DB_NAME}")
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(connection):
    """Create the 'usuarios' table if it doesn't exist."""
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                edad INTEGER NOT NULL,
                calificacion REAL NOT NULL
            )
        ''')
        connection.commit()
        print("Table 'usuarios' created or already exists.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")