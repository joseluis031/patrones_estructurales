# main.py

from proxi import *
import json
import getpass
from usuario2 import *

# Solicitar al usuario que elija entre registrarse e iniciar sesión
opcion = input("¿Desea registrarse (r) o iniciar sesión (i)? ").lower()

if opcion == 'r':
    # Registrarse
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")  # Utilizar getpass para ocultar la contraseña
    nuevo_usuario = Usuario(nombre_usuario, contraseña)
    nuevo_usuario.guardar_en_csv("Ejercicio Proxi/usuarios.csv")

elif opcion == 'i':
    # Iniciar sesión
    nombre_usuario_buscar = input("Ingrese su nombre de usuario: ")
    contraseña_buscar = getpass.getpass("Ingrese su contraseña: ")

    # Buscar un usuario en el archivo CSV con nombre de usuario y contraseña
    if Usuario.buscar_en_csv("Ejercicio Proxi/usuarios.csv", nombre_usuario_buscar, contraseña_buscar):
        # Usuario autenticado, crear Proxy y acceder a la estructura
        carpeta_principal = Carpeta("Secundaria")
        documento1 = Documentos_Leaf("Documento1", "Texto", 10)
        documento2 = Documentos_Leaf("Documento2", "Imagen", 20)
        enlace1 = Enlace_Leaf("Enlace1", "http://enlace1.com")
        proxy_documento1 = Proxy(documento1, usuario_actual=nombre_usuario_buscar)
        proxy_documento1.operation()

        carpeta_principal.add(documento1)
        carpeta_principal.add(documento2)
        carpeta_principal.add(enlace1)
        carpeta_principal.add(proxy_documento1)

        # Convertir la estructura a JSON
        estructura_json = carpeta_principal.to_dict()
        with open("Ejercicio Proxi/basedatos.json", "w") as json_file:
            json.dump(estructura_json, json_file, indent=2)

else:
    print("Opción no válida. Por favor, seleccione 'r' para registrarse o 'i' para iniciar sesión.")
