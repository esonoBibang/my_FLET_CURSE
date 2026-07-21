
#TRABAJANDO CON CAMPO DE TEXTO
import flet as ft
from rich import color


def main(page: ft.Page):

    page.title = "Trabajando con TextField"

    def mostrar_texto(e):
        texto.value = campo_texto.value
        campo_texto.value = ""
        #page.update()

    campo_texto = ft.TextField(
        label="Escriba aquí",
        hint_text="Su nombre",
        on_submit=mostrar_texto
         )
    texto = ft.Text()



    page.add(campo_texto, texto)




ft.app(main)