# main.py

from proxi import *
import json
import getpass
from usuario2 import *
from añadir_carpeta import *
from borrar import *
from editar import *

from interfaz import *

# Solicitar al usuario que elija entre registrarse e iniciar sesión
# main.py

# ... (código anterior)

opcion = input("¿Desea registrarse (r) o iniciar sesión (i)? ").lower()

if opcion == 'r':
    # Registrarse
    registrar_usuario()
elif opcion == 'i':
    # Iniciar sesión
    if iniciar_sesion():
        # Usuario autenticado, cargar estructura y realizar operaciones
        carpeta_principal = Carpeta("Principal")
        cargar_estructura_desde_json(carpeta_principal, json.load(open("Ejercicio Proxi/basedatos.json")))
        realizar_operacion("usuario_actual", carpeta_principal)
else:
    print("Opción no válida. Por favor, seleccione 'r' para registrarse o 'i' para iniciar sesión.")