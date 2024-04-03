import flet as ft
from home_page import ProfilePage

from localizer import localize


class LandingPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/landing", padding=60)

        self.page = page

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
                                    text=localize("{{ go2profile }}"),
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

    def view_pop(e: ft.ViewPopEvent) -> None:
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = router
    page.on_view_pop = view_pop
    page.go("/landing")
