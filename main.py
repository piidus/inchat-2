import flet as ft
from controllers.page_controller import route_change

def main(page: ft.Page):
    page.title = "InChat"
    page.window.width = 300
    page.on_route_change = route_change

    # Start on LoginPage or another default page
    page.go("/login_page")

ft.app(target=main)
