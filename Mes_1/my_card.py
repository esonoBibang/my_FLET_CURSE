import flet as ft

def main(page: ft.Page):
    page.padding = 20
    page.bgcolor = ft.Colors.GREY_100
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    card = ft.Card(
        elevation=20,
        bgcolor=ft.Colors.BLACK,

        content=ft.Container(
            width=350,
            height=250,
            padding=10,

            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Image(src=r"D:\my_FLET_CURSE\Mes_1\picture.jpg",width=100,height=100),
                            ft.Container(
                                content=ft.Column(
                                    controls=[ft.Text("Antonio Esono Bibang Andeme"),ft.Text("Ing técnico Electronica")]
                                )
                            )
                        ]
                    ),
                    ft.Divider(thickness=2,color=ft.Colors.WHITE),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Cliente registrado"),
                                ft.Icon(ft.Icons.CHECK_CIRCLE_OUTLINE,color=ft.Colors.GREEN)]
                        ),
                        alignment=ft.Alignment.BOTTOM_CENTER,

                    )
                ],spacing=10
            )
        )
    )



    
    page.add(card)

ft.run(main)