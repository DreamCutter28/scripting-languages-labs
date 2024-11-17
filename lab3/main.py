import os
import sqlite3

# Получаем путь к директории скрипта (иначе VSCode создает в корне...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_database():
    """Создание базы данных и таблицы posts"""
    # Путь к файлу базы данных относительно скрипта
    db_path = os.path.join(BASE_DIR, 'blog.db')
    
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

if __name__ == "__main__":
    create_database()