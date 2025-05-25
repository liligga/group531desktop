import flet as ft

from database import Database


def main(page: ft.Page):
    page.title = "Приложение для списка дел"
    page.window.width = 1024
    # data - свойство объекта page, которое может хранить любые данные
    # которые будут использоваться в любом месте прилижения, работает как глобальная переменная
    page.data = 0  # id задачи

    # создаем экземпляр класса Database
    db = Database("db.sqlite3")
    # создаем таблицы
    db.create_tables()

    def get_rows() -> list[ft.Row]:
        """
        Функция возвращает список Row, которые будут отображаться в todo_list_area
        """
        rows = []
        for todo in db.all_todos():
            # проходим по списку задач и добавляем каждую в todo_list_area
            # так как Column/Row может в себя вмещать другие элементы, свойство controls как раз служит списком элементов, добавляемых в Column/Row
            rows.append(
                ft.Row(
                    controls=[
                        ft.Text(value=todo[0], size=30),
                        ft.Text(value=f"Задача: {todo[1]}", size=30),
                        ft.Text(
                            value=f"Категория: {todo[2]}", size=30, color=ft.Colors.BLUE
                        ),
                        ft.IconButton(
                            icon=ft.Icons.EDIT_NOTE,
                            icon_color=ft.Colors.GREEN,
                            icon_size=20,
                            on_click=open_edit_modal,
                            data=todo[0],
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

    def add_todo(e):
        """
        Функция, которая будет вызываться при нажатии на кнопку 'Добавить'
        """
        # Добавляем задачу в БД
        db.add_todo(task=task_input.value, category=category_input.value)

        # обновляем список задач
        todo_list_area.controls = get_rows()

        # очищаем поля
        task_input.value = ""
        category_input.value = ""
        todo_count_text.value = f"Всего {db.count_todos()} задач(а)"

        # обновляем страницу, чтобы отобразить изменения
        page.update()  # эта строка обязательна

    def delete_todo(e):
        """
        Функция, которая будет вызываться при нажатии на кнопку 'Удалить'
        """
        print(f"В delete_todo нажали на todo с id={e.control.data}")

        # удаляем задачу из БД
        db.delete_todo(todo_id=e.control.data)

        # обновляем список задач
        todo_list_area.controls = get_rows()

        # обновляем количество задач
        todo_count_text.value = f"Всего {db.count_todos()} задач(а)"

        # обновляем страницу
        page.update()

    def open_edit_modal(e):
        """
        Функция, которая будет вызываться при нажатии на кнопку 'Редактировать'
        и открывать модальное окно
        """
        print(f"В open_edit_modal нажали на todo с id={e.control.data}")

        # запоминаем id задачи
        page.data = e.control.data
        # получаем задачу из БД
        todo = db.get_todo(todo_id=e.control.data)

        # заполняем поля данными из БД
        task_input.value = todo[1]
        category_input.value = todo[2]

        # открываем модальное окно
        page.open(edit_modal)

    def close_edit_modal(e):
        """
        Функция, которая будет вызываться при нажатии на кнопку 'Отменить'
        и закрывать модальное окно
        """
        page.close(edit_modal)

    def update_todo(e):
        """
        Функция, которая будет вызываться при нажатии на кнопку 'Сохранить'
        в модальном окне и сохранять изменения в БД
        """
        # сохраняем изменения в БД
        db.update_todo(
            todo_id=page.data,
            task=task_input.value,
            category=category_input.value,
        )

        # обновляем список задач
        todo_list_area.controls = get_rows()

        # закрываем модальное окно
        page.close(edit_modal)

        # очищаем поля
        task_input.value = ""
        category_input.value = ""

        # обновляем страницу
        page.update()

    ##### создаем элементы интерфейса приложения #####
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

    # создаем модальное окно
    edit_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Хотите изменить задачу?"),
        # текстовые поля для редактирования задачи
        content=ft.Column(
            controls=[
                task_input,
                category_input,
            ]
        ),
        # кнопки
        actions=[
            ft.ElevatedButton(
                "Сохранить",
                on_click=update_todo,
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
            ),
            ft.ElevatedButton("Отменить", on_click=close_edit_modal),
        ],
    )
    ################################################

    # добавляем элементы на страницу, порядок важен
    page.add(
        title,
        form_area,
        todo_count_text,
        todo_list_area,
    )  # от того, в каком порядке они тут добавляются, зависит в каком порядке они отображаются


ft.app(main)
