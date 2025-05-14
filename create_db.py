import sqlite3

def create_connection(db_file="tasks.db"):
    """Создает подключение к SQLite базе данных"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Подключение к SQLite DB успешно: {db_file}")
        return conn
    except sqlite3.Error as e:
        print(f"Ошибка подключения: {e}")
    return conn

def create_tasks_table(conn):
    """Создает таблицу Tasks, если её нет"""
    sql = """
    CREATE TABLE IF NOT EXISTS Tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        created_date TEXT DEFAULT CURRENT_TIMESTAMP,
        is_done BOOLEAN DEFAULT FALSE
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        print("✅ Таблица Tasks создана (или уже существует)")
    except sqlite3.Error as e:
        print(f"❌ Ошибка при создании таблицы: {e}")

def initialize_database():
    """Инициализирует БД и таблицу (вызывается 1 раз)"""
    conn = create_connection()
    if conn:
        create_tasks_table(conn)
        conn.close()

if __name__ == "__main__":
    initialize_database()