import flet as ft
from constants import COLORS, FONT_STYLE


def details_screen(page: ft.Page, todo, toggle_status, show_home_screen):
    def toggle():
        toggle_status(todo)
        show_home_screen()

    page.controls.clear()
    page.controls.append(
        ft.Column(
            [
                ft.Text("Todo詳細", **FONT_STYLE["headline"]),
                ft.Text(f"タイトル: {todo.title}", **FONT_STYLE["body"]),
                ft.Text(f"詳細内容: {todo.details}", **FONT_STYLE["body"]),
                ft.Text(f"登録日時: {todo.created_at}", **FONT_STYLE["body"]),
                ft.Text(f"ステータス: {'達成済み' if todo.status else '未達成'}", color=COLORS["yellow"]),
                ft.ElevatedButton("ステータス切替", on_click=lambda _: toggle(), bgcolor=COLORS["green"], color=COLORS["white"]),
                ft.ElevatedButton("戻る", on_click=lambda _: show_home_screen(), bgcolor=COLORS["blue"], color=COLORS["white"]),
            ],
            expand=True,
            spacing=10,
        )
    )
    page.update()
