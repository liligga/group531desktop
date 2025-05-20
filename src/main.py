import flet as ft

from database import Database


def main(page: ft.Page):
    page.title = "Приложение для списка дел"
    page.window.width = 1024
    # data - свойство объекта page, которое может хранить любые данные
    # которые будут использоваться в любом месте прилижения, работает как глобальная переменная
    # page.data = 0  # счетчик задач

    # создаем экземпляр класса Database
    db = Database("db.sqlite3")
    # создаем таблицы
    db.create_tables()

    todos = db.all_todos()
    print(todos)

    def get_rows() -> list[ft.Row]:
        rows = []
        for todo in db.all_todos():
            # проходим по списку задач и добавляем каждую в todo_list_area
            # так как Column может в себя вмещать другие элементы, свойство controls как раз служит списком элементов, добавляемых в Column
            rows.append(
                ft.Row(
                    controls=[
                        ft.Text(value=todo[0]),
                        ft.Text(value=f"Задача: {todo[1]}", size=30),
                        ft.Text(
                            value=f"Категория: {todo[2]}", size=30, color=ft.Colors.BLUE
                        ),
                        ft.IconButton(
                            icon=ft.Icons.EDIT,
                            icon_color=ft.Colors.GREEN,
                            icon_size=20,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            icon_color=ft.Colors.RED,
                            icon_size=20,
                            on_click=delete_todo,
                            data=todo[0],
                        ),
                    ]
                )
            )
        return rows

    # функция, которая будет вызываться при нажатии на кнопку "Добавить"
    def add_todo(e):
        # Добавляем задачу в БД
        db.add_todo(task=task_input.value, category=category_input.value)

        todo_list_area.controls = get_rows()

        # очищаем поля
        task_input.value = ""
        category_input.value = ""
        todo_count_text.value = f"Всего {db.count_todos()} задач(а)"

        # обновляем страницу, чтобы отобразить изменения
        page.update()  # эта строка обязательна

    def delete_todo(e):
        print(f"В delete_todo нажали на todo с id={e.control.data}")
        db.delete_todo(todo_id=e.control.data)
        todo_list_area.controls = get_rows()
        todo_count_text.value = f"Всего {db.count_todos()} задач(а)"
        page.update()

    # создаем элементы интерфейса
    title = ft.Text(value="Список дел", size=33)
    task_input = ft.TextField(label="Введите задачу")
    category_input = ft.TextField(label="Введите категорию")
    add_button = ft.ElevatedButton("Добавить", on_click=add_todo)
    todo_count_text = ft.Text(
        value=f"Всего {db.count_todos()} задач(а)", size=28, color=ft.Colors.PINK
    )
    # это место, куда будут добавляться задачи в виде Text
    todo_list_area = ft.Column(controls=get_rows(), scroll="auto", expand=True)
    # создаем форму в виде строки и добавляем в нее поля и кнопку
    form_area = ft.Row(controls=[task_input, category_input, add_button])
    title.value = "Приложение для списка дел"

    # добавляем элементы на страницу, порядок важен
    page.add(
        title,
        form_area,
        todo_count_text,
        todo_list_area,
    )  # от того, в каком порядке они тут добавляются, зависит в каком порядке они отображаются


ft.app(main)
