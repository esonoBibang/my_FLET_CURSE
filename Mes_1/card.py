### Card

import flet as ft 

def main(page:ft.Page):
    page.title = "Etiquetas"
    page.padding = 20
    page.bgcolor =ft.Colors.LIGHT_GREEN_50
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    targeta = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Name: Antonio Esono",weight=ft.FontWeight.BOLD,size=12),
                    ft.Text("content of the card",weight=ft.FontWeight.BOLD,size=12)] 
                    ),
            padding=10,
            bgcolor=ft.Colors.BLUE_GREY_700,
             
        ),
        elevation=20 #Defines the size of the shadow below the card
        
        )
    
    horizontal_line = ft.Divider(color=ft.Colors.GREEN,height=20,thickness=2)

    icon = ft.Icon(ft.Icons.FAVORITE, color=ft.Colors.PINK, size=40)

    image = ft.Image(
        src =r"D:\my_FLET_CURSE\Mes_1\picture.jpg",
        width=600,
        height=600,
        expand=1
        #fit=ft.BoxFit.COVER,            # recorta manteniendo proporción, sin deformar
        #border_radius=ft.BorderRadius.all(75),  # ejemplo: imagen circular (radio = mitad del ancho)
    )

    page.add(targeta,horizontal_line,icon,image)


ft.run(main)

