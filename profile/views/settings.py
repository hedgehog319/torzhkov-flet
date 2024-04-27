import flet as ft

from typing import Literal
from localizer import localize


class SettingsPage(ft.View):
    def __init__(
        self,
        page: ft.Page,
        appbar: ft.AppBar,
        theme: Literal["light", "dark"] = "light",
    ):
        super().__init__(route="/settings", padding=60)

        self.appbar = appbar
        self.page = page
        self.theme = theme
        self.build()

    def build(self) -> None:
        self.theme_toggler = ft.IconButton(
            on_click=self.change_theme,
            icon="dark_mode",
            selected_icon="light_mode",
            style=ft.ButtonStyle(
                color={"": ft.colors.BLACK, "selected": ft.colors.WHITE}
            ),
        )

        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text(value=localize("{{ language }}") + ":"),
                                ft.Dropdown(
                                    icon="icons.LANGUAGE",
                                    on_change=self.change_lang,
                                    options=[
                                        ft.dropdown.Option(locale)
                                        for locale in localize._available_locales
                                    ],
                                    value=localize.locale,
                                ),
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.Text(value=localize("{{ theme }}") + ":"),
                                self.theme_toggler,
                            ]
                        ),
                    ],
                ),
            )
        ]

    def change_lang(self, event: ft.ControlEvent) -> None:
        localize.set_locale(event.data)
        self.build()
        self.update()

    def change_theme(self, event: ft.ControlEvent) -> None:
        if self.page is None:
            return

        self.page.theme_mode = (
            ft.ThemeMode.LIGHT
            if self.page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )

        self.theme_toggler.selected = not self.theme_toggler.selected

        self.page.update()
