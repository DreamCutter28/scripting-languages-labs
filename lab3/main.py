import os
import sqlite3
import requests

# Получаем путь к директории скрипта (иначе VSCode создает в корне...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'blog.db')


def create_database():
    """Создание базы данных и таблицы posts"""
    # Инициализируем переменную перед try
    conn = None

    try:
        # Проверяем, существует ли база данных
        if os.path.exists(DB_PATH):
            print("База данных уже существует")
            return

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                title TEXT,
                body TEXT
            )
        ''')

        conn.commit()
        print("База данных успешно создана")

    except sqlite3.Error as error:
        print("Ошибка при создании базы данных:", error)
    finally:
        if conn:
            conn.close()


def fetch_posts():
    """Получение данных с тестового сервера"""
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        print("Ошибка при получении данных:", error)
        return None


def save_posts(posts):
    """Сохранение постов в базу данных"""
    if not posts:
        return

    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.executemany(
            'INSERT OR REPLACE INTO posts (id, user_id, title, body) VALUES (?, ?, ?, ?)',
            [(post['id'], post['userId'], post['title'], post['body'])
             for post in posts]
        )

        conn.commit()
        print(f"Успешно сохранено {len(posts)} постов")

    except sqlite3.Error as error:
        print("Ошибка при сохранении данных:", error)
    finally:
        if conn:
            conn.close()


def get_user_posts(user_id):
    """Получение всех постов конкретного пользователя"""
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM posts WHERE user_id = ?', (user_id,))
        posts = cursor.fetchall()

        return posts

    except sqlite3.Error as error:
        print("Ошибка при получении постов пользователя:", error)
        return []
    finally:
        if conn:
            conn.close()


def main():
    create_database()
    posts = fetch_posts()
    if posts:
        save_posts(posts)

    # Пример получения постов пользователя
    user_id = 1
    user_posts = get_user_posts(user_id)
    print(f"\nПосты пользователя {user_id}:")
    for post in user_posts:
        print(f"ID: {post[0]}")
        print(f"Заголовок: {post[2]}")
        # Выводим только первые 100 символов
        print(f"Текст: {post[3][:100]}...")
        print("-" * 50)


if __name__ == "__main__":
    main()
