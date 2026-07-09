#TRABAJANDO CON BOTONES

import flet as ft

def main(page: ft.Page):
    page.title = "Botones_en_flet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    contador = ft.Text("0", size=20)
    numero = 0

    def sumar(e):
        nonlocal numero #modificar la variable numero dentro de la funcion anidada
        numero += 1
        contador.value = str(numero) #+1,+2,...
        page.update()

    def restar(e):
        nonlocal numero
        numero -= 1
        contador.value = str(numero) #-1,-2,...
        page.update()

    page.add(
        ft.Row([
            ft.IconButton(icon=ft.Icons.REMOVE, on_click=restar),
            contador,
            ft.IconButton(icon=ft.Icons.ADD, on_click=sumar),
        ],
        ),
        ft.ElevatedButton("Boton elevado", on_click=lambda e: print("Clic")),
        ft.OutlinedButton("Boton con borde"),
        ft.TextButton("Boton de texto"),
    )


ft.app(main)