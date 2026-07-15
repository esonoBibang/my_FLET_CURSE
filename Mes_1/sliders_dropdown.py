"""Sliders y Dropdown.
Ejemplo de selección de valores numéricos y de listas desplegables con retroalimentación en tiempo real."""
import flet as ft

def main(page:ft.Page):
    page.title = "Sliders y Dropdown"
    page.padding = 200

    text_slider = ft.Text("Volum 0.1")
    text_dropdown = ft.Text("Pais seleccionado: Ninguno")

    def al_cambiar_slider(e):
        text_slider.value = f"Volum {float(e.control.value)}"
        page.update()

    slider = ft.Slider(
        min=0,
        max=5.0,
        value=0.1,
        divisions=50,
        label="{value}",
        inactive_color="black",
        active_color="green",
        width=200,
        on_change=al_cambiar_slider)

    def al_cambiar_dropdown(e):
        text_dropdown.value = f"País seleccionado: {e.control.value}"
        page.update()

    dropdown = ft.Dropdown(
        label="País",
        width=250,
        options=[
            ft.DropdownOption(key="QG", text="Guinea Ecuatorial"),
            ft.DropdownOption(key="Es", text="España"),
            ft.DropdownOption(key="Méx", text="México"),
            ft.DropdownOption(key="Arg", text="Argentina"),
        ],
        on_select=al_cambiar_dropdown)

    page.add(
        text_slider,
        slider,
        ft.Divider(),
        text_dropdown,
        dropdown,
    )

ft.run(main)