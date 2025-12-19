import flet as ft

def main(page: ft.Page):
    #Titulo de la pag por defecto
    page.title = "Memoriza Y Aprende"
    page.bgcolor = "#232376"
    #Alinenado 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

#Aqui estamos creando unavariable tipo texto por eso el ft Text
    titulo = ft.Text(
        "¡Memoriza Y Aprende!",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#df6b16",
        text_align=ft.TextAlign.CENTER,
    )

#Aqui estamos creando unavariable tipo texto por eso el ft Text
    descripcion = ft.Text(
        "En este juego aprenderás a tu ritmo palabras en inglés de manera divertida "
        "y rápida el significado y traducción español-inglés de algunas palabras.",
        size=20,
        text_align=ft.TextAlign.CENTER,
        color="#232376",
    )

    btn_empezar = ft.ElevatedButton(
        "EMPEZAR",
        width=200,
        height=50,
        bgcolor="#f88633",
        color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
    )

    btn_tutorial = ft.ElevatedButton(
        "TUTORIAL",
        width=200,
        height=50,
        bgcolor="#232376",
        color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
    )

    contenido =  ft.Column(
            [
                titulo,
                ft.Divider(height=20, color="transparent"),
                
                ft.Container(
                    content=descripcion,
                    alignment=ft.alignment.center,
                    width=900,
                    height=60,
                ),
                ft.Divider(height=40, color="transparent"),
                #Centrando los botones con .Row
                ft.Row(
                    [
                    btn_empezar,
                    btn_tutorial,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER, #Esta linea me ayuda a centrar el contenido(en este caso los botones)
                ),
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
#IMPORTANTE
    page.add(
        ft.Container(
                    content=contenido,
                    alignment=ft.alignment.center,
                    height=400,
                    bgcolor="#f0f0f0"
                ),
            )

ft.app(target=main)

#ft.Divider(width=10, color="transparent"),

