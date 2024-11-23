import flet as ft
from constants import COLORS, FONT_STYLE

def edit_todo_screen(page: ft.Page, todo, update_todo, show_home_screen):
    title_input = ft.TextField(
        label="タイトルを編集",
        value=todo.title,
        expand=True,
        color=COLORS["black"],
        border_color=COLORS["dark_gray"],
    )
    details_input = ft.TextField(
        label="詳細内容を編集",
        value=todo.details,
        expand=True,
        multiline=True,
        height=150,
        color=COLORS["black"],
        border_color=COLORS["dark_gray"],
    )

    def save_changes(e):
        if not title_input.value.strip() or not details_input.value.strip():
            page.snack_bar = ft.SnackBar(
                ft.Text("タイトルと詳細内容は必須です！", color=COLORS["white"]),
                bgcolor=COLORS["red"],
            )
            page.snack_bar.open = True
            page.update()
            return
        todo.title = title_input.value.strip()
        todo.details = details_input.value.strip()
        update_todo()
        show_home_screen()

    page.controls.clear()
    page.controls.append(
        ft.Column(
            [
                ft.Text("Todo編集", **FONT_STYLE["headline"]),
                title_input,
                details_input,
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "保存", on_click=save_changes, bgcolor=COLORS["green"], color=COLORS["white"]
                        ),
                        ft.ElevatedButton(
                            "キャンセル", on_click=lambda _: show_home_screen(), bgcolor=COLORS["blue"], color=COLORS["white"]
                        ),
                    ],
                    spacing=10,
                ),
            ],
            expand=True,
            spacing=10,
        )
    )
    page.update()
