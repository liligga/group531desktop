import flet as ft

from database import Database


def main(page: ft.Page):
    page.title = "Приложение для списка дел"
    # data - свойство объекта page, которое может хранить любые данные
    # которые будут использоваться в любом месте прилижения, работает как глобальная переменная
    page.data = 0  # счетчик задач

    # создаем экземпляр класса Database
    db = Database("db.sqlite3")
    # создаем таблицы
    db.create_tables()

    todos = db.all_todos()
    print(todos)

    # функция, которая будет вызываться при нажатии на кнопку "Добавить"
    def add_todo(e):
        # Добавляем задачу в БД
        db.add_todo(task=task_input.value, category=category_input.value)

        # очищаем Column
        todo_list_area.controls.clear()
        # получаем все задачи из БД
        todos = db.all_todos()
        for todo in todos:
            # проходим по списку задач и добавляем каждую в todo_list_area
            # так как Column может в себя вмещать другие элементы, свойство controls как раз служит списком элементов, добавляемых в Column
            todo_list_area.controls.append(
                ft.Row(
                    controls=[
                        ft.Text(value=f"Задача: {todo[1]}", size=30),
                        ft.Text(value=f"Категория: {todo[2]}", size=30),
                    ]
                )
            )
            # тут увеличиваем счетчик количества задач
            page.data += 1

        # очищаем поля
        task_input.value = ""
        category_input.value = ""
        todo_count_text.value = f"Всего {page.data} задач(а)"

        # обновляем страницу, чтобы отобразить изменения
        page.update()  # эта строка обязательна

    # создаем элементы интерфейса
    title = ft.Text(value="Список дел", size=33)
    task_input = ft.TextField(label="Введите задачу")
    category_input = ft.TextField(label="Введите категорию")
    add_button = ft.ElevatedButton("Добавить", on_click=add_todo)
    todo_count_text = ft.Text(value=f"Всего {page.data} задач(а)", size=28)
    # это место, куда будут добавляться задачи в виде Text
    todo_list_area = ft.Column()
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
