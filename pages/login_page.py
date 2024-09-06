import flet as ft
from flet import TextField, Column, Switch, Container, Text, Row



class UserNameTextField(TextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = "Enter your name"
        self.width = 300
        self.bgcolor = 'white'

        # self.user_name = kwargs.get("user_name", "Guest")
   

class LoginPage:
    def __init__(self, page: ft.Page, **kwargs):
        self.page = page
        self.page.bgcolor = "#e6f7ff"
        self.some_value = kwargs.get("some_value", "Default Value")
        self.ip_address = kwargs.get("ip_address", "No IP Address Provided")
        self.name_field = ft.TextField(label="Enter your name", width=300, bgcolor='white')
        self.error_message = ft.Text("", color=ft.colors.RED)  # Placeholder for error messages

    def size_setter(self, height, width):
        new_height = self.page.window.height * height /100
        new_width = self.page.window.width * width /100
        return new_height, new_width 
    def build(self):
        # self.user_name_text_field = UserNamePart()
        main_colom_height, main_colom_width = self.size_setter(80, 80)
        return ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            border=ft.border.all(2, ft.colors.BLACK),
            border_radius=ft.border_radius.all(10),
            padding=ft.padding.all(10),
            content=Column(
                height=main_colom_height,
               controls=[
                   self.permission_container(),
                   self.user_name_text_field(),
               ]
                )

        )
    def permission_container(self):
        switch = Switch(scale=0.7, active_color=ft.colors.DEEP_PURPLE_300, 
                        inactive_track_color=ft.colors.AMBER_ACCENT_400, on_change=self.switch_click)
        switch_height, switch_width = self.size_setter(height=50, width=70)
        return Container(
                border=ft.border.all(2, ft.colors.GREEN_ACCENT_700),
                border_radius=ft.border_radius.all(10),
                bgcolor="white",
                
                content=Column(
                    height=switch_height,
                    alignment=ft.MainAxisAlignment.CENTER,  # Align content vertically in the center
                    horizontal_alignment=ft.CrossAxisAlignment.START,  # Align content horizontally in the center
                    controls=[Row(controls=[switch, Text(value="Storage"), Text("Granted")], ),
                            Row(controls=[switch, Text(value="Microphone"), Text("Granted")],)]
                    )
        )
    
    def switch_click(self, e):
        print(e)
    
    def user_name_text_field(self):
        self.text_box = ft.TextField(label="Enter your name", width=300, bgcolor='white')
        button = ft.ElevatedButton(text="Join Chat", on_click=self.join_chat_click)
        height, width = self.size_setter(30, 100)
        return Container(
            
            border=ft.border.all(2, ft.colors.GREEN_ACCENT_700),
            border_radius=ft.border_radius.all(10),
            height=height,
            bgcolor="white",
            padding=10,
            content=Column(
                disabled=True,
            
                alignment=ft.MainAxisAlignment.CENTER,  # Align content vertically in the center
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Align content horizontally in the center
                controls=[self.text_box, button, self.error_message],
            )
        )
    def join_chat_click(self, e):
        # print(e)
        user_name = self.text_box.value
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
