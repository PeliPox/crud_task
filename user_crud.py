from db import get_connection


def create_user(name: str, email: str) -> int:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;",
        (name, email)
    )

    user_id = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()

    return user_id


def get_users():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, email FROM users")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


def update_user(user_id: int, new_name: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("UPDATE users SET name = %s WHERE id = %s",
                (new_name, user_id))

    conn.commit()
    cur.close()
    conn.close()


def delete_user(user_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE id = %s", (user_id, ))

    conn.commit()
    cur.close()
    conn.close()

