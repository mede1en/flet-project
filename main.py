import flet as ft #as ft укораяивает слово flet

def app(page: ft.Page):
    # button = ft.Button(content="button")
    plane_text = ft.Text(value="hello world")
    # page.theme_mode = ft.ThemeMode.LIGHT

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        
    icon_button = ft.IconButton(icon=ft.Icons.SMART_BUTTON, on_click=change_theme)

    def change(e):
        txt = user_input.value.strip()
        user_input.value= ""

        if txt:
            plane_text.color = None
            plane_text.value = f"hello {txt}"
        else:
            plane_text.value = f"Введите коррекное имя {user_input.value}"
            plane_text.color = ft.Colors.RED_600

    
    # button.content = "дргая кнопка"
    # button.color= ft.Colors.GREEN_900

    btn = ft.TextButton("отправить", on_click=change)
    user_input = ft.TextField(label="enter name", on_submit=change)

    page.add(plane_text, 
             user_input,
             btn,
             icon_button)


ft.app(app) #view= ft.AppView.WEB_BROWSER -----запуск через браузер


# gitignore.io