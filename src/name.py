"""модуль с примером про ввод имени"""

import flet as ft


def main(page: ft.Page):
    page.title = "Приложение для списка дел"

    def change_name(e):
        # print("привет", name_input.value)
        if name_input.value:
            title.value = f"Привет, {name_input.value}"
            name_input.value = ""
        else:
            title.value = "Привет, мир"

        page.update()

    title = ft.Text(value="Привет, мир", size=30)
    name_input = ft.TextField(label="Введите имя")
    button = ft.ElevatedButton("Добавить", on_click=change_name)

    page.add(
        title,
        name_input,
        button,
    )


ft.app(main)
