import flet as ft 

def main(page:ft.Page):
    page.title ="The Stack"
    page.padding = 20

    stack = ft.Stack(
        width=300,
        height= 200,
        controls=[

            ft.Container(
                content=ft.Text("ONE"),
                width =100,
                height = 100,
                bgcolor=ft.Colors.RED_300,
                border_radius =15,
                padding=10
                  ),

            ft.Container(
                content=ft.Text("New"),
                width =100,
                height = 100,
                bgcolor=ft.Colors.BLUE_300,
                border_radius =15,
                top=10,
                right=10,
                padding=10
                ),

            ft.Container(
                content=ft.Icon(ft.Icons.FAVORITE,color=ft.Colors.WHITE),
                width =100,
                height = 100,
                bgcolor=ft.Colors.with_opacity(0.4,ft.Colors.BLUE_300),
                border_radius =15,
                padding =8,
                bottom=10,
                left=10
                )]
                )

    page.add(stack)


ft.run(main)