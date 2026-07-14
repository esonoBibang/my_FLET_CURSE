"""Manejo de múltiples controles de selección con sus respectivos eventos on_change."""

import flet as ft
from flet.controls.material import radio_group


def main(page:ft.Page):
    page.title = "Checkbox, Switch y Radio"
    page.padding = 20
    resumen = ft.Text(size=16)

    # --- Checkboxes ---
    check_python = ft.Checkbox(label="Python", value=False)
    check_flet = ft.Checkbox(label="Flet", value=False)
    check_sql = ft.Checkbox(label="SQL", value=False)

    def al_cambiar_checkbox(e):

        seleccionados = []
        #erificamos si los checkbox son seleccionados
        if check_python.value: seleccionados.append("Python")

        if check_flet.value: seleccionados.append("Flet")

        if check_sql.value: seleccionados.append("SQL")

        resumen.value = f"Lenguajes seleccionados: {', '.join(seleccionados) if seleccionados else 'Ninguno'}"
        page.update() #Guardar y Aplicar cambios

    for c in (check_python, check_flet, check_sql):
        c.on_change = al_cambiar_checkbox


    #------------------Switch---------------------
    switch_theme = ft.Switch(label="Change mode",value=True)

    def al_cambiar_switch(e):
        page.theme_mode = ft.ThemeMode.DARK if switch_theme.value else ft.ThemeMode.LIGHT
        page.update() #Guardar y Aplicar cambios

    switch_theme.on_change = al_cambiar_switch

    #-----------RadioGroup---------------------
    def al_cambiar_radio(e):
        resumen.value = f"Nivel seleccionado: {radio_group.value}"
        page.update() #Guardar y Aplicar cambios

    radio_group = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="principiante", label="Principiante",),
            ft.Radio(value="intermedio", label="Intermedio"),
            ft.Radio(value="avanzado", label="Avanzado"),
        ]),
        on_change=al_cambiar_radio #Comando que detecta el cambio
    )

    page.add(
        ft.Text("Lenguajes:", weight=ft.FontWeight.BOLD),
        check_python, check_flet, check_sql,
        ft.Divider(), #A thin horizontal line (divider), with padding on either side.
        switch_theme,
        ft.Divider(),#A thin horizontal line (divider), with padding on either side.
        ft.Text("Nivel de experiencia:", weight=ft.FontWeight.BOLD),
        radio_group,
        ft.Divider(),#A thin horizontal line (divider), with padding on either side.
        resumen
    )


ft.run(main)