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
        self.permission_handler = ft.PermissionHandler()
        self.page.add(self.permission_handler)
        self.error_message = ft.Text("", color=ft.colors.RED)  # Placeholder for error messages
    def check_permissions_after_build(self):
        
        print('[check_permissions_after_build]')
        try:
            # microphone_permission = self.permission_handler.check_permission(ft.PermissionType.MICROPHONE)
            # storage_permission =self.permission_handler.check_permission(ft.PermissionType.STORAGE)
            # print(microphone_permission, storage_permission)
            # Check permissions for storage and microphone
            storage_permission = self.permission_handler.check_permission(ft.PermissionType.STORAGE)
            microphone_permission = self.permission_handler.check_permission(ft.PermissionType.MICROPHONE)

            # Update the UI based on permission status
            self.storage_permission_text.current.value = "Granted" if storage_permission == ft.PermissionStatus.GRANTED else "Denied"
            self.microphone_permission_text.current.value = "Granted" if microphone_permission == ft.PermissionStatus.GRANTED else "Denied"
            
            # Enable or disable UI components based on permissions
            self.return_container.content.disabled = not (storage_permission == ft.PermissionStatus.GRANTED and microphone_permission == ft.PermissionStatus.GRANTED)
            
            # Ensure the changes are applied to the page
            self.page.update()
        except Exception as e:
            print(e)
        
    def will_unmount(self):
        print('[will_unmount]')
         # ft.PermissionType.MICROPHONE]))
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
        # Create refs for the text fields
        self.storage_permission_text = ft.Ref[ft.Text]()
        self.microphone_permission_text = ft.Ref[ft.Text]()

        # Create switches for microphone and storage permissions
        storage_switch = ft.Switch(
            scale=0.7, 
            active_color=ft.colors.DEEP_PURPLE_300, 
            inactive_track_color=ft.colors.AMBER_ACCENT_400, 
            on_change=self.switch_click
        )
        storage_switch.permission_type = ft.PermissionType.STORAGE

        microphone_switch = ft.Switch(
            scale=0.7, 
            active_color=ft.colors.DEEP_PURPLE_300, 
            inactive_track_color=ft.colors.AMBER_ACCENT_400, 
            on_change=self.switch_click
        )
        microphone_switch.permission_type = ft.PermissionType.MICROPHONE
        switch_height, switch_width = self.size_setter(height=50, width=70)
        return Container(
                border=ft.border.all(2, ft.colors.GREEN_ACCENT_700),
                border_radius=ft.border_radius.all(10),
                bgcolor="white",
                
                content=Column(
                    height=switch_height,
                    alignment=ft.MainAxisAlignment.CENTER,  # Align content vertically in the center
                    horizontal_alignment=ft.CrossAxisAlignment.START,  # Align content horizontally in the center
                    controls=[Row(controls=[storage_switch, Text(value="Storage"), 
                                            Text(ref=self.storage_permission_text, value="Denied")], ),
                            Row(controls=[microphone_switch, Text(value="Microphone"), 
                                            Text(ref=self.microphone_permission_text, value="Denied")], ), 
                            ]
                            )
        )
    
    def switch_click(self, e):
        # print(self.permission_handler.check_permissions([ft.PermissionType.STORAGE, ft.PermissionType.MICROPHONE]))
        if e.control.permission_type == ft.PermissionType.STORAGE:
            if e.control.value:
                self.storage_permission_text.current.value = "Granted"
                d = self.permission_handler.request_permission(ft.PermissionType.STORAGE)
                print("Storage permission granted")
                
            else:
                self.storage_permission_text.current.value = "Denied"
            
        elif e.control.permission_type == ft.PermissionType.MICROPHONE:
            if e.control.value:
                self.microphone_permission_text.current.value = "Granted"
            else:
                self.microphone_permission_text.current.value = "Denied"
            print("Microphone permission granted")
        print(e)
         # Check if both permissions are granted
        if self.storage_permission_text.current.value == "Granted" and self.microphone_permission_text.current.value == "Granted":
            self.return_container.content.disabled = False  # Enable the input field
        else:
            self.return_container.content.disabled = True  # Keep the input field disabled

        e.page.update()
    
    def user_name_text_field(self):
        self.text_box = ft.TextField(label="Enter your name", width=300, bgcolor='white')
        button = ft.ElevatedButton(text="Join Chat", on_click=self.join_chat_click)
        height, width = self.size_setter(30, 100)
        self.return_container = Container(
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
        # Call permission checking after build
        self.check_permissions_after_build()

        return self.return_container
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
            # self.will_unmount()
            print("Navigated to ChatPage")
        except Exception as e:
            self.page.add(ft.Text(f"Error in navigation: {e}"))
            self.page.update()
