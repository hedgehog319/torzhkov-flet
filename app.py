import flet as ft
from profile import Profile


class LandingPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/landing", padding=60)

        self.page = page

        # Define a button to route to profile
        self.button = ft.Container(
            border_radius=5,
            expand=True,
            bgcolor="#F4CE14",
            content=ft.Text("Check Linkage", color="black", size=18),
            padding=ft.padding.only(left=25, right=25, top=10, bottom=10),
            alignment=ft.alignment.center,
            on_click=None,
        )

        # Define the list of controls for this view
        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Divider(height=120, color="transparent"),
                                ft.OutlinedButton(
                                    text="Go to profile",
                                    on_click=lambda _: self.page.go("/profile")
                                    if self.page
                                    else None,
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                ),
            )
        ]


def main(page: ft.Page):
    # page.theme_mode = ft.ThemeMode.DARK

    def router(route):
        page.views.clear()

        if page.route == "/landing":
            landing = LandingPage(page)
            page.views.append(landing)

        if page.route == "/profile":
            profile = ProfilePage(page)
            page.views.append(profile)

        page.update()

    page.on_route_change = router
    page.go("/landing")
