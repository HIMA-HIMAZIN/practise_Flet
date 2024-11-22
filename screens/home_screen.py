import flet as ft
from models.todo import Todo

def home_screen(page: ft.Page, todos: list, show_add_todo_screen, show_details_screen):
    def update_todo_list():
        todo_list.controls.clear()
        for i, todo in enumerate(todos):
            todo_list.controls.append(
                ft.ListTile(
                    title=ft.Text(todo.title),
                    on_click=lambda e, idx=i: show_details_screen(idx),
                )
            )
        todo_list.update()

    todo_list = ft.Column()
    add_todo_button = ft.ElevatedButton("Todo登録", on_click=lambda _: show_add_todo_screen())

    # 中央配置を設定
    page.controls.clear()
    page.controls.append(
        ft.Column(
            [
                ft.Container(
                    content=ft.Text("Todo一覧", style=ft.TextThemeStyle.HEADLINE_SMALL),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    content=add_todo_button,
                    alignment=ft.alignment.center,  # ボタンを中央に配置
                    padding=ft.padding.only(top=20),
                ),
                ft.Container(
                    content=todo_list,
                    alignment=ft.alignment.center_left,  # Todoリストは左寄せ
                    expand=True,
                ),
            ],
            expand=True,
            spacing=20,
        )
    )

    # ページに`todo_list`が追加された後に更新処理を呼び出す
    page.update()  # ここでページ全体を描画
    update_todo_list()  # 更新処理を呼び出す
