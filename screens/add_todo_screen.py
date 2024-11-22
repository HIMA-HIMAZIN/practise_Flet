import flet as ft
from models.todo import Todo

def add_todo_screen(page: ft.Page, todos: list, show_home_screen):
    title_input = ft.TextField(label="タイトルを入力", expand=True)
    details_input = ft.TextField(label="詳細内容を入力", expand=True, multiline=True, height=150)

    def save_todo(e):
        if not title_input.value.strip() or not details_input.value.strip():
            page.snack_bar = ft.SnackBar(ft.Text("タイトルと詳細内容は必須です！"))
            page.snack_bar.open = True
            page.update()
            return
        todos.append(
            Todo(
                title=title_input.value.strip(),
                details=details_input.value.strip(),
            )
        )
        show_home_screen()

    page.controls.clear()
    page.controls.append(
        ft.Column(
            [
                ft.Text("Todo登録", style=ft.TextThemeStyle.HEADLINE_SMALL),
                title_input,
                details_input,
                ft.Row(
                    [
                        ft.ElevatedButton("保存", on_click=save_todo),
                        ft.ElevatedButton("キャンセル", on_click=lambda _: show_home_screen()),
                    ],
                    spacing=10,
                ),
            ],
            expand=True,
            spacing=10,
        )
    )
    page.update()
