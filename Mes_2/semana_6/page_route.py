
#page.route: un texto que guarda en qué ruta estás ahora mismo (por ejemplo / o /detalle).
#conocer la ruta actual

import flet as ft

def main(page: ft.Page):
    page.title = "page.route"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    #Mostrar la ruta actual en la que estamos
    def mostrar_ruta_actual(e):
        page.add(ft.Text(f"Ruta actual: {page.route}"))

    page.add(
        ft.ElevatedButton(
            "Mostrar ruta actual", on_click=mostrar_ruta_actual ))
        
ft.run(main)


