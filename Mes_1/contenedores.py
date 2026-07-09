#Container - Caja con estilo
import flet as ft
from flet.controls import border_radius


def main(page: ft.Page):
    page.title = 'Contenedores'
    page.horizontal_alignment =ft.CrossAxisAlignment.CENTER

    caja_1 = ft.Container(
        content = ft.Text('caja_1 con color y bordes redondeados'),
        width = 300,
        height = 100,
        bgcolor = ft.Colors.BLUE_500,
        border_radius = 20,
        padding = 10,
        alignment = ft.Alignment.CENTER,
    )
    caja_2 = ft.Container(
        content=ft.Text('caja_2 con color y bordes redondeados'),
        width = 300,
        height = 100,
        border_radius = 20,
        padding = 10,
        bgcolor = ft.Colors.RED,
        margin = 10,
        #border=ft.Border.all(1, ft.Colors.RED)
    )

    page.add(caja_1)
    page.add(caja_2)


ft.run(main)