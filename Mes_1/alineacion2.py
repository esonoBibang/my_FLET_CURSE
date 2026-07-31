
#Alineación dentro de un Container (`alignment`)

import flet as ft

def main(page:ft.Page):
    page.padding = 20
    page.title = "aligment on container"

    page.add(
        ft.Container(
            content=ft.Text("Container"),
            padding=10,
            bgcolor=ft.Colors.with_opacity(0.3,ft.Colors.BLUE_300),
            width=300,
            height=300,
            alignment=ft.Alignment.BOTTOM_LEFT,
            border_radius=15
        )
    )

ft.run(main)