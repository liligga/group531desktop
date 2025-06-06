import sqlite3


# CRUD - Create, Read, Update, Delete


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
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    category TEXT
                )
            """)

    def count_todos(self):
        """
        Метод, в котором вызывается запрос для получения количества задач из БД
        """
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            result = cursor.execute("SELECT COUNT(*) FROM todos")
            # (0)
            return result.fetchone()[0]

    def all_todos(self):
        """
        Метод, в котором вызывается запрос для получения всех задач из БД
        """

        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            result = cursor.execute("SELECT * FROM todos")
            return result.fetchall()

    def get_todo(self, todo_id):
        """
        Метод, в котором вызывается запрос для получения конкретной задачи из БД
        """
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            result = cursor.execute("SELECT * FROM todos WHERE id=(?)", (todo_id,))
            # (1, 'cook meal', 'home')
            return result.fetchone()

    def add_todo(self, task: str, category: str):
        """
        Метод, в котором вызывается запрос для добавления в БД новой задачи
        """

        print(task, category, "in database add_todo")
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO todos (task, category) VALUES
                (?, ?)
                """,
                (task, category),
            )
            # так делать неправильно:
            # conn.execute(
            #     f"INSERT INTO todos (task, category) VALUES ({task}, {category})",
            # )
            conn.commit()

    def update_todo(self, todo_id: int, task: str, category: str):
        """
        Метод, в котором вызывается запрос для обновления задачи
        """
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                UPDATE todos SET task = ?, category = ? WHERE
                id = ?
                """,
                (task, category, todo_id),
            )

    def delete_todo(self, todo_id):
        """
        Метод, в котором вызывается запрос для удаления задачи
        """
        with sqlite3.connect(self.path) as conn:
            conn.execute("DELETE FROM todos WHERE id=(?)", (todo_id,))
