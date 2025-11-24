from db import get_connection

ALLOWED_STATUSES = ["todo", "in_progress", "done"]

def validate_task(title: str, status: str):
    if not isinstance(title, str):
        raise ValueError("Title должен быть string.")

    title = title.strip()
    if not title:
        raise ValueError("Title не может быть пустым.")
    if len(title) > 200:
        raise ValueError("Title не может быть такой длинный.")

    if status not in ALLOWED_STATUSES:
        raise ValueError(f'Status должен быть один из {ALLOWED_STATUSES}')

    return title, status


def create_task(title: str, description: str, status: str, user_id: int) -> int:
    title, status = validate_task(title, status)
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO tasks (title, description, status, user_id) VALUES (%s, %s, %s, %s) RETURNING id;",
        (title, description, status, user_id)
    )
    task_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()
    return task_id


def get_all_tasks():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT title, description, status, user_id from tasks ")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows


def update_task(task_id: int, title: str, description: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("UPDATE tasks SET title = %s, description = %s WHERE id = %s;",
                (title, description, task_id))

    conn.commit()
    cur.close()
    conn.close()


def delete_task(task_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM tasks WHERE id = %s;", (task_id, ))

    conn.commit()
    cur.close()
    conn.close()

