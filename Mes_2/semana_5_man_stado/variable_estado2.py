
#El uso de control.update() 
import flet as ft 

def main(page:ft.Page):
    contador = 0
    actulizar_barra_estado = False
    #Controles:
    texto = ft.Text(value="O", size=30)
    barra_estado = ft.Text(value="Listo",color="GREEN")

    #Metodos o funciones
    def incrementar(e):
        nonlocal contador
        nonlocal actulizar_barra_estado

        if actulizar_barra_estado == True:
            barra_estado.value = "Listo"
            barra_estado.update()
 
        contador += 1
        texto.value = str(contador)
        texto.update() #redibujamos el control

    def resetear(e):
        nonlocal contador
        nonlocal actulizar_barra_estado

        actulizar_barra_estado = True
        contador = 0
        texto.value = "0"
        barra_estado.value = "Contador reiniciado"
        page.update()

    def decrementar(e):
        nonlocal contador
        contador -= 1
        texto.value = str(contador)
        texto.update()

    page.add(
        texto,
        ft.Row(
            controls=[
                ft.Button("Incrementar",on_click=incrementar,bgcolor=ft.Colors.WHITE,color=ft.Colors.BLACK),
                ft.Button("Resetear",on_click=resetear,bgcolor=ft.Colors.WHITE,color=ft.Colors.BLACK),
                ft.Button("Decrementar",on_click=decrementar,bgcolor=ft.Colors.WHITE,color=ft.Colors.BLACK),
            ]
        ),
        barra_estado
    )
    
ft.run(main)
