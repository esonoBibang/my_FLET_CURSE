#CONTAINER

import flet as ft

def main(page: ft.Page):
    page.title = "container"
    page.padding = 30
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    columns = ft.Column(
        controls=[
                ft.Text("Container 1",size=24,weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK),
                ft.TextField(),
                ft.TextField(),
                ft.TextField(),
                ft.TextField()
        ]
    )
    box = ft.Container(
        content=columns,
            
        #configuraciones del contenedor
        bgcolor=ft.Colors.BLUE_GREY_500,
        width=300,
        height=400,
        padding=20,
        alignment=ft.Alignment.TOP_CENTER,
        border_radius=15,
        shadow=ft.BoxShadow(
            spread_radius=10,
            blur_radius=20,
            color=ft.Colors.with_opacity(0.5,ft.Colors.RED)
            ),
                  

    )

    page.add(box)



ft.run(main)


