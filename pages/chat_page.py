import flet as ft

class ChatPage:
    def __init__(self, page: ft.Page, **kwargs):
        self.page = page
        self.user_name = kwargs.get("user_name", "Guest")

    def build(self):
        return ft.Column(
            controls=[
                ft.Text(f"Welcome to Chat Page, {self.user_name}"),
                # Add chat-related controls here
            ]
        )
