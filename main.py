import flet as ft
from models.todo import Todo
from screens.home_screen import home_screen
from screens.add_todo_screen import add_todo_screen
from screens.details_screen import details_screen
from screens.edit_todo_screen import edit_todo_screen

def main(page: ft.Page):
    page.title = "Todoアプリ"
    page.theme_mode = ft.ThemeMode.LIGHT

    todos = []

    def show_home_screen():
        home_screen(page, todos, show_add_todo_screen, show_details_screen, toggle_todo_status, edit_todo, delete_todo)

    def show_add_todo_screen():
        add_todo_screen(page, todos, show_home_screen)

    def show_details_screen(index):
        details_screen(page, todos[index], toggle_todo_status, show_home_screen)

    def toggle_todo_status(todo):
        todo.status = not todo.status

    def edit_todo(index):
        todos[index].title = "編集されたタイトル"  # サンプル編集
        show_home_screen()

    def delete_todo(index):
        todos.pop(index)
        show_home_screen()

    def edit_todo(index):
        def update_todo():
            todos[index] = todos[index]
        edit_todo_screen(page, todos[index], update_todo, show_home_screen)


    show_home_screen()

ft.app(target=main)
