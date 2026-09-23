
#Opción B · Parámetro como "query string"

import flet as ft 
from urllib.parse import urlparse, parse_qs

def main(page:ft.Page):

    async def ir_al_detalle(e):
        await page.push_route("https://www.ejemplo.com/detalle?usuario=Antonio_eson")

    vista_inicio = ft.View(
            route="/",
            controls=[
                ft.AppBar(ft.Text("INICIO",size=30)),
                ft.Text("Estas en el inio"),
                ft.ElevatedButton("Detalla",on_click=ir_al_detalle)
                ])
    
     #funcion cotructora de vistas
    def route_change(e):
        page.views.clear()
        page.views.append(vista_inicio)


        ruta = urlparse(page.route) #descompone la ruta en sus componentes (path, query, etc.)
    #print(ruta.scheme)   # https
    #print(ruta.netloc)   # www.ejemplo.com
    #print(ruta.path)     # /detalle
    #print(ruta.query)    # usuario=ana&edad=30
    #print(ruta.fragment) # seccion1

        if ruta.path =="/detalle":
            consultas = parse_qs(ruta.query) #Toma la cadena de consulta (query string, la parte después del ?), entrega un diccionario con los parámetros y sus valores
            usuario = consultas.get("usuario", ["?"])[0] #obtiene el valor del parámetro "id" o "?" si no existe
            edad = consultas.get("edad", ["?"])[0] #obtiene el valor del parámetro "edad" o "?" si no existe
            seccion = consultas.get("seccion", [""])[0] #obtiene el valor del fragmento (después del #) o "" si no existe

            #mostrar parametros extraidos
            page.views.append(
                ft.View(
                    route=page.route,
                    controls=[
                        ft.AppBar(title=ft.Text("Detalle")), 
                        ft.Text(f"Usuario: {usuario}"),
                        ft.Text(f"Edad: {edad}"),
                        ft.Text(f"Sección: {seccion}")
                    ]

                )
            )
        page.update()

    async def view_pop(e):
        if len(page.views) > 1:
            page.views.remove(e.view)
            vista_actual = page.views[-1]
            await page.push_route(vista_actual.route)

          
    page.on_route_change = route_change # cuando se cambia la ruta, se ejecuta la función route_change
    page.on_view_pop = view_pop # cuando se cierra una vista, se ejecuta la función view_pop
    route_change(None)


ft.run(main)