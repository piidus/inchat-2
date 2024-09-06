import flet as ft
from components.app_menu import AppMenu
from pages.login_page import LoginPage
from pages.chat_page import ChatPage
from pages.contact_page import ContactPage

page_list = {
    "/login_page": LoginPage,
    "/chat_page": ChatPage,
    "/contact_page": ContactPage
}
current_page_instance = None  # Global variable to keep track of the current page instance

def route_change(event: ft.RouteChangeEvent):
    global current_page_instance
    page = event.page
    route = event.route
    page.controls.clear()

    if current_page_instance:
        if hasattr(current_page_instance, 'will_unmount'):
            current_page_instance.will_unmount()
            # print("will_unmount called for", type(current_page_instance).__name__)
    if route in page_list:
        page_class = page_list[route]
        page_instance = page_class(page, user_name=page.session.get("user_name"))
        # Call did_mount for the new page instance
        if hasattr(page_instance, 'did_mount'):
            page_instance.did_mount()
        
        page.controls.append(page_instance.build())
        
        if route != "/login_page":  # Add menu to pages other than login
            menu = AppMenu(page)
            page.controls.append(menu.build())
        
        current_page_instance = page_instance
    else:
        page.controls.append(ft.Text("Page not found"))

    page.update()
