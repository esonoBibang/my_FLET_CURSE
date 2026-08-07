#Diseño responsive básico

import flet as ft

def main1(page:ft.Page):
    page.title = "Responsive basico"
    page.padding = 20

    status_text = ft.Text()

    card = ft.Container(
        content=ft.Text("Responsive content",color=ft.Colors.BLACK),
        bgcolor=ft.Colors.BLUE_GREY_500,
        padding=20,
        border_radius=8

    )

    def ajustar_layout(e=None):

        ancho = page.width # ancho actual del viewport en px lógicos

        if ancho < 600:
            # "modo móvil": la tarjeta ocupa casi todo el ancho
            card.width = ancho - 40 #modificamos el ancho de la tarjeta para que ocupe casi todo el ancho del viewport
            status_text.value = f'Modo compacto (ancho: {ancho:.0f}px)'

        else:
            # "modo escritorio": ancho fijo, más elegante
            card.width = 400
            status_text.value = f"Modo amplio (ancho: {ancho:.0f}px)"

        page.update()

    page.on_resize = ajustar_layout  # se dispara cada vez que cambia el tamaño de la página

    page.add(status_text, card)

    ajustar_layout()  # llamada inicial para fijar el estado al abrir la app

#ft.run(main1)

#el expand

def main2(page: ft.Page):
    page.padding = 20

    page.add(
        ft.Row(
            controls=[
                ft.Container(bgcolor=ft.Colors.BLUE, width=100, height=100),
                ft.Container(bgcolor=ft.Colors.RED, width=100, height=100),
                ft.Container(bgcolor=ft.Colors.GREEN, width=100, height=100),
            ],
            expand=True, #the row will expand to fill the available space
            #height=150
        )
    )

ft.run(main2)


    