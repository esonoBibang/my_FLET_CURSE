import flet as ft

def main(page:ft.Page):
    page.padding = 20
    page.title = "Oficina Escolar"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.WHITE

    #Tamaño inicial de la ventana:
    page.window.width = 1200
    page.window.height = 900
    page.window.resizable = True # se puede redimencionar

    texto = ft.Text("Los dos factores de reducción de la ecuación (5.90) forman un producto que hay que considerar " \
    "con cuidado en cualquier procedimiento de diseño. No es suficiente asegurarse de que Rs " \
    "sea relativamente pequeña si se pasa por alto el efecto de la magnitud de RL. Por ejemplo" \
    "en la ecuación (5.90) si el primer factor es 0.9 y el segundo es 0.2, el producto de los dos da " \
    "un factor de reducción total igual a (0.9)(0.2) ⫽ 0.18, el cual se aproxima al factor menor." \
    " El efecto del excelente nivel de 0.9 fue borrado por completo por el segundo multiplicador "
    )
    #funciones:
    def mostrar_texto(e):
        texto.value = f"la asignatura seleccionada es : {e.control.value}"
        page.update()

    #baches (Card)
    def bache(texto,bgcolor=ft.Colors.BLACK):
        return ft.Card(
            content= ft.Container(
               content=ft.Text(texto,color=ft.Colors.WHITE,size=15),
               padding=5,
               alignment=ft.Alignment.CENTER
            ),

            #configuraciones de Card
            elevation=20,
            bgcolor=bgcolor,
            expand=True # todas las cards reparten el espacio por igual

        )
    banner = ft.Container(
        content=ft.Row(
            controls=[
                bache("home"),
                bache("Programacion"),
                bache("Alumnos"),
                bache("profesores"),
                bache("Matricula"),
                bache("Informes"),
            ]
                ,
            #configuraciones de las filas
        ),
        #configuraciones del contenedor
        padding=10,
        height= 60,
        expand=True,# se ajusta al ancho del padre
        #bgcolor=ft.Colors.WHITE,
        alignment=ft.Alignment.TOP_CENTER,
        border_radius=15
        
    )

    #elementos del checkbox
    languege_2 = ft.Checkbox(label="C++",value=False)
    languege_3 = ft.Checkbox(label="C#",value=False)
    languege_4 = ft.Checkbox(label="Java",value=False)
    languege_5 = ft.Checkbox(label="JavaScripts",value=False)

    asignaruras = ft.Dropdown(
        label="Asignaturas",
        width=180,
        border_color="RED",
        on_select= mostrar_texto,
        options=[
            ft.DropdownOption(key="Matematicas",text="Matematicas"),
            ft.DropdownOption(key="Lengua y literatura",text="Lengua y literatura"),
            ft.DropdownOption(key="Fisica",text="Fisica"),
            ft.DropdownOption(key="Química",text="Química"),
            ft.DropdownOption(key="Historia",text="Historia"),
            ft.DropdownOption(key="Biología",text="Biología"),
            ft.DropdownOption(key="Dibujo",text="Dibujo"),
            ft.DropdownOption(key="electrotecnia",text="electrotecnia"),
            ft.DropdownOption(key="Francés",text="Francés"),
            ft.DropdownOption(key="Inglés",text="Inglés")

        ]
    )
    menu = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=asignaruras,
                    padding=10,
                    width=200,
                    height=60,
                    margin=10,
                    ),
                languege_2,
                languege_3,
                languege_4,
                languege_5
            ],spacing=5
        ),
        height=700,
        width=200,
        bgcolor=ft.Colors.BLACK,
        border_radius=15

    )

    body_principal = ft.Container(
            content=ft.Column(
                controls=[texto]
            ),
            padding=10,
            bgcolor=ft.Colors.BLACK,
            border_radius=15,
            expand=True,  # ocupa todo el espacio restante
            height=700


        )


    body = ft.Container(
        content=ft.Row(
            controls=[menu,body_principal],
            spacing=5,
            expand=True,
        ),   
        #configuraciones de del contenedor body
        bgcolor=ft.Colors.GREEN,
        border_radius=15,
        padding=10,
        expand=True,  # se ajusta al alto/ancho disponible
        
    )

    #CONTENEDOR PADRE
    boss_container = ft.Container(
        content=ft.Column(
            controls=[banner,body],
            spacing=5,
            expand=True
        ),
    )

    page.add(boss_container)



ft.run(main)