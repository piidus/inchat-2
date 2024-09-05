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

def route_change(event: ft.RouteChangeEvent):
    page = event.page
    route = event.route
    page.controls.clear()

    if route in page_list:
        page_class = page_list[route]
        page_instance = page_class(page, user_name=page.session.get("user_name"))
        page.controls.append(page_instance.build())
        
        if route != "/login_page":  # Add menu to pages other than login
            menu = AppMenu(page)
            page.controls.append(menu.build())
    else:
        page.controls.append(ft.Text("Page not found"))

    page.update()
