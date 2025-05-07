import flet as ft


def main(page: ft.Page):
    page.title = "Приложение для списка дел"

    title = ft.Text(value="Привет мир!", size=30)
    name_input = ft.TextField(label="Введите имя")
    button = ft.ElevatedButton("Добавить")

    page.add(title, name_input, button)


ft.app(main)
