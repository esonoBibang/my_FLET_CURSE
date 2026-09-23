
#page.go(): cómo navegar
#no dibuja nada por sí mismo: solo cambia la ruta y avisa a tu código
import flet as ft

def main(page:ft.Page):
    page.title = "page.go()"

    def ir_a_ventatas(e):
        print("Estamos en ventas")
        page.go("/ventas")

    page.add(
        ft.ElevatedButton("ventas",on_click=ir_a_ventatas))


ft.run(main)

