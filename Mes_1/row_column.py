import flet as ft


def main(page: ft.Page):
    page.title = "Row and Column"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding =20
    

    # Create a Rows with containers Text widgets
    text_row = ft.Text("THIS IS A ROWS", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    text_column = ft.Text("THIS IS A COLUMNS", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    row = ft.Row(
        controls=[
            ft.Container(
                bgcolor=ft.Colors.RED_500, 
                width=200, 
                height=100,
                content=ft.Text("COTAINER 1"),
                padding=10,
                border_radius=15,
                alignment=ft.Alignment.TOP_CENTER
                
                ),

            ft.Container(
                bgcolor=ft.Colors.GREEN_500, 
                width=200, 
                height=100,
                content=ft.Text("CONTAINER 2",weight=ft.FontWeight.BOLD,),
                border_radius=15,
                alignment=ft.Alignment.TOP_CENTER,
                padding=10
                ),

            ft.Container(bgcolor=ft.Colors.BLUE_500, width=200, height=100,content=ft.Text("CONTAINER 3",weight=ft.FontWeight.BOLD,),border_radius=15,alignment=ft.Alignment.TOP_CENTER,padding=10),
            ft.Container(bgcolor=ft.Colors.BROWN_400,width=200,height=100,content=ft.Text("CONTAINER 4",weight=ft.FontWeight.BOLD,),border_radius=15,alignment=ft.Alignment.TOP_CENTER,padding=10)
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    #creat column with containers and text widgets
    column = ft.Column(
        controls=[
            ft.Container(bgcolor=ft.Colors.BLUE_300,width=400,height=100,border_radius=15,content=ft.Text("CONTAINER 1",weight=ft.FontWeight.BOLD,),alignment=ft.Alignment.CENTER,padding=10),
            ft.Container(bgcolor=ft.Colors.BROWN_400,width=400,height=100,border_radius=15,content=ft.Text("CONTAINER 2",weight=ft.FontWeight.BOLD,),alignment=ft.Alignment.CENTER,padding=10),
            ft.Container(bgcolor=ft.Colors.GREEN_300,width=400,height=100,border_radius=15,content=ft.Text("CONTAINER 3",weight=ft.FontWeight.BOLD,),alignment=ft.Alignment.CENTER,padding=10),
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.CENTER
    )
    

    # Add the Row and Column to the page
    page.add(
        text_row, 
        row, 
        text_column,
        column)

    page.add(
            ft.Row(
                controls=[
                    ft.Column([ft.Icon(ft.Icons.STAR), ft.Text("Favoritos")]),
                    ft.Column([ft.Icon(ft.Icons.HOME), ft.Text("Inicio")]),
                    ft.Column([ft.Icon(ft.Icons.SETTINGS), ft.Text("Configuración")]),
                    ft.Column([ft.Icon(ft.Icons.INFO), ft.Text("Información")]),
                    ft.Column([ft.Icon(ft.Icons.CONTACT_PAGE), ft.Text("Contacto")]),
                    ft.Column([ft.Icon(ft.Icons.HELP), ft.Text("Ayuda")]),
                    ft.Column([ft.Icon(ft.Icons.SHOPPING_CART), ft.Text("Carrito")]),
                    ft.Column([ft.Icon(ft.Icons.PERSON), ft.Text("Perfil")]),
                    ft.Column([ft.Icon(ft.Icons.NOTIFICATIONS), ft.Text("Notificaciones")]),
    
                ]
            )
        )

ft.app(main)