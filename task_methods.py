from create_db import create_connection
from datetime import datetime, timezone, timedelta

def create_task(description):
    """Добавляет новую задачу с текущим временем в UTC+4"""

    # Настройка таймзоны UTC+4
    UTC_PLUS_4 = timezone(timedelta(hours=4))

    conn = create_connection()
    if not conn:
        return

    try:
        # Получаем текущее время с UTC+4
        current_time = datetime.now(UTC_PLUS_4).strftime('%Y-%m-%d %H:%M:%S')

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Tasks (description, created_date) VALUES (?, ?)",
            (description, current_time)
        )
        conn.commit()
        print(f"✅ Задача добавлена: '{description}'")
    except Exception as e:
        print(f"❌ Ошибка при добавлении задачи: {e}")
    finally:
        conn.close()

def delete_task(task_id):
    """Удаляет выбранную задачу"""

    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        print(f"✅ Задача удалена")

def update_task(task_id, new_description):
    """Изменяет выбранную задачу"""

    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Tasks set description = ? WHERE id = ?", (new_description,task_id,))
        conn.commit()
        conn.close()
        print(f"✅ Задача изменена")


def mark_as_done(task_id):
    """Помечает задачу как выполненную"""

    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Tasks set is_done = ? WHERE id = ?", (True, task_id,))
        conn.commit()
        conn.close()
        print(f"✅ Задача выполнена")


def get_all_tasks():
    """Возвращает список всех задач"""

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Tasks")
    tasks = cursor.fetchall()

    conn.close()

    return tasks

def get_task_by_id(task_id):
    """Возвращает конкретную задачу"""

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()

    conn.close()

    return task

if __name__ == "__main__":

    result = get_all_tasks()
    print(result)