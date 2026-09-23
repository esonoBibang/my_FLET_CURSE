#contador con múltiples botones que comparten estado
#vesion de flet  0.86.1
"""
Ahora el caso interesante: varios botones (sumar, restar, x2, reset)
 que todos modifican el mismo estado compartido
"""

import flet as ft 

class ContadorMultiple(ft.Column):

    def __init__(self):
        super().__init__()

        #Atributos:
        self.contador = 0
        self.texto = ft.Text(value="",weight=ft.FontWeight.BOLD,size=30)
        self.estato = ft.Text(value="Listo",color=ft.Colors.WHITE)
        self.reseteado = False

        self.button_1 = ft.Button("Incrementar",on_click=self.incrementar)
        self.button_2 = ft.Button("Decrementar",on_click=self.decrementar)
        self.button_3 = ft.Button("X2",on_click=self.multiplicar_x2)
        self.button_4 = ft.Button("Resetear",on_click=self.resetear)

        #Lo que se mostrará en pantalla
        self.controls = [
            ft.Row(
                controls=[
                    self.button_1,
                    self.button_2,
                    self.button_3,
                    self.button_4,
                ]),
            self.texto,
            self.estato     
        ]

    #Metodos
    def incrementar(self,e):
        self.contador +=1
        self.texto.value = str(self.contador)
        self.texto.update()

    def decrementar(self,e):
        if self.reseteado:
            self.estato.value = "Listo"
            self.estato.update()
            
        self.contador -=1
        self.texto.value = str(self.contador)
        self.texto.update()

    def multiplicar_x2(self,e):
        if self.reseteado:
            self.estato.value = "Listo"
            self.estato.update()

        self.contador = self.contador * 2
        self.texto.value = str(self.contador)
        self.texto.update()

    def resetear(self,e):
        self.contador = 0
        self.texto.value = str(self.contador)
        self.reseteado = True

        self.texto.update()

              
"""Funcion principal"""
def main(page:ft.Page):
    page.padding = 20

    contenedor = ft.Container(

        content=ContadorMultiple(),
        width=600,
        height=200,
        bgcolor=ft.Colors.BLACK,
        padding=10,
        border_radius=15
    )

    contenedor_1 = ft.Container(
        content=contenedor,
        width=900,
        height=300,
        alignment=ft.Alignment.CENTER,
        bgcolor=ft.Colors.RED_400,
        border_radius=15

    )
    page.add(contenedor_1)

ft.run(main)
