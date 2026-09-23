import flet as ft
from urllib.parse import urlparse, parse_qs

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

    async def mi_query(e):
        await page.push_route("https://www.ejemplo.com/productos/zapatos;color=rojo?categoria=deportivo&talla=42#reseñas")

    async def desconocida(e):
        await page.push_route("/error")


    #2 · route_change: construir la pila según la ruta

    def route_change(e):
        page.views.clear()

       # async def mi_query(e):
           # await page.push_route("https://www.ejemplo.com/productos/zapatos;color=rojo?categoria=deportivo&talla=42#reseñas")

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
                            ft.ElevatedButton("Detalles",on_click=detalles),
                            ft.ElevatedButton("Desconocida",on_click=desconocida)
                            
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
                        ft.ElevatedButton("Query",on_click=mi_query),
                    ]
                )
            )

        elif urlparse(page.route).path.startswith("/productos"):
            
            componentes_ruta = urlparse(page.route) #lista
            my_queries = parse_qs(componentes_ruta.query) # lista

            page.views.append(
               ft.View(
                   route=page.route,
                   controls=[
                ft.AppBar(title=ft.Text("Partes de la dirección")),
                ft.Text(f"scheme: {componentes_ruta.scheme}"),
                ft.Text(f"netloc: {componentes_ruta.netloc}"),
                ft.Text(f"path: {componentes_ruta.path}"),
                ft.Text(f"params: {componentes_ruta.params}"),
                ft.Text(f"query: {componentes_ruta.query}"),
                ft.Text(f"fragment: {componentes_ruta.fragment}"),
                ft.Text(f"queries parseadas: {my_queries}"),
                   ]
               )
           )
        elif page.route == "/error":
            page.views.append(
                ft.View(
                    route="/error",
                    controls=[
                        ft.AppBar(title=ft.Text("ERROR"))
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