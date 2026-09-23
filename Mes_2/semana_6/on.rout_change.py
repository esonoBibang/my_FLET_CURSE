#on_route_change y on_view_pop


import flet as ft

def main(page: ft.Page):
    page.title = "Rutas completas"

    # --- Callbacks de navegación (ahora async, usando push_route) ---
    async def ir_a_tienda(e):
        await page.push_route("/tienda")

    async def ir_a_anuncios(e):
        await page.push_route("/anuncios")

    async def volver_al_inicio(e):
        await page.push_route("/")

    #En la funcion solo reconstruimos la lista de vistas.
    def route_change(e):
        page.views.clear()  # 1) Empezamos limpiando la pila completa
        #la vista raiz siempre existe "/"

        page.views.append(
            ft.View(
                route="/", #Vista raiz
                controls=[
                    ft.AppBar(title=ft.Text("Inicio")),
                    ft.Text("Estamos en la ruta raiz"),
                    ft.ElevatedButton("Ir a la tienda", on_click=ir_a_tienda),
                    ft.ElevatedButton("Ir a anuncios", on_click=ir_a_anuncios),
                ],
            )
        )

        # 3) Si la ruta actual es "/tienda", añadimos esa vista encima
        if page.route == "/tienda":
            page.views.append(
                ft.View(
                    route="/tienda",
                    controls=[
                        ft.AppBar(title=ft.Text("Tienda")),
                        ft.Text("Eatamos en la tienda",weight=ft.FontWeight.BOLD,size=30),
                        ft.ElevatedButton("Estamos Volver al inicio", on_click=volver_al_inicio),
                    ],
                )
            )
        # Y si la ruta actual es "/anuncios"
        elif page.route == "/anuncios":
            page.views.append(
                ft.View(
                    route="/anuncios",
                    controls=[
                        ft.AppBar(title=ft.Text("Anuncios")),
                        ft.Text("Estamos en los anuncios", weight=ft.FontWeight.BOLD, size=30),
                        #ft.ElevatedButton("Volver al inicio", on_click=volver_al_inicio),
                    ],
                )
            )
        page.update()

    #Esta función se ejecuta automáticamente cuando el usuario pulsa la flecha de "Atrás" que Flet dibuja
    async def view_pop(e):
        # Se ejecuta cuando el usuario pulsa el botón "Atrás" del AppBar
        # e.view es la vista concreta que se cerró (no siempre es "la última de la lista")
        if e.view is not None:
            page.views.remove(e.view)  # eliminamos exactamente vista que aparece en el evento como atributo
            top_view = page.views[-1]  # Nueva última vista
            await page.push_route(top_view.route)

    page.on_route_change = route_change  # Le decimos a Flet: "cada vez que cambie la ruta, llama a esta función". Es una asignación, no una llamada
    page.on_view_pop = view_pop
    route_change(None)  # Para forzar la primera construcción de page.views (ya no usamos page.go, que está deprecado)


ft.run(main)