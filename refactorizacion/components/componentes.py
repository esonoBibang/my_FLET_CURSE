#COMPONENTES REUTILIZABLES


import flet as ft
from models.matricula_alumno import alumno,profesor,informacion




def boton_matricular():
    return ft.Button("Matricular", on_click=alumno)

def boton_profesor():
    return ft.Button("Profesor", on_click=profesor)

def boton_informacion():
    return ft.Button("Informacion del Alumno", on_click=informacion)

