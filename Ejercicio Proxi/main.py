# main.py

from proxi import *
import json
import getpass
from usuario2 import *

# Solicitar al usuario que elija entre registrarse e iniciar sesión
# main.py

# ... (código anterior)

def registrar_usuario():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    nuevo_usuario = Usuario(nombre_usuario, contraseña)
    nuevo_usuario.guardar_en_csv("usuarios.csv")

def iniciar_sesion():
    nombre_usuario_buscar = input("Ingrese su nombre de usuario: ")
    contraseña_buscar = getpass.getpass("Ingrese su contraseña: ")
    return Usuario.buscar_en_csv("usuarios.csv", nombre_usuario_buscar, contraseña_buscar)

def realizar_operacion(usuario_actual, carpeta_principal):
    # ... (código anterior)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Acceder a una Carpeta (simulación)
        carpeta_principal.operation()
    elif opcion == "2":
        # Editar documento (simulación)
        print("Realizando operación específica en el documento (simulación)...")
    elif opcion == "3":
        # Añadir documento (simulación)
        nombre_documento = input("Ingrese el nombre del nuevo documento: ")
        tipo_documento = input("Ingrese el tipo de documento: ")
        tamaño_documento = int(input("Ingrese el tamaño del documento en KB: "))
        nuevo_documento = Documentos_Leaf(nombre_documento, tipo_documento, tamaño_documento)
        carpeta_principal.add(nuevo_documento)
        guardar_estructura_en_json(carpeta_principal, "basedatos.json")
        print(f"Documento '{nombre_documento}' añadido correctamente.")
    elif opcion == "4":
        # Añadir enlace (simulación)
        nombre_enlace = input("Ingrese el nombre del nuevo enlace: ")
        link_enlace = input("Ingrese el enlace: ")
        nuevo_enlace = Enlace_Leaf(nombre_enlace, link_enlace)
        carpeta_principal.add(nuevo_enlace)
        guardar_estructura_en_json(carpeta_principal, "basedatos.json")
        print(f"Enlace '{nombre_enlace}' añadido correctamente.")
    elif opcion == "5":
        # Añadir carpeta (simulación)
        nombre_carpeta = input("Ingrese el nombre de la nueva carpeta: ")
        nueva_carpeta = Carpeta(nombre_carpeta)
        carpeta_principal.add(nueva_carpeta)
        guardar_estructura_en_json(carpeta_principal, "basedatos.json")
        print(f"Carpeta '{nombre_carpeta}' añadida correctamente.")
    else:
        print("Opción no válida.")
