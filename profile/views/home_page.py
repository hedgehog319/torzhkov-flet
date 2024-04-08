import flet as ft
from flet_runtime.app import random_string

from localizer import localize


class ProfilePage(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(route="/profile", padding=20)

        self.page = page

        self.build()

    def build(self) -> None:
        description = ft.TextField(
            value=localize("{{ profile_description }}"),
            label=localize("{{ profile_description_label }}"),
            read_only=True,
        )

        def rand_desc(_: ft.TapEvent) -> None:
            description.value = random_string(100)
            description.update()

        self.controls = [
            ft.Container(
                expand=True,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Divider(height=1, color="transparent"),
                                ft.Dropdown(
                                    icon="icons.LANGUAGE",
                                    on_change=self.change_lang,
                                    options=[
                                        ft.dropdown.Option(locale)
                                        for locale in localize._available_locales
                                    ],
                                    value=localize.locale,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Divider(height=20, color="transparent"),
                        ft.Container(
                            bgcolor="white10",
                            width=128,
                            height=128,
                            shape=ft.BoxShape("circle"),
                            # Define image for profile picture
                            image_src="./hedgehog.jpg",
                            image_fit=ft.ImageFit.COVER,
                            shadow=ft.BoxShadow(
                                spread_radius=6,
                                blur_radius=20,
                                color=ft.colors.with_opacity(0.71, "black"),
                            ),
                        ),
                        ft.Divider(height=10, color="transparent"),
                        ft.Text(localize("Hedgehog319"), size=32),
                        ft.Divider(height=50, color="transparent"),
                        ft.Column(
                            spacing=20,
                            controls=[
                                description,
                                ft.OutlinedButton(
                                    text=localize("{{ rnd_button }}"),
                                    on_click=rand_desc,
                                ),
                            ],
                        ),
                    ],
                ),
            )
        ]

    def change_lang(self, event: ft.ControlEvent) -> None:
        localize.set_locale(event.data)
        self.build()
        self.update()
