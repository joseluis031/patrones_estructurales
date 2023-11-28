from proxi import *

import getpass  # Módulo para ocultar la entrada de contraseña en la consola
import csv 



class Usuario:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    def guardar_en_bd(self):
        # Conectar a la base de datos
        conn = sqlite3.connect('Ejercicio Proxi/usuarios.db')
        cursor = conn.cursor()
        try:
            # Insertar nuevo usuario
            query = "INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)"
            cursor.execute(query, (self.usuario, self.contraseña))
            conn.commit()
            conn.close()
            print(f"Usuario '{self.usuario}' registrado correctamente")

        except sqlite3.IntegrityError:
            print("Ese usuario no esta disponible")
            conn.close()

        

    @staticmethod
    def cargar_usuarios_desde_bd():
        # Conectar a la base de datos
        conn = sqlite3.connect('Ejercicio Proxi/usuarios.db')
        cursor = conn.cursor()

        # Obtener usuarios
        query = "SELECT usuario, contraseña FROM usuarios"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Cerrar la conexión
        conn.close()

        # Crear instancias de Usuario a partir de los resultados
        usuarios = [Usuario(row[0], row[1]) for row in rows]
        return usuarios
    



def registrar_usuario():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    nuevo_usuario = Usuario(nombre_usuario, contraseña)
    nuevo_usuario.guardar_en_bd()
    


def iniciar_sesion():
    nombre_usuario_buscar = input("Ingrese su nombre de usuario: ")
    contraseña_buscar = getpass.getpass("Ingrese su contraseña: ")

    # Cargar usuarios desde el archivo CSV
    
    # Crear una instancia de ProxyDB con la lista de usuarios cargada
    proxydb = ProxyDB(carpeta_principal)
    
    # Autenticar al usuario mediante el ProxyDB
    if proxydb.check_access(nombre_usuario_buscar, contraseña_buscar):
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