import flet as ft
from app import main

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
