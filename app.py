import flet as ft

def main(page: ft.Page):
    page.title = "Memoriza Y Aprende"
    page.bgcolor = "#f0f0f0"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    titulo = ft.Text(
        "Memoriza Y Aprende",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#df6b16",
        text_align=ft.TextAlign.CENTER,
    )

    descripcion = ft.Text(
        "En este juego aprenderás a tu ritmo palabras en inglés de manera divertida "
        "y rápida el significado y traducción español - inglés de algunas palabras.",
        size=18,
        text_align=ft.TextAlign.CENTER,
        color="#232376",
    )

    btn_empezar = ft.ElevatedButton(
        "Empezar",
        width=200,
        height=50,
        bgcolor="#4CAF50",
        color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
    )

    btn_tutorial = ft.ElevatedButton(
        "Tutorial",
        width=200,
        height=50,
        bgcolor="#2196F3",
        color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
    )

    page.add(
        ft.Column(
            [
                titulo,
                ft.Divider(height=20, color="transparent"),
                descripcion,
                ft.Divider(height=40, color="transparent"),
                btn_empezar,
                ft.Divider(height=10, color="transparent"),
                btn_tutorial,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)

