import flet as ft


def main(page: ft.Page):
    page.title = "Приложение для списка дел"
    page.data = 0  # счетчик задач, так сказать глобальная переменная

    # функция, которая будет вызываться при нажатии на кнопку "Добавить"
    def add_todo(e):
        # создаем строку с задачей
        todo = f"{task_input.value}, категория: {category_input.value}"
        print(todo)
        # добавляем задачу в список
        todo_list_area.controls.append(ft.Text(value=todo, size=30))

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

    # добавляем элементы на страницу, порядок важен
    page.add(
        title,
        task_input,
        category_input,
        add_button,
        todo_count_text,
        todo_list_area,
    )


ft.app(main)
