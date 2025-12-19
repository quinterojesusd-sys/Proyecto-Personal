import json

def guardar_usuario(nombre, puntaje):
    datos = {"nombre": nombre, "puntaje": puntaje}
    
    try:
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        usuarios = []
    
    usuarios.append(datos)
    
    with open("usuarios.json", "w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, indent=4, ensure_ascii=False)

# Ejemplo de uso
usuario = input("Ingresa tu nombre: ")
puntaje = 15
guardar_usuario(usuario, puntaje)
