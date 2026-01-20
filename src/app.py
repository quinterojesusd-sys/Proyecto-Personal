import flet as ft
import json
import random
import os

def guardar_puntaje(nombre, puntos):
    nombre_estandar = nombre.lower()
    nuevo_registro = {"nombre": nombre_estandar, "puntos": puntos}
    lista_usuarios = []

    if os.path.exists("usuarios.json"):
        try:
            with open("usuarios.json", "r", encoding="utf-8") as f:
                lista_usuarios = json.load(f)
        except:
            lista_usuarios = []

    lista_usuarios.append(nuevo_registro)

    try:
        with open("usuarios.json", "w", encoding="utf-8") as f:
            json.dump(lista_usuarios, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error guardando: {e}")

def obtener_datos_usuario(nombre):
    nombre_estandar = nombre.lower()
    total_puntos = 0
    partidas = 0
    if os.path.exists("usuarios.json"):
        try:
            with open("usuarios.json", "r", encoding="utf-8") as f:
                datos = json.load(f)
                for registro in datos:
                    if registro.get("nombre", "").lower() == nombre_estandar:
                        total_puntos += registro.get("puntos", 0)
                        partidas += 1
        except:
            pass
    return total_puntos, partidas

def main(page: ft.Page):
    page.title = "Aprende Inglés"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 700

    usuario_actual = ""
    score = 0
    round_index = 0
    quiz_words = []
    
    lista_palabras_cargadas = []

    titulo = ft.Text("Aprende Inglés", size=30, weight=ft.FontWeight.BOLD)
    area_contenido = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    page.add(titulo, area_contenido)

    def cargar_palabras_json():
        nonlocal lista_palabras_cargadas
        try:
            with open("words.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            facil = data.get("easy", [])
            medio = data.get("medium", [])
            dificil = data.get("hard", [])
            
            lista_palabras_cargadas = facil + medio + dificil
            return True
        except Exception as e:
            return False

    def mostrar_login():
        area_contenido.controls.clear()
        
        exito = cargar_palabras_json()
        if not exito:
            area_contenido.controls.append(ft.Text("❌ Error: No se encontró words.json", color="red", size=20))
            page.update()
            return

        campo_nombre = ft.TextField(
            label="Escribe tu nombre", 
            width=280, 
            text_align=ft.TextAlign.CENTER
        )

        def intentar_entrar(e):
            nonlocal usuario_actual
            if not campo_nombre.value:
                campo_nombre.error_text = "¡El nombre es obligatorio!"
                page.update()
                return
            
            usuario_actual = campo_nombre.value
            mostrar_menu()

        btn_entrar = ft.ElevatedButton(
            content=ft.Text("COMENZAR"),
            width=200,
            on_click=intentar_entrar
        )

        area_contenido.controls.append(ft.Text("¡Bienvenido!", size=24))
        area_contenido.controls.append(campo_nombre)
        area_contenido.controls.append(ft.Container(height=10))
        area_contenido.controls.append(btn_entrar)
        page.update()

    def mostrar_menu():
        area_contenido.controls.clear()
        
        total, jugadas = obtener_datos_usuario(usuario_actual)

        info_usuario = ft.Container(
            content=ft.Column([
                ft.Text(f"👤 Jugador: {usuario_actual}", size=18, weight=ft.FontWeight.BOLD),
                ft.Text(f"🏆 Puntos totales: {total}"),
                ft.Text(f"🎮 Partidas jugadas: {jugadas}")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            border=ft.border.all(1, ft.Colors.BLUE_200),
            border_radius=10,
            bgcolor=ft.Colors.BLUE_50
        )

        btn_quiz = ft.ElevatedButton(
            content=ft.Text("🧠 Jugar Quiz"),
            width=250,
            on_click=lambda e: iniciar_quiz()
        )

        btn_practica = ft.ElevatedButton(
            content=ft.Text("📖 Modo Práctica"),
            width=250,
            on_click=lambda e: iniciar_practica()
        )

        btn_salir = ft.TextButton(
            content=ft.Text("Cerrar Sesión"),
            on_click=lambda e: mostrar_login()
        )

        area_contenido.controls.append(info_usuario)
        area_contenido.controls.append(ft.Container(height=20))
        area_contenido.controls.append(btn_quiz)
        area_contenido.controls.append(btn_practica)
        area_contenido.controls.append(btn_salir)
        page.update()

    def iniciar_quiz():
        nonlocal score, round_index, quiz_words
        score = 0
        round_index = 0
        
        if not lista_palabras_cargadas:
             area_contenido.controls.append(ft.Text("Error: Lista de palabras vacía"))
             page.update()
             return

        quiz_words = lista_palabras_cargadas.copy()
        random.shuffle(quiz_words)
        quiz_words = quiz_words[:10]
        
        ronda_quiz()

    def ronda_quiz():
        nonlocal round_index, score
        area_contenido.controls.clear()

        if round_index >= len(quiz_words):
            guardar_puntaje(usuario_actual, score)
            
            area_contenido.controls.append(ft.Text("🎉 ¡Terminaste!", size=30))
            area_contenido.controls.append(ft.Text(f"Puntaje: {score}/{len(quiz_words)}", size=25, weight=ft.FontWeight.BOLD))
            area_contenido.controls.append(ft.Text("✅ Puntos guardados", color="green"))
            
            btn_volver = ft.ElevatedButton(
                content=ft.Text("Volver al Menú"),
                on_click=lambda e: mostrar_menu()
            )
            area_contenido.controls.append(ft.Container(height=20))
            area_contenido.controls.append(btn_volver)
            page.update()
            return

        palabra_actual = quiz_words[round_index]
        correcta = palabra_actual["spanish"]

        otras = [w["spanish"] for w in lista_palabras_cargadas if w["spanish"] != correcta]
        
        cantidad_opciones = min(3, len(otras))
        malas = random.sample(otras, cantidad_opciones)
        
        opciones = malas + [correcta]
        random.shuffle(opciones)

        txt_pregunta = ft.Text(f"¿Cómo se dice '{palabra_actual['english']}'?", size=22)
        txt_resultado = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
        columna_botones = ft.Column(spacing=10)

        def verificar_respuesta(e):
            nonlocal score
            respuesta_elegida = e.control.data 
            
            if respuesta_elegida == correcta:
                score += 1
                txt_resultado.value = "✅ ¡Correcto!"
                txt_resultado.color = ft.Colors.GREEN
            else:
                txt_resultado.value = f"❌ Mal. Era: {correcta}"
                txt_resultado.color = ft.Colors.RED
            
            for btn in columna_botones.controls:
                btn.disabled = True
            
            btn_siguiente = ft.ElevatedButton(
                content=ft.Text("Siguiente ➡"),
                on_click=lambda x: avanzar_ronda()
            )
            area_contenido.controls.append(btn_siguiente)
            page.update()

        def avanzar_ronda():
            nonlocal round_index
            round_index += 1
            ronda_quiz()

        for opcion in opciones:
            btn = ft.ElevatedButton(
                content=ft.Text(opcion),
                data=opcion,
                width=250,
                on_click=verificar_respuesta
            )
            columna_botones.controls.append(btn)

        area_contenido.controls.append(ft.Text(f"Pregunta {round_index + 1} de {len(quiz_words)}"))
        area_contenido.controls.append(txt_pregunta)
        area_contenido.controls.append(ft.Container(height=10))
        area_contenido.controls.append(columna_botones)
        area_contenido.controls.append(ft.Container(height=10))
        area_contenido.controls.append(txt_resultado)
        page.update()

    def iniciar_practica():
        area_contenido.controls.clear()
        
        if not lista_palabras_cargadas:
             return

        palabra = random.choice(lista_palabras_cargadas)
        
        txt_ingles = ft.Text(palabra["english"], size=40, weight=ft.FontWeight.BOLD)
        txt_espanol = ft.Text("???", size=30, color="blue")

        def revelar(e):
            txt_espanol.value = palabra["spanish"]
            page.update()

        def siguiente(e):
            iniciar_practica()

        area_contenido.controls.append(ft.Text("Modo Práctica", size=20))
        area_contenido.controls.append(ft.Container(height=20))
        area_contenido.controls.append(txt_ingles)
        area_contenido.controls.append(txt_espanol)
        area_contenido.controls.append(ft.Container(height=20))
        
        fila_botones = ft.Row(
            controls=[
                ft.ElevatedButton(content=ft.Text("Ver Respuesta"), on_click=revelar),
                ft.ElevatedButton(content=ft.Text("Siguiente"), on_click=siguiente)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        btn_volver = ft.OutlinedButton(
            content=ft.Text("⬅ Volver al Menú"),
            on_click=lambda e: mostrar_menu()
        )

        area_contenido.controls.append(fila_botones)
        area_contenido.controls.append(ft.Container(height=20))
        area_contenido.controls.append(btn_volver)
        page.update()

    mostrar_login()

ft.app(target=main)