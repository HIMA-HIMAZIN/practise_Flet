import flet as ft
from models.todo import Todo
from screens.home_screen import home_screen
from screens.add_todo_screen import add_todo_screen
from screens.details_screen import details_screen

def main(page: ft.Page):
    page.title = "Todoアプリ"
    page.theme_mode = ft.ThemeMode.LIGHT

    todos = []

    # 各画面への遷移
    def show_home_screen():
        page.controls.clear()  # ページをクリアして再描画
        home_screen(page, todos, show_add_todo_screen, show_details_screen)
        page.update()

    def show_add_todo_screen():
        page.controls.clear()  # ページをクリアして再描画
        add_todo_screen(page, todos, show_home_screen)
        page.update()

    def show_details_screen(index):
        page.controls.clear()  # ページをクリアして再描画
        details_screen(page, todos[index], show_home_screen)
        page.update()

    # 初期画面を表示
    show_home_screen()

ft.app(target=main)
