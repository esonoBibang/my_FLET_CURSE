
#Espaciado: spacing, padding y margin

import flet as ft

def main(page:ft.Page):
    page.padding = 40


    box_1 = ft.Container(
        content=ft.Text("BOX NUMBER 1, whit padding",color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD),
        bgcolor=ft.Colors.TEAL_100,
        padding=ft.Padding.all(20),          # padding igual en los 4 lados
        margin=ft.Margin.symmetric(vertical=10, horizontal=5),  # margin distinto por eje
        border_radius=8,

    )

    box_2 = ft.Container(
        content=ft.Text("BOX NUMBER TWO, whit asymetric padding",color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD),
        bgcolor=ft.Colors.TEAL_100,
        padding=ft.Padding.only(left=30, top=10, right=30, bottom=10),
        border_radius=8,

    )

    page.add(
        box_1,
        box_2,
    )

ft.run(main)




