import flet as ft

class AppMenu:
    def __init__(self, page: ft.Page, **kwargs):
        self.page = page

    def build(self):
        return ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.HOME, on_click=self.go_home),
                ft.IconButton(icon=ft.icons.CHAT, on_click=self.go_chat),
                ft.IconButton(icon=ft.icons.CONTACT_MAIL, on_click=self.go_contact),
            ]
        )

    def go_home(self, e):
        self.page.go("/login_page")

    def go_chat(self, e):
        self.page.go("/chat_page")

    def go_contact(self, e):
        self.page.go("/contact_page")
