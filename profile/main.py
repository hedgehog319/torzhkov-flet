import flet as ft

from views.home_page import ProfilePage
from views.landing import LandingPage


def main(page: ft.Page):
    page.title = "Profile page"

    def route_change(_: ft.RouteChangeEvent):
        page.views.clear()

        # REDO: change to match
        if page.route == "/profile":
            page.views.append(ProfilePage(page))

        if page.route == "/landing":
            page.views.append(LandingPage())

        page.update()

    def view_pop(_: ft.ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/landing")


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
