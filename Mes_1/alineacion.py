### a) Alineación dentro de Row/Column (ejes principal y transversal)
import flet as ft

def main(page:ft.Page):
    page.padding = 20

    page.add(
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("ONE",color=ft.Colors.BLACK),
                    ft.Text("TWO",color=ft.Colors.BLACK),
                    ft.Text("Three",color=ft.Colors.BLACK),
                    ft.Text("Four",color=ft.Colors.BLACK),
                    ft.Text("Five",color=ft.Colors.BLACK)
                    ],

                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                vertical_alignment=ft.CrossAxisAlignment.START
            ),
            height= 80,
            bgcolor= ft.Colors.BLUE_100,
            padding= 10,
            border_radius=15,
            width=500

        )
    )

ft.run(main)