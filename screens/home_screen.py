import flet as ft
from constants import COLORS, FONT_STYLE


def home_screen(page: ft.Page, todos, show_add_todo_screen, show_details_screen, update_todo_status, edit_todo, delete_todo):
    filter_status = 0  # 0: All, 1: Completed, 2: Incomplete

    def update_todo_list():
        todo_list.controls.clear()
        # フィルタリングに基づきTodoリストを更新
        filtered_todos = todos if filter_status == 0 else [t for t in todos if t.status == (filter_status == 1)]
        for i, todo in enumerate(filtered_todos):
            # Todo項目を横並びに表示
            todo_list.controls.append(
                ft.Container(
                    content=ft.Row(  # 横並びにするためRowを使用
                        [
                            ft.Text(todo.title, **FONT_STYLE["subtitle"], expand=True),  # タイトルを左揃え
                            ft.Text("達成済み" if todo.status else "未達成", color=COLORS["yellow"], size=12),  # 状態表示
                            ft.IconButton(
                                icon=ft.icons.EDIT, icon_color=COLORS["blue"], tooltip="編集",
                                on_click=lambda e, idx=i: open_edit_dialog(idx)
                            ),  # 編集ボタン
                            ft.IconButton(
                                icon=ft.icons.DELETE, icon_color=COLORS["red"], tooltip="削除",
                                on_click=lambda e, idx=i: delete_todo(idx)
                            ),  # 削除ボタン
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # アイテム間のスペースを均等に配置
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,  # 縦中央揃え
                    ),
                    padding=ft.padding.symmetric(vertical=5),  # 項目の上下余白
                    bgcolor=COLORS["light_gray"],  # 背景色
                    border_radius=ft.border_radius.all(8),  # 角丸デザイン
                )
            )
        todo_list.update()

    def open_edit_dialog(index):
        # 編集ダイアログ
        title_input = ft.TextField(label="タイトルを編集", value=todos[index].title)
        details_input = ft.TextField(label="詳細内容を編集", value=todos[index].details, multiline=True)

        def save_changes(_):
            # 保存ボタンの動作
            todos[index].title = title_input.value  # タイトルを更新
            todos[index].details = details_input.value  # 詳細を更新
            page.dialog.open = False  # モーダルを閉じる
            page.update()  # モーダルを閉じた画面を更新
            update_todo_list()  # 変更箇所をリストに反映

        def cancel_changes(_):
            # キャンセルボタンの動作
            page.dialog.open = False  # モーダルを閉じる
            page.update()  # 元の画面を更新

        page.dialog = ft.AlertDialog(
            title=ft.Text("Todo編集", **FONT_STYLE["headline"]),
            content=ft.Column([title_input, details_input]),
            actions=[
                ft.ElevatedButton("保存", on_click=save_changes, bgcolor=COLORS["green"], color=COLORS["white"]),
                ft.ElevatedButton("キャンセル", on_click=cancel_changes, bgcolor=COLORS["red"], color=COLORS["white"]),
            ],
        )
        page.dialog.open = True  # モーダルを開く
        page.update()

    def on_tab_change(e):
        # フィルタタブの変更イベント
        nonlocal filter_status
        filter_status = e.control.selected_index
        update_todo_list()

    todo_list = ft.Column()  # Todoリストを格納するコンテナ

    # Todo追加ボタン
    add_todo_button = ft.ElevatedButton(
        "Todo登録",
        on_click=lambda _: show_add_todo_screen(),
        bgcolor=COLORS["blue"],
        color=COLORS["white"],
    )

    # メイン画面のレイアウト
    page.controls.clear()
    page.controls.append(
        ft.Column(
            [
                ft.Text("Todo一覧", **FONT_STYLE["headline"]),  # ヘッダーテキスト
                ft.Tabs(
                    selected_index=0,
                    tabs=[
                        ft.Tab(text="すべて"),  # フィルタタブ：すべて
                        ft.Tab(text="達成"),   # フィルタタブ：達成
                        ft.Tab(text="未達成"), # フィルタタブ：未達成
                    ],
                    on_change=on_tab_change,  # タブ変更時の処理
                ),
                ft.Container(content=todo_list, expand=True),  # Todoリストの表示領域
                ft.Container(content=add_todo_button, alignment=ft.alignment.center, padding=ft.padding.only(top=20)),
            ],
            expand=True,
            spacing=20,  # 各コンポーネント間のスペース
        )
    )
    page.update()
    update_todo_list()  # 初期表示の更新
