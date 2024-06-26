import flet as ft

from localizer import localize


class LandingPage(ft.View):
    def __init__(self, appbar: ft.AppBar):
        super().__init__(route="/landing", padding=60)

        self.appbar = appbar

        # Define the list of controls for this view
        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Divider(height=120, color="transparent"),
                                ft.OutlinedButton(
                                    text=localize("{{ go2profile }}"),
                                    on_click=lambda e: e.page.go("/profile")
                                    if self.page
                                    else None,
                                ),
                            ],
                        ),
                    ],
                ),
            )
        ]
