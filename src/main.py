import flet as ft


def main(page: ft.Page):
    page.title = "Приложение для списка дел"
    # data - свойство объекта page, которое может хранить любые данные
    # которые будут использоваться в любом месте прилижения, работает как глобальная переменная
    page.data = 0  # счетчик задач

    # функция, которая будет вызываться при нажатии на кнопку "Добавить"
    def add_todo(e):
        # создаем строку с задачей
        todo = f"{task_input.value}, категория: {category_input.value}"
        print(todo)
        # добавляем задачу в список
        # так как Column может в себя вмещать другие элементы, свойство controls как раз служит списком элементов, добавляемых в Column
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
    )  # от того, в каком порядке они тут добавляются, зависит в каком порядке они отображаются


ft.app(main)
