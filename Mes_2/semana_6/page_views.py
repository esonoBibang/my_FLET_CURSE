
#La pila de pantallas
#page.views

import flet as ft

def main(page:ft.Page):
    page.title = "page.views"

    #Cremos  un objeto view
    vista_inicio = ft.View( 
        route="/", 
        controls=[
        ft.AppBar(
            title=ft.Text("Inicio")), 
            ft.Text("Bienvenido a la app 1"),
            ], )

    #Añadimos a la alista Views
    page.views.append(vista_inicio)
  
ft.app(target=main)

