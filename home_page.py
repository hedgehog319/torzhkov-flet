import flet as ft
from flet_runtime.app import random_string


class ProfilePage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/profile", padding=20)

        self.page = page

        def rand_desc(_: ft.TapEvent):
            description.value = random_string(100)
            description.update()

        description = ft.TextField(
            value="Some description",
            label="Description",
            read_only=True,
        )

        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
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
                        ft.Text("Hedgehog319", size=32),
                        ft.Divider(height=50, color="transparent"),
                        ft.Column(
                            spacing=20,
                            controls=[
                                description,
                                ft.OutlinedButton(
                                    text="Random description", on_click=rand_desc
                                ),
                            ],
                        ),
                    ],
                ),
            )
        ]
