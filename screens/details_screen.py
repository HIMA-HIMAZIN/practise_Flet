import flet as ft

def details_screen(page: ft.Page, todo, show_home_screen):
    page.controls.clear()
    page.controls.append(
        ft.Column(
            [
                ft.Text("Todo詳細", style=ft.TextThemeStyle.HEADLINE_SMALL),
                ft.Text(f"タイトル: {todo.title}"),
                ft.Text(f"詳細内容: {todo.details}"),
                ft.Text(f"登録日時: {todo.created_at}"),
                ft.ElevatedButton("戻る", on_click=lambda _: show_home_screen()),
            ],
            expand=True,
            spacing=10,
        )
    )
    page.update()
