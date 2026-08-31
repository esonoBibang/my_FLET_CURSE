# Uso de clases para encapsular estado (patrón “componente”)

#Cuando la app crece, tener todo suelto en main se vuelve un lío. La solución: 
#Crear una clase que hereda de un control de Flet (por ejemplo ft.Column) y que guarda su propio estado adentro.

import flet as ft 

class Contador(ft.Column):
    def __init__(self):
        super().__init__()

       
        self.contador = 0
        self.texto = ft.Text(value="0",size=30,weight=ft.FontWeight.BOLD)
        self.comentario = ft.Text("listo",size=30,weight=ft.FontWeight.BOLD)

        self.boton_1 = ft.Button("Incrementar",on_click=self.incrementar)
        self.boton_2 = ft.Button("Decrementar",on_click=self.decrementar)

        #Artibuto de ft.column
        self.controls = [
            self.texto,
            ft.Row(controls=[self.boton_1,self.boton_2]),
            self.comentario
        ]
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def incrementar(self,e):
            self.contador += 1
            self.texto.value = str(self.contador)
            self.texto.update()

    def decrementar(self,e):
         self.contador -= 1
         self.texto.value = str(self.contador)
         self.texto.update()
         
def main(page:ft.Page):
    page.add(Contador())

ft.run(main)
