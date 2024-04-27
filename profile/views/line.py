import flet as ft


class LinePage(ft.View):
    def __init__(self, appbar: ft.AppBar) -> None:
        super().__init__(route="/settings", padding=60)

        self.appbar = appbar

        self.build()

    def build(self) -> None:
        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(value="Post 1"),
                        ft.Text(value="Post 2"),
                        ft.Text(value="Post 3"),
                    ],
                ),
            )
        ]
