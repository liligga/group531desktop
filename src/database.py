import sqlite3


class Database:
    """
    Класс для работы с БД. тут будут методы для создания таблиц,
    для добавления, обновления и удаления задач(таблица todos)
    """

    def __init__(self, path):
        self.path = path

    def create_tables(self):
        """
        Метод, в котором описывается, какие таблицы и с какими колонками создаются для приложения
        """
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY,
                    task TEXT NOT NULL,
                    category TEXT
                )
            """)

    def add_todo(self):
        """
        Метод, в котором вызывается запрос для добавления новой задачи
        """
        pass

    def delete_todo(self):
        """
        Метод, в котором вызывается запрос для удаления задачи
        """
        pass
