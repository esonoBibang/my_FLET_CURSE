"""botones y texto"""
import flet as ft
from flet.controls.material import tooltip


def main(page: ft.Page):
    page.title = 'Botones y texto'
    page.padding =20
    page.horizontal_alignment ='center'

    # Texto con distintos estilos
    titulo = ft.Text("Controles Básicos (Button and Text)", size=24, weight=ft.FontWeight.BOLD)
    mensaje = ft.Text("Presiona un botón para ver el resultado", size=14, color=ft.Colors.GREY_700)
    campo_texto = ft.TextField(
        label="Escriba lo que piensas de app",
        hint_text="Creo se podría...",
        #helper="Usaremos esto solo para notificarte",
        icon=ft.Icons.EMAIL,
        #prefix_icon=ft.Icons.ALTERNATE_EMAIL,
        border=ft.InputBorder.UNDERLINE,
        filled=True,
        max_length=50,
        width=300,
        height=300,  # fuerza un alto fijo
        multiline=True,
        #counter="{value_length}/{max_length} caracteres",
        #on_change=lambda e: print(e.control.value),
    )


    def al_hacer_click_elevated(e):
        #Modificamos la forma del mensaje
        mensaje.value = "Presionaste el ElevatedButton"
        mensaje.color = ft.Colors.BLUE
        mensaje.font = ft.FontWeight.BOLD
        mensaje.size = 24
        page.update() #Actualizamos la pagina

    def al_hacer_cick_text(e):
        mensaje.value = "Texto enviado"
        campo_texto.value = "Mensaje enviado"
        mensaje.color = ft.Colors.GREEN
        mensaje.size = 24
        page.update()

    def al_hacer_click_icon(e):
        mensaje.value = "Presionaste el IconButton"
        mensaje.color = ft.Colors.RED_700
        page.update()



    #Creamos los botones

    boton_elevated = ft.ElevatedButton(
        content = "Elevated",
        icon = ft.Icons.SEND,
        tooltip = "Send",
        on_click = al_hacer_click_elevated
    )

    boton_text = ft.TextButton(
        content = "TextButton",
        icon = ft.Icons.CHAT,
        tooltip = "Escriba un mensaje",
        on_click = al_hacer_cick_text

    )

    boton_icon = ft.IconButton(
        icon = ft.Icons.FAVORITE_BORDER,
        on_click = al_hacer_click_icon,
        tooltip = "Me gusta",
        icon_color = ft.Colors.RED_700

    )


    page.add(titulo,mensaje,campo_texto,
             ft.Row([boton_elevated,boton_text,boton_icon]),
            )




ft.run(main)