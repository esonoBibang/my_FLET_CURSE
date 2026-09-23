
#Navegación con parámetros en la ruta
#Opción A · Parámetro dentro de la propia ruta


import flet as ft

def main(page:ft.Page):
    page.title ="Navegación con parámetros en la ruta"

    async def ventas(e):
        await page.push_route("ventas")

    async def compras(e):
        await page.push_route("compras")

    async def compras_item(e):
        await page.push_route("/compras/1")  # Navegar a la ruta con el parámetro

    async def ventas_item(e):
        await page.push_route("/ventas/1")  # Navegar a la ruta con el parámetro

    #Funcion que construye las vistas
    def rout_change(e):
        page.views.clear()

        #vista principal
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.AppBar(title=ft.Text("Vista principal")),
                    ft.Text("Estas en la vista principal",color=ft.Colors.WHITE,size=30),
                    ft.Row([
                        ft.ElevatedButton("VENTAS",on_click=ventas),
                        ft.ElevatedButton("COMPRAS",on_click=compras),
                        ft.ElevatedButton("ID_compra",on_click=compras_item),
                        ft.ElevatedButton("ID_ventas", on_click=ventas_item)])
                    ])
                )
    

        if page.route == "ventas":
            page.views.append(
                ft.View(
                    route="ventas",
                    controls=[
                        ft.AppBar(title=ft.Text("Vista ventas")),
                        ft.Text("Estas en ventas",color=ft.Colors.WHITE,size=30),
                    ]
                )
            )

        elif page.route == "compras":
            page.views.append(
                ft.View(
                    route ="compras",
                    controls = [
                        ft.AppBar(title=ft.Text("Vista compras")), 
                        ft.Text("Estas en compras",color=ft.Colors.WHITE,size=30)]
                )
            )

        elif page.route.startswith("/compras/"):
            partes = page.route.split("/")
            item_id = partes[2]  # Obtener el ID de la vista de compras desde la ruta

            page.views.append(
                ft.View(
                    route="Id de compras",
                    controls=[
                        ft.AppBar(title=ft.Text(f"Vista compras - Item {item_id}")),
                        ft.Text(f"Estas en compras - Item {item_id}", color=ft.Colors.WHITE, size=30),
                    ]
                )
            )

        elif page.route.startswith("/ventas/"):
            partes = page.route.split("/")
            item_id = partes[2]  # Obtener el ID de la vista de ventas desde la ruta

            page.views.append(
                ft.View(
                    route="Id de ventas",
                    controls=[
                        ft.AppBar(title=ft.Text(f"Vista ventas - Item {item_id}")),
                        ft.Text(f"Estas en ventas - Item {item_id}", color=ft.Colors.WHITE, size=30),
                    ]
                )
            )

    #funcion que hace retroceder a la vista anterior
    async def pop_view(e):

        if e.view is not None:

            page.views.remove(e.view) #eliminar la vista actual
            nueva_vista = page.views[-1] #obtener la vista anterior
            await page.push_route(nueva_vista.route)


    page.on_route_change = rout_change
    page.on_view_pop = pop_view
    rout_change(None)
    

ft.run(main)