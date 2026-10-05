import flet as ft
from components.componentes import boton_matricular,boton_profesor,boton_informacion
from views.vista_alumno import formulario_alumno, formulario_profesor, alumno_actual




def main(page: ft.Page):
    page.title = "Mi colegio"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 40


    #motrar paginas y construir la pila de vistas
    def route_change(e):

        page.views.clear()
        
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.AppBar(title=ft.Text("Mi colegio"),bgcolor=ft.Colors.GREEN_200),
                    ft.Text("Bienvenido al Colegio", weight=ft.FontWeight.BOLD),
                    ft.Row(
                        controls=[
                            boton_profesor(),
                            boton_matricular(),
                            boton_informacion()
                        ]
                    )
                ]
            )
        )

        #las diferentes rutas y vistas
        if page.route == "/profesor":
            page.views.append(
                ft.View(
                    route="/profesor",
                    controls=[
                        ft.AppBar(title=ft.Text("Profesor")),
                        ft.Text("Estamos en la pagina del profesor ",weight=ft.FontWeight.BOLD,size=30),
                        ft.ElevatedButton("Inicio",on_click=lambda e: page.go("/")),
                        formulario_profesor(),
                        
                        

                    ]
                )
            )

        if page.route == "/alumno":
            page.views.append(
                ft.View(
                    route="/alumno",
                    controls=[
                        ft.AppBar(title=ft.Text("Alumno")),
                        ft.Text("Estamos en la pagina del alumno ",weight=ft.FontWeight.BOLD,size=30),
                        ft.ElevatedButton("Inicio",on_click=lambda e: page.go("/")),
                        formulario_alumno(),
                        
                       

                    ]
                )
            )

        if page.route == "/informacion":
            page.views.append(
                ft.View(
                    route="/informacion",
                    controls=[
                        ft.AppBar(title=ft.Text("Informacion del Alumno")),
                        ft.Text("Estamos en la pagina de informacion del alumno ",weight=ft.FontWeight.BOLD,size=30),
                        ft.Text(f"Nombre: {alumno_actual.nombre}"),
                        ft.Text(f"Apellido: {alumno_actual.apellido}"),
                        ft.Text(f"Curso: {alumno_actual.curso}"),
                        ft.Text(f"Nivel: {alumno_actual.nivel}"),
                        
                        
                        

                    ]
                )
            )

        page.update()

    #cambiar de pagina
    async def view_pop(e):
        if len(page.views) > 1:
           page.views.remove(e.view)
           vista_actual = page.views[-1]
           await page.push_route(vista_actual.route)


    page.on_route_change = route_change #detecta el cambio de ruta y llama a la funcion
    page.on_view_pop = view_pop #detecta  la flecha de volver atras
    route_change(None) #construye la primera vista
        







ft.run(main)