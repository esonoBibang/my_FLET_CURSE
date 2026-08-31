#Variables de estado dentro de la función main

import flet as ft

def main(page:ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER

    contador = 0 # variable de estado

    texto = ft.Text(value=str(contador),size=30,color=ft.Colors.BLACK)

    def incrementar(e): 
        nonlocal contador            # necesario para modificar la variable externa
        contador += 1                #incrementamos la cuenta
        texto.value = str(contador)  # cambiamos el el valor del texto
        
        page.update()                #sin esto la pagina no cambia (redibuja toda la página)

    page.add(
        texto,
        ft.Button("Incrementar",on_click=incrementar)
    )
ft.run(main)