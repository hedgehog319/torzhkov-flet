import flet as ft

from views.home_page import ProfilePage
from views.landing import LandingPage
from views.line import LinePage
from views.settings import SettingsPage


def main(page: ft.Page):
    page.title = "Profile page"
    appbar = ft.AppBar(
        title=ft.Text("Soshial", size=30),
        bgcolor="blue",
        actions=[
            ft.IconButton(
                on_click=lambda e: e.page.go("/settings"),
                icon=ft.icons.SETTINGS,
            ),
            ft.IconButton(
                on_click=lambda e: e.page.go("/line"),
                icon=ft.icons.CALENDAR_TODAY_OUTLINED,
            ),
        ],
    )

    def route_change(_: ft.RouteChangeEvent):
        page.views.clear()

        # REDO: change to match
        if page.route == "/profile":
            page.views.append(ProfilePage(page, appbar=appbar))

        if page.route == "/landing":
            page.views.append(LandingPage(appbar=appbar))

        if page.route == "/settings":
            page.views.append(SettingsPage(page, appbar=appbar))

        if page.route == "/line":
            page.views.append(LinePage(appbar=appbar))

        page.update()

    def view_pop(_: ft.ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/profile")


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
