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
    def cargar_usuarios_desde_csv(archivo_csv):
        usuarios = []
        try:
            with open(archivo_csv, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        usuario = Usuario(row[0], row[1])
                        usuarios.append(usuario)
            print("Usuarios cargados correctamente desde CSV.")
        except Exception as e:
            print(f"Error al cargar usuarios desde CSV: {e}")
        return usuarios


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

    # Cargar usuarios desde el archivo CSV
    usuarios_registrados = Usuario.cargar_usuarios_desde_csv("Ejercicio Proxi/usuarios.csv")
    
    # Crear una instancia de Proxy con la lista de usuarios cargada
    proxy = Proxy(carpeta_principal, usuarios_registrados)
    # Autenticar al usuario mediante el Proxy
    if proxy.check_access(nombre_usuario_buscar, contraseña_buscar):
        print(f"Inicio de sesión exitoso para '{nombre_usuario_buscar}' ")
        return True
    else:
        print(f"Inicio de sesión fallido para '{nombre_usuario_buscar}' o la contraseña no coincide")
        return False

    
    
    








# Llamada a la función

























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