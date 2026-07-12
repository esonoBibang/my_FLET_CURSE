"""Formulario con validación básica usando TextField, incluyendo campo de contraseña y campo numérico."""
import flet as ft
from flet.controls import alignment


def main(page:ft.Page):
    page.title = "Text Field"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    result = ft.Text(value="",size = 16)
    check_password = ft.Text(value="",size = 16)

    name_field = ft.TextField(
        label='Name',
        width = 300,
        hint_text = "your name",
        border=ft.InputBorder.UNDERLINE,
        filled=True,
    )
    password_field = ft.TextField(
        label="Password",
        password = True,
        can_reveal_password = True,
        width = 300,
        border=ft.InputBorder.UNDERLINE,
        filled=True,
    )

    number_field = ft.TextField(
        label="Old",
        keyboard_type = ft.KeyboardType.NUMBER,
        width = 300,
        border = ft.InputBorder.UNDERLINE,
        filled = True,
    )


#Verificamos si se ha introducido los datos en elos campos
    def validar(e):
        if name_field.value == "":
            name_field.value = "Este campo es obligatorio"
            page.update()
            return
        elif password_field.value == "":
            check_password.value="No pusiste una contraseña"
            page.update()
            return
        elif check_password.value == "No pusiste una contraseña":
            check_password.value = ""
            page.update()
            return

        else:
            result.value = f"Hola {name_field.value}, tienes {number_field.value} años!"
            page.update()


    def limpiar(e):
        name_field.value = ""
        password_field.value = ""
        number_field.value = ""
        page.update()


    page.add(
        name_field,
        password_field,
        number_field,
        ft.Row([
            ft.ElevatedButton(content="Enviar",on_click=validar),
            ft.ElevatedButton(content="limpiar",on_click=limpiar)
        ],alignment=ft.MainAxisAlignment.CENTER,),
        result,
        check_password,
    )

ft.run(main)


