#CONTROLES BASICOS. Texto
import flet as ft


def main(page: ft.Page):
    page.title = "Mostrar_textos"


    #CONTROLES DE TEXTO
    text_1 = ft.Text("BIENVENIDOS")
    text_2 = ft.Text("Bienvenidos, aquí estoy trabajando con controles básicos de flet (texto)",size=30,weight=ft.FontWeight.BOLD)
    text_3 = ft.Text("Bienvenidos al primer mes con flet",italic=True, size=20)
    text_4 = ft.Text("Espero que disfruten con migo en este increible mundo de programación",color=ft.Colors.GREEN)

    #Poner el texto en la pantalla
    page.add(
        text_1,
        text_2,
        text_3,
        text_4,
    )


ft.app(main)
