# archivo: app.py
# Requisitos: pip install flet

import flet as ft


def main(page: ft.Page):
    # Configuración básica de la página
    page.title = "Memoriza Y Aprende"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 24
    page.window_min_width = 360
    page.window_min_height = 500
    page.scroll = ft.ScrollMode.AUTO

    # Título
    titulo = ft.Text(
        "Memoriza Y Aprende",
        size=32,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    # Descripción
    descripcion = ft.Text(
        "En este juego aprenderás a tu ritmo palabras en inglés de manera divertida "
        "y rápida el significado y traducción español - inglés de algunas palabras.",
        size=16,
        text_align=ft.TextAlign.CENTER,
    )

    # Manejadores de eventos (puedes conectarlos a otras pantallas)
    def on_empezar_click(e: ft.ControlEvent):
        # Aquí podrías navegar a la pantalla del juego
        page.snack_bar = ft.SnackBar(ft.Text("¡Empezar! Cargando juego..."))
        page.snack_bar.open = True
        page.update()

    def on_tutorial_click(e: ft.ControlEvent):
        # Aquí podrías abrir una vista de tutorial
        page.dialog = ft.AlertDialog(
            title=ft.Text("Tutorial"),
            content=ft.Text(
                "1. Lee la palabra en inglés.\n"
                "2. Intenta recordar su significado en español.\n"
                "3. Verifica tu respuesta y repite para memorizar."
            ),
            actions=[ft.TextButton("Cerrar", on_click=lambda _: close_dialog())],
        )
        page.dialog.open = True
        page.update()

    def close_dialog():
        page.dialog.open = False
        page.update()

    # Botones
    btn_empezar = ft.ElevatedButton(
        "Empezar",
        icon=ft.Icons.PLAY_ARROW,
        on_click=on_empezar_click,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )
    btn_tutorial = ft.OutlinedButton(
        "Tutorial",
        icon=ft.Icons.SCHOOL,
        on_click=on_tutorial_click,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )

    # Layout principal centrado
    contenido = ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                ft.Divider(height=10, color="transparent"),
                descripcion,
                ft.Divider(height=20, color="transparent"),
                ft.Row(
                    controls=[btn_empezar, btn_tutorial],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=16,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )

    page.add(contenido)


if __name__ == "__main__":
    ft.app(target=main)
