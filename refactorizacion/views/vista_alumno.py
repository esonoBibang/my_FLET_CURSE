#VISTA DE INSCRIPCION DEL ALUMNO

import flet as ft
from dataclasses import dataclass

#la clase Alumno para almacenar la información del alumno
@dataclass
class Alumno:
    nombre: str = ""
    apellido: str = ""
    curso_clave: str = ""
    curso: str = ""
    nivel: str = ""   # "ESBA" o "BACHILLERATO"

alumno_actual = Alumno() #objeto global para almacenar la información del alumno actual

def formulario_alumno():

    cursos = {
            "pe":"primero esba",
              "se":"Segundo esba",
              "te":"Tercero esba",
              "ce":"Cuarto esba",
              "pb":"Primero Bach",
              "sb":"Segundo Bach"
            }
    nombre = ft.TextField(label="Nombre")
    apellido = ft.TextField(label="Apellido")
    informacion_curso = ft.Text("")
    mensaje = ft.Text("")

    def curso_seleccionado(e):
        clave = e.control.value
        if clave in ["pe", "se", "te", "ce"]:
            informacion_curso.value = "Alumno de la ESBA"
        elif clave in ["pb", "sb"]:
            informacion_curso.value = "Alumno del BACHILLERATO"      
        else:
            informacion_curso.value = ""

        informacion_curso.update()

    curso =ft.Dropdown(
        label="Cursos",
        width=250,
        options=[ft.DropdownOption(key=key, text=value) for key, value in cursos.items()],
        on_select=curso_seleccionado
    )

    def guardar(e):
        # Validación básica
        if not nombre.value or not apellido.value or not curso.value:
            mensaje.value = "Completa todos los campos"
            mensaje.color = ft.Colors.RED
            mensaje.update()
            return

        # Guardar los datos
        alumno_actual.nombre = nombre.value.strip()
        alumno_actual.apellido = apellido.value.strip()
        alumno_actual.curso_clave = curso.value
        alumno_actual.curso = cursos[curso.value]
        alumno_actual.nivel = "ESBA" if curso.value in ["pe", "se", "te", "ce"] else "BACHILLERATO"

        mensaje.value = "Datos guardados"
        mensaje.color = ft.Colors.GREEN
        mensaje.update()

    boton_guardar = ft.Button("Guardar", on_click=guardar)

    return ft.Column(controls=[nombre, apellido,curso, informacion_curso, boton_guardar, mensaje])



def formulario_profesor():

    nombre = ft.TextField(label="Nombre")

    apellido = ft.TextField(label="Apellido")

    materia = ft.TextField(label="Materia")

    años_experiencia = ft.TextField(label="Años de experiencia",keyboard_type=ft.KeyboardType.NUMBER)# especificar el tipo de teclado para que solo acepte números

    return ft.Column(controls=[nombre, apellido, materia, años_experiencia])




 