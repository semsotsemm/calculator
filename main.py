import flet as ft

def main(page: ft.Page):
    def get_info(e, i):
        if( result.value != "0"):
            result.value += numbers[i].text
        else:
            result.value = numbers[i].text
        page.update()

    def get_operation(e, i):
        current_operation = operations[i]
        result.value += operations[i].text
        page.update()

    def get_result(e):
        try:
            expression = result.value
            if "/0" in expression:
                if "-" in expression:
                    result.value = "-∞"
                else:
                    result.value = "∞"
            else:
                result.value = str(eval(expression))
        except Exception:
            result.value = "Ошибка"
        page.update()
    
    def clear_strok(e, i):
        if(i == 4):
            result.value = result.value[:-1] if result.value != "0" else "0"
        else:
            result.value = "0"
        page.update()

    page.title = "Калькулятор"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    result = ft.TextField(value="0", width = 300, text_align = ft.TextAlign.CENTER, on_submit=get_result)
    numbers = [
        ft.ElevatedButton("1", on_click=lambda e: get_info(e, 0)),
        ft.ElevatedButton("2", on_click=lambda e: get_info(e, 1)),
        ft.ElevatedButton("3", on_click=lambda e: get_info(e, 2)),
        ft.ElevatedButton("4", on_click=lambda e: get_info(e, 3)),
        ft.ElevatedButton("5", on_click=lambda e: get_info(e, 4)),
        ft.ElevatedButton("6", on_click=lambda e: get_info(e, 5)),
        ft.ElevatedButton("7", on_click=lambda e: get_info(e, 6)),
        ft.ElevatedButton("8", on_click=lambda e: get_info(e, 7)),
        ft.ElevatedButton("9", on_click=lambda e: get_info(e, 8)),
        ft.ElevatedButton("0", on_click=lambda e: get_info(e, 9))
    ]
    operations = [
           ft.ElevatedButton("+", on_click=lambda e: get_operation(e, 0)),
           ft.ElevatedButton("-", on_click=lambda e: get_operation(e, 1)),
           ft.ElevatedButton("*", on_click=lambda e: get_operation(e, 2)),
           ft.ElevatedButton("/", on_click=lambda e: get_operation(e, 3)),
           ft.ElevatedButton("<-", on_click=lambda e: clear_strok(e, 4)),
           ft.ElevatedButton("C", on_click=lambda e: clear_strok(e, 5)),
           ft.ElevatedButton("=", on_click=lambda e: get_result(e))
    ]


    page.add(
        ft.Row([result],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([numbers[0],numbers[1],numbers[2],operations[0]],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([numbers[3],numbers[4],numbers[5],operations[1]],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([numbers[6],numbers[7],numbers[8],operations[2]],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([numbers[9],operations[3],operations[4],operations[5],operations[6]],alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main #,view= ft.AppView.WEB_BROWSER)
)