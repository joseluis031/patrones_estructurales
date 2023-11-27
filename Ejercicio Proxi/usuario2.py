from proxi import *

import getpass  # Módulo para ocultar la entrada de contraseña en la consola
import csv 

class Usuario:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    def guardar_en_csv(self, archivo_csv):
        try:
            with open(archivo_csv, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.usuario, self.contraseña])
            print(f"Usuario '{self.usuario}' registrado correctamente")
        except Exception as e:
            print(f"Error al guardar en CSV: {e}")

    @staticmethod
    def buscar_en_csv(archivo_csv, usuario_buscar, contraseña_buscar):
        try:
            with open(archivo_csv, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == usuario_buscar and row[1] == contraseña_buscar:
                        print(f"Inicio de sesión exitoso para '{usuario_buscar}' ")
                        return True
            print(f"Inicio de sesión fallido para '{usuario_buscar}' o la contraseña no coincide")
            return False
        except Exception as e:
            print(f"Error al buscar en CSV: {e}")
            return False


# main.py

# ... (código anterior)

def registrar_usuario():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    nuevo_usuario = Usuario(nombre_usuario, contraseña)
    nuevo_usuario.guardar_en_csv("Ejercicio Proxi/usuarios.csv")

def iniciar_sesion():
    nombre_usuario_buscar = input("Ingrese su nombre de usuario: ")
    contraseña_buscar = getpass.getpass("Ingrese su contraseña: ")
    return Usuario.buscar_en_csv("Ejercicio Proxi/usuarios.csv", nombre_usuario_buscar, contraseña_buscar)

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
        guardar_estructura_en_json(carpeta_principal, "Ejercicio Proxi/basedatos.json")
        print(f"Documento '{nombre_documento}' añadido correctamente.")
    elif opcion == "4":
        # Añadir enlace (simulación)
        nombre_enlace = input("Ingrese el nombre del nuevo enlace: ")
        link_enlace = input("Ingrese el enlace: ")
        nuevo_enlace = Enlace_Leaf(nombre_enlace, link_enlace)
        carpeta_principal.add(nuevo_enlace)
        guardar_estructura_en_json(carpeta_principal, "Ejercicio Proxi/basedatos.json")
        print(f"Enlace '{nombre_enlace}' añadido correctamente.")
    elif opcion == "5":
        # Añadir carpeta (simulación)
        nombre_carpeta = input("Ingrese el nombre de la nueva carpeta: ")
        nueva_carpeta = Carpeta(nombre_carpeta)
        carpeta_principal.add(nueva_carpeta)
        guardar_estructura_en_json(carpeta_principal, "Ejercicio Proxi/basedatos.json")
        print(f"Carpeta '{nombre_carpeta}' añadida correctamente.")
    elif opcion == "6":
        # Editar documentos, enlaces o carpetas existentes
        agregar_elemento_a_carpeta(carpeta_principal)
    else:
        print("Opción no válida.")


def editar_elemento(carpeta):
    tipo_a_editar = input("Ingrese el tipo a editar (Documento, Enlace, Carpeta): ")
    nombre_a_editar = input("Ingrese el nombre a editar: ")

    if tipo_a_editar == "Documento":
        editar_documento(carpeta, nombre_a_editar)
    elif tipo_a_editar == "Enlace":
        editar_enlace(carpeta, nombre_a_editar)
    elif tipo_a_editar == "Carpeta":
        editar_carpeta(carpeta, nombre_a_editar)
    else:
        print("Tipo no válido.")
        
def editar_documento(carpeta, nombre_documento):
    for child in carpeta._children:
        if isinstance(child, Documentos_Leaf) and child.nombre == nombre_documento:
            print(f"Documento encontrado: {child.operation()}")
            nuevo_nombre = input("Ingrese el nuevo nombre del documento: ")
            nuevo_tipo = input("Ingrese el nuevo tipo de documento: ")
            nuevo_tamaño = int(input("Ingrese el nuevo tamaño del documento en KB: "))
            
            child.nombre = nuevo_nombre
            child.tipo_documento = nuevo_tipo
            child.tamaño = nuevo_tamaño
            
            guardar_estructura_en_json(carpeta, "Ejercicio Proxi/basedatos.json")
            
            print(f"Documento '{nombre_documento}' editado correctamente.")
            return

    print(f"Documento '{nombre_documento}' no encontrado.")
    
def editar_enlace(carpeta, nombre_enlace):
    for child in carpeta._children:
        if isinstance(child, Enlace_Leaf) and child.nombre == nombre_enlace:
            print(f"Enlace encontrado: {child.operation()}")
            nuevo_nombre = input("Ingrese el nuevo nombre del enlace: ")
            nuevo_link = input("Ingrese el nuevo enlace: ")
            
            child.nombre = nuevo_nombre
            child.link = nuevo_link
            
            guardar_estructura_en_json(carpeta, "Ejercicio Proxi/basedatos.json")
            
            print(f"Enlace '{nombre_enlace}' editado correctamente.")
            return

    print(f"Enlace '{nombre_enlace}' no encontrado.")
    
def editar_carpeta(carpeta, nombre_carpeta):
    for child in carpeta._children:
        if isinstance(child, Carpeta) and child.nombre == nombre_carpeta:
            print(f"Carpeta encontrada: {child.operation()}")
            nuevo_nombre = input("Ingrese el nuevo nombre de la carpeta: ")
            
            child.nombre = nuevo_nombre
            
            guardar_estructura_en_json(carpeta, "Ejercicio Proxi/basedatos.json")
            
            print(f"Carpeta '{nombre_carpeta}' editada correctamente.")
            return

    print(f"Carpeta '{nombre_carpeta}' no encontrada.")
    
    
    
def agregar_elemento_a_carpeta(carpeta_principal):
    # Mostrar las carpetas disponibles
    print("Carpetas disponibles:")
    for i, child in enumerate(carpeta_principal._children):
        if isinstance(child, Carpeta):
            print(f"{i + 1}. {child.nombre}")

    # Elegir la carpeta
    try:
        indice_carpeta = int(input("Seleccione una carpeta (por número): ")) - 1
        carpeta_seleccionada = carpeta_principal._children[indice_carpeta]

        # Pedir detalles del nuevo elemento
        tipo_elemento = input("Ingrese el tipo de elemento (Documento, Enlace, Carpeta): ")
        nombre_elemento = input("Ingrese el nombre del nuevo elemento: ")

        if tipo_elemento == "Documento":
            tipo_documento = input("Ingrese el tipo de documento: ")
            tamaño_documento = int(input("Ingrese el tamaño del documento en KB: "))
            nuevo_elemento = Documentos_Leaf(nombre_elemento, tipo_documento, tamaño_documento)
        elif tipo_elemento == "Enlace":
            enlace = input("Ingrese el enlace: ")
            nuevo_elemento = Enlace_Leaf(nombre_elemento, enlace)
        elif tipo_elemento == "Carpeta":
            nuevo_elemento = Carpeta(nombre_elemento)
        else:
            print("Tipo de elemento no válido.")
            return

        carpeta_seleccionada.add(nuevo_elemento)
        guardar_estructura_en_json(carpeta_principal, "Ejercicio Proxi/basedatos.json")
        print(f"Elemento '{nombre_elemento}' añadido correctamente a la carpeta '{carpeta_seleccionada.nombre}'.")
    except (ValueError, IndexError):
        print("Selección no válida.")






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
'''
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
    Usuario.buscar_en_csv("Ejercicio Proxi/usuarios.csv", nombre_usuario_buscar, contraseña_buscar)
    if Usuario.buscar_en_csv("Ejercicio Proxi/usuarios.csv", nombre_usuario_buscar, contraseña_buscar):
        # Usuario autenticado, crear Proxy y acceder a la estructura
        carpeta_principal = Carpeta("Principal")
        documento1 = Documentos_Leaf("Documento1", "Texto", 10)

        proxy_documento1 = Proxy(documento1)
        

        # Llamada a la función realizar_operacion
        proxy_documento1.operation()
        carpeta_principal.add(documento1)
        carpeta_principal.add(proxy_documento1)

        # Convertir la estructura a JSON
        estructura_json = carpeta_principal.to_dict()
        with open("Ejercicio Proxi/basedatos.json", "w") as json_file:
            json.dump(estructura_json, json_file, indent=2)

else:
    print("Opción no válida. Por favor, seleccione 'r' para registrarse o 'i' para iniciar sesión.")
'''