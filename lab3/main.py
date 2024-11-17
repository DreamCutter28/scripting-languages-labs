import os
import sqlite3
import requests

# Получаем путь к директории скрипта (иначе VSCode создает в корне...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_database():
    """Создание базы данных и таблицы posts"""
    # Путь к файлу базы данных относительно скрипта
    db_path = os.path.join(BASE_DIR, 'blog.db')
    
    # Инициализируем переменную перед try
    conn = None
    
    try:
        # Проверяем, существует ли база данных
        if os.path.exists(db_path):
            print("База данных уже существует")
            return
            
        conn = sqlite3.connect(db_path)
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

if __name__ == "__main__":
    create_database()
    posts = fetch_posts()
    if posts:
        print(f"Успешно получено {len(posts)} постов")