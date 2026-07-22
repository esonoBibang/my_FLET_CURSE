
import flet as ft
import re

def main(page:ft.Page):
    page.title = "Formulario"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLUE_GREY_800


    login = ft.Text("REGISTRATE",weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE, size=34,italic=True)


    def validar(e):
        print("Validando formulario...")
        
        # Lista de los campos que queremos validar
        campos = [name, apellido, password, email, country]

        #verificamos los campos vacios
        for campo in campos:
            if not campo.value or campo.value.strip() == "":
                campo.error = "Este campo es obligatorio"
            
            else:
                campo.error = None

        if not country.value:
            country.error_text = "Este campo es obligatorio"
        else:
            country.error_text = None

        #validar la contraseña
        valor = password.value.strip() #checking if the password is empty or has only whitespace characters

        if not valor:
            password.error = "La contraseña es obligatoria"

        elif len(valor) < 8:
            password.error = "Debe tener al menos 8 caracteres"

        elif not re.search(r"[A-Z]", valor):#looking for at least one uppercase letter in the password
            password.error = "Debe contener al menos una letra mayúscula"

        elif not re.search(r"[a-z]", valor):#looking for at least one lowercase letter in the password
            password.error = "Debe contener al menos una letra minúscula"

        elif not re.search(r"[0-9]", valor):#looking for at least one number in the password
            password.error = "Debe contener al menos un número"

        elif not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\];'`~]", valor):#looking for at least one special character in the password
            password.error = "Debe contener al menos un carácter especial"

        else:
            password.error = None


        #validar el mail
        valor_email = email.value.strip() #checking if the email is empty or has only whitespace characters
        if valor_email:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email.value):
                email.error = "Formato de email inválido"
            else:
                email.error = None
        else:
            email.error = "El email es obligatorio"

        page.update() #update the page to reflect the changes made to the error messages



    #Create the controls for the form
    name = ft.TextField(value = "",label="Name",width=400)

    apellido = ft.TextField(value="",label="Apellidos",width=400)

    password = ft.TextField(
        label="Contraseña",
        can_reveal_password=True,
        password=True,
        width=400)
    
    email = ft.TextField(value="",label="email",width=400)

    country = ft.Dropdown(
    label="Pais",
    width=400,
    options=[
        ft.dropdown.Option(key="es", text="España"),
        ft.dropdown.Option(key="fr", text="Francia"),
        ft.dropdown.Option(key="it", text="Italia"),
        ft.dropdown.Option(key="pt", text="Portugal"),
        ft.dropdown.Option(key="dz", text="Argelia"),
        ft.dropdown.Option(key="ao", text="Angola"),
        ft.dropdown.Option(key="bj", text="Benín"),
        ft.dropdown.Option(key="bw", text="Botsuana"),
        ft.dropdown.Option(key="bf", text="Burkina Faso"),
        ft.dropdown.Option(key="bi", text="Burundi"),
        ft.dropdown.Option(key="cv", text="Cabo Verde"),
        ft.dropdown.Option(key="cm", text="Camerún"),
        ft.dropdown.Option(key="td", text="Chad"),
        ft.dropdown.Option(key="km", text="Comoras"),
        ft.dropdown.Option(key="cg", text="Congo"),
        ft.dropdown.Option(key="cd", text="Congo (RD)"),
        ft.dropdown.Option(key="ci", text="Costa de Marfil"),
        ft.dropdown.Option(key="dj", text="Yibuti"),
        ft.dropdown.Option(key="eg", text="Egipto"),
        ft.dropdown.Option(key="sz", text="Esuatini"),
        ft.dropdown.Option(key="et", text="Etiopía"),
        ft.dropdown.Option(key="ga", text="Gabón"),
        ft.dropdown.Option(key="gm", text="Gambia"),
        ft.dropdown.Option(key="gh", text="Ghana"),
        ft.dropdown.Option(key="gn", text="Guinea"),
        ft.dropdown.Option(key="gw", text="Guinea-Bisáu"),
        ft.dropdown.Option(key="gq", text="Guinea Ecuatorial"),
        ft.dropdown.Option(key="ke", text="Kenia"),
        ft.dropdown.Option(key="ls", text="Lesoto"),
        ft.dropdown.Option(key="lr", text="Liberia"),
        ft.dropdown.Option(key="ly", text="Libia"),
        ft.dropdown.Option(key="mg", text="Madagascar"),
        ft.dropdown.Option(key="mw", text="Malaui"),
        ft.dropdown.Option(key="ml", text="Malí"),
        ft.dropdown.Option(key="ma", text="Marruecos"),
        ft.dropdown.Option(key="mu", text="Mauricio"),
        ft.dropdown.Option(key="mr", text="Mauritania"),
        ft.dropdown.Option(key="mz", text="Mozambique"),
        ft.dropdown.Option(key="na", text="Namibia"),
        ft.dropdown.Option(key="ne", text="Níger"),
        ft.dropdown.Option(key="ng", text="Nigeria"),
        ft.dropdown.Option(key="rw", text="Ruanda"),
        ft.dropdown.Option(key="st", text="Santo Tomé y Príncipe"),
        ft.dropdown.Option(key="sn", text="Senegal"),
        ft.dropdown.Option(key="sc", text="Seychelles"),
        ft.dropdown.Option(key="sl", text="Sierra Leona"),
        ft.dropdown.Option(key="so", text="Somalia"),
        ft.dropdown.Option(key="za", text="Sudáfrica"),
        ft.dropdown.Option(key="sd", text="Sudán"),
        ft.dropdown.Option(key="ss", text="Sudán del Sur"),
        ft.dropdown.Option(key="tz", text="Tanzania"),
        ft.dropdown.Option(key="tg", text="Togo"),
        ft.dropdown.Option(key="tn", text="Túnez"),
        ft.dropdown.Option(key="ug", text="Uganda"),
        ft.dropdown.Option(key="zm", text="Zambia"),
        ft.dropdown.Option(key="zw", text="Zimbabue"),])

    radio_group = ft.RadioGroup(
        content=ft.Row([ft.Radio(value="M", label="Masculino"),
                        ft.Radio(value="F", label="Femenino")]))

    chekbox = ft.Checkbox(label="Acepto los términos y condiciones", value=False)

    button_send = ft.ElevatedButton("Enviar", on_click=validar)

    #put  the controls in a container
    contenedor = ft.Container(
        content= ft.Column(
            [name,apellido,password,email,country,button_send,radio_group,chekbox],
            spacing=10,
        ),
        width=500,
        height=800,
        border_radius=20,
        padding=10,
        alignment = ft.Alignment.CENTER,
        )

  
    
    #Mostrar los elementos en pantalla
    page.add(login,contenedor)

ft.run(main)