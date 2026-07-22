import flet as ft
def main(page: ft.Page):
    page.title = "Formulario de Registro - Semana 2"
    page.padding = 30
    page.window.width = 420
    # Controles de entrada

    nombre = ft.TextField(label="Nombre completo", width=350)
    edad = ft.TextField(label="Edad", width=350, keyboard_type=ft.KeyboardType.NUMBER)
    genero = ft.RadioGroup(
        content=ft.Row([
        ft.Radio(value="M", label="Masculino"),
        ft.Radio(value="F", label="Femenino"),
        ])
        )
    pais = ft.Dropdown(
        label="País",
        width=350,
        options=[
        ft.DropdownOption(key="Guinea Ecuatorial", text="Guinea Ecuatorial"),
        ft.DropdownOption(key="España", text="España"),
        ft.DropdownOption(key="Otro", text="Otro"),
        ]
        )
    acepta_terminos = ft.Checkbox(label="Acepto los términos y condiciones", value=False)

    recibir_noticias = ft.Switch(label="Recibir notificaciones", value=True)

    satisfaccion = ft.Slider(min=0, max=10, divisions=10, label="{value}", value=5)

    resultado = ft.Text(value="", size=14, color=ft.Colors.GREEN_700)

    def enviar_formulario(e):
        if not nombre.value or not edad.value:
            resultado.value = "⚠ Completa nombre y edad."
            resultado.color = ft.Colors.RED
            page.update()
            return
        if not acepta_terminos.value:
            resultado.value = "⚠ Debes aceptar los términos."
            resultado.color = ft.Colors.RED
            page.update()
            return
    resumen = (
        f"✅ Registro exitoso\n"
        f"Nombre: {nombre.value}\n"
        f"Edad: {edad.value}\n"
        f"Género: {genero.value}\n"
        f"País: {pais.value}\n"
        f"Notificaciones: {'Sí' if recibir_noticias.value else 'No'}\n"
        f"Satisfacción: {int(satisfaccion.value)}/10"
        )
    resultado.value = resumen
    resultado.color = ft.Colors.GREEN_700
    page.update()
    boton_enviar = ft.ElevatedButton(
    content="Registrarse",
    icon=ft.Icons.CHECK_CIRCLE,
    on_click=enviar_formulario
    )
    page.add(
        ft.Text("Formulario de Registro", size=22, weight=ft.FontWeight.BOLD),
        nombre,
        edad,
        ft.Text("Género:"),
        genero,
        pais,
        acepta_terminos,
        recibir_noticias,
        ft.Text("Nivel de satisfacción esperado:"),
        satisfaccion,
        boton_enviar,
        ft.Divider(),
        resultado
        )
ft.run(main)