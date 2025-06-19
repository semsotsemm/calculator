import flet as ft

def main(page: ft.Page):
    ##Функции
    def get_info(e, i):
        if( result.value != "0"):
            result.value += numbers[i].text
        else:
            result.value = numbers[i].text
        page.update()

    def get_operation(e, i):
        if i == 9:
            result.value = str(-1 * int(result.value))
        else:
            result.value += operation_symbols[i]
        page.update()

    def get_result(e):
        try:
            expression = result.value
            if "/0" in expression:
                if "-" in expression:
                    result.value = "-∞"
                else:
                    result.value = "∞"
            elif "%" in expression:
                expression = expression.replace("%", "/100")
                result.value = str(eval(expression))
            else:
                result.value = str(eval(expression))
        except Exception:
            result.value = "Ошибка"
        page.update()
    
    def clear_strok(e, i):
        if(i == 6):
            result.value = result.value[:-1] if result.value != "0" else "0"
        else:
            result.value = "0"
        page.update()
    
    #Параметры цифр
    numbers_styles = ft.ButtonStyle(
        bgcolor=ft.Colors.with_opacity(1, "#1F1F1F"),
        color=ft.Colors.WHITE,
        text_style=ft.TextStyle(weight=ft.FontWeight.W_900,font_family="Courier New")
    )

    numbers = [
        ft.ElevatedButton("1", on_click=lambda e: get_info(e, 0), style=numbers_styles),
        ft.ElevatedButton("2", on_click=lambda e: get_info(e, 1), style=numbers_styles),
        ft.ElevatedButton("3", on_click=lambda e: get_info(e, 2), style=numbers_styles),
        ft.ElevatedButton("4", on_click=lambda e: get_info(e, 3), style=numbers_styles),
        ft.ElevatedButton("5", on_click=lambda e: get_info(e, 4), style=numbers_styles),
        ft.ElevatedButton("6", on_click=lambda e: get_info(e, 5), style=numbers_styles),
        ft.ElevatedButton("7", on_click=lambda e: get_info(e, 6), style=numbers_styles),
        ft.ElevatedButton("8", on_click=lambda e: get_info(e, 7), style=numbers_styles),
        ft.ElevatedButton("9", on_click=lambda e: get_info(e, 8), style=numbers_styles),
        ft.ElevatedButton("0", on_click=lambda e: get_info(e, 9), style=numbers_styles)
    ]
    
    #Стили вспомогающих кнопок
    management_styles = ft.ButtonStyle(
        bgcolor=ft.Colors.with_opacity(1, "#4D4D4D"),
        color=ft.Colors.WHITE,
        text_style=ft.TextStyle(
            weight=ft.FontWeight.W_900,
            font_family="Courier New"
            )
    )

    #Параметры операций
    operations_styles = ft.ButtonStyle(
        bgcolor=ft.Colors.with_opacity(1, "#FFC400"),
        color=ft.Colors.WHITE,
        text_style=ft.TextStyle(
            weight=ft.FontWeight.W_900,
            font_family="Courier New"
            )
    )

    operation_symbols = ["+", "-", "*", "/", "%", "."]

    operations = [
           ft.ElevatedButton("+", on_click=lambda e: get_operation(e, 0), style=operations_styles),
           ft.ElevatedButton("-", on_click=lambda e: get_operation(e, 1), style=operations_styles),
           ft.ElevatedButton("×", on_click=lambda e: get_operation(e, 2), style=operations_styles),
           ft.ElevatedButton("/", on_click=lambda e: get_operation(e, 3), style=operations_styles),
           ft.ElevatedButton("<-", on_click=lambda e: clear_strok(e,6), style=management_styles),
           ft.ElevatedButton("C", on_click=lambda e: clear_strok(e,7), style=management_styles),
           ft.ElevatedButton("=", on_click=lambda e: get_result(e), style=operations_styles),
           ft.ElevatedButton("%", on_click=lambda e: get_operation(e, 4), style=operations_styles),
           ft.ElevatedButton("+/-", on_click=lambda e: get_operation(e,9), style=management_styles),
           ft.ElevatedButton(".", on_click=lambda e: get_operation(e, 5), style=numbers_styles)
    ]
    
    ##Базовые настройки
    page.title = "Калькулятор"
    page.theme_mode = "dark"
    page.bgcolor = ft.Colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    result = ft.TextField(value="0", width = 250, text_align = ft.TextAlign.CENTER, on_submit=get_result)

    ##Добавление кнопок на страницу
    page.add(
        ft.Row([result],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([operations[4],operations[8],operations[5],operations[3]],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([numbers[0],numbers[1],numbers[2],operations[2]],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([numbers[3],numbers[4],numbers[5],operations[1]],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([numbers[6],numbers[7],numbers[8],operations[0]],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([operations[9],numbers[9],operations[7],operations[6]],alignment=ft.MainAxisAlignment.CENTER),
    )
    result.focus()

ft.app(target=main)