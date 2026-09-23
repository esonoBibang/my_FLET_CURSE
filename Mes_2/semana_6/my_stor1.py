
#app con 3 pantallas (Inicio, Tienda, Anuncios)

#1.Imports, título y callbacks de navegación

#2 · route_change: construir la pila según la ruta

import flet as ft
#from urllib.parse import urlparse, parse_qs

def main(page:ft.Page):
    page.title = "Tienda con rutas completas"

    #1.Imports, título y callbacks de navegación

    # --- Callbacks de navegación (async, usando push_route) --

    async def ir_a_tienda(e):
        await page.push_route("/tienda")

    async def ir_a_anuncios(e):
        await page.push_route("/anuncios")

    async def volver_al_inicio(e):
        await page.push_route("/")

    async def acerca_de(e):
        await page.push_route("/acerca de")

    async def detalles(e):
        await page.push_route("/detalles")

    async def id(e):
        await page.push_route("/detalles/01/02/03")

    #2 · route_change: construir la pila según la ruta

    def route_change(e):
        page.views.clear()

        # la vista raiz siempre existe "/"
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.AppBar(title=ft.Text("Home"),bgcolor=ft.Colors.GREEN_200),
                    ft.Text("Bienvenido al Inicio"),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton("Tienda",on_click=ir_a_tienda),
                            ft.ElevatedButton("Anuncios",on_click=ir_a_anuncios),
                            ft.ElevatedButton("Acerca de",on_click=acerca_de),
                            ft.ElevatedButton("Detalles",on_click=detalles)
                        ]
                    ),
                    
                   
                ]
            )
        )

        if page.route == "/tienda":

            page.views.append(
                ft.View(
                    route="/tienda",
                    controls=[
                        ft.AppBar(title=ft.Text("Tienda")),
                        ft.Text("Estamos en la tienda ",weight=ft.FontWeight.BOLD,size=30),
                        ft.ElevatedButton("Inicio",on_click=volver_al_inicio)
                    ]
                )
            )
        elif page.route == "/anuncios":

            page.views.append(
                ft.View(
                    route="/anuncios",
                    controls=[
                        ft.AppBar(title=ft.Text("Anuncios")),
                        ft.ElevatedButton("Inicio",on_click=volver_al_inicio)
                    ]
                )
            )

        elif page.route == "/acerca de":

            page.views.append(
                ft.View(
                    route="/acerca de",
                    controls=[
                        ft.AppBar(title=ft.Text("Acerca de",size=30)),
                        ft.Text("A quí econtraras informacion sobre nosotros")
                    ]
                )
            )

        elif page.route == "/detalles":

            page.views.append(
                ft.View(
                    route="/detalles",
                    controls=[
                        ft.AppBar(title=ft.Text("Detalles")),
                        ft.ElevatedButton("IDs",on_click=id),
                    ]
                )
            )

        elif page.route.startswith("/detalles/"):
            partes_ruta = page.route.split("/")
            id_1 = partes_ruta[2]
            id_2 = partes_ruta[3]
            id_3 = partes_ruta[4]

            page.views.append(
                ft.View(
                    route="/detalles/01/02/03",
                    controls=[
                        ft.ElevatedButton("Inicio",on_click=volver_al_inicio),
                        ft.AppBar(title=ft.Text("Los IDs")),
                        ft.Text(f"Primer ID:  {id_1}"),
                        ft.Text(f"Segundo ID: {id_2}"),
                        ft.Text(f"Tercer  ID: {id_3}"),
                        
                    ]
                )
            )

        page.update() #redibuja la pantalla con la pila ya construida.

    async def view_pop(e):

        if len(page.views)>1:
            page.views.remove(e.view) #eliminamaos la vista del evento
            vista_actual = page.views[-1] # tomamos la vista anterior
            await page.push_route(vista_actual.route) #pasa a la ruta de dicha vista



    page.on_route_change = route_change #detecta el cambio de ruta y llama a la funcion
    page.on_view_pop = view_pop #detecta  la flecha de volver atras
    route_change(None) #construye la primera vista




ft.run(main)