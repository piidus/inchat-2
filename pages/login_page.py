import flet as ft

class LoginPage:
    def __init__(self, page: ft.Page, **kwargs):
        self.page = page
        self.some_value = kwargs.get("some_value", "Default Value")
        self.ip_address = kwargs.get("ip_address", "No IP Address Provided")
        self.name_field = ft.TextField(label="Enter your name", width=300)
        self.error_message = ft.Text("", color=ft.colors.RED)  # Placeholder for error messages

    def build(self):
        return ft.Column(
            controls=[
                ft.Text(f"Login Page, some_value: {self.some_value}, IP Address: {self.ip_address}"),
                self.name_field,
                self.error_message,
                ft.ElevatedButton(text="Join chat", on_click=self.join_chat_click),
            ],
            expand=True
        )

    def join_chat_click(self, e):
        user_name = self.name_field.value
        if not user_name:
            self.error_message.value = "Please enter your name to join the chat."
            self.page.update()
            return
        
        self.page.session.set("user_name", user_name)
        self.error_message.value = "Username set to: " + user_name  # Clear any previous error message
        self.page.update()
        try:
            # Navigate to ChatPage
            self.page.go("/chat_page")
            print("Navigated to ChatPage")
        except Exception as e:
            self.page.add(ft.Text(f"Error in navigation: {e}"))
            self.page.update()
