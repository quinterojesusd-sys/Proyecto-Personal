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

# Cargar en lista de datos (memoria) todos los datos (listas, diccionarios). Actualizar el puntaje, sobreescribir en Json.
