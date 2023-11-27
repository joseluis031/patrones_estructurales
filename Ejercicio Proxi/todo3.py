from abc import ABC, abstractmethod
from typing import List
from datetime import datetime
import json


class Component(ABC):
    @abstractmethod
    def operation(self) -> None:
        pass
    
    def to_dicta(self):
        raise NotImplementedError("to_dict method must be implemented in subclasses")
    
    def realizar_operacion(self):
        pass

class Carpeta(Component):
    def __init__(self, nombre):
        self.nombre = nombre
        self._children = []
    
    def add(self, component: Component) -> None:
        self._children.append(component)
        
    def remove(self, component: Component) -> None:
        self._children.remove(component)
    
    def operation(self) -> str:
        results = [f"Composite: {self.nombre}"]
        for child in self._children:
            results.append(child.operation())
        return '\n'.join(results)
    
    def to_dicta(self):
        return {
            "tipo": "Carpeta",
            "nombre": self.nombre,
            "Contiene": [child.to_dict() for child in self._children]
        }
            
class Documentos_Leaf(Component):
    def __init__(self, nombre, tipo_documento, tamaño):
        self.nombre = nombre
        self.tipo_documento = tipo_documento
        self.tamaño = tamaño
        
        
    def operation(self):
        return  f"Leaf: {self.nombre} ({self.tipo_documento}, {self.tamaño} KB)"
    
    def to_dicta(self):
        return {
            "tipo": "Documento",
            "nombre": self.nombre,
            "tipo_documento": self.tipo_documento,
            "tamanio": self.tamaño,
        }

class Enlace_Leaf(Component):
    def __init__(self, nombre, link):
        self.nombre = nombre
        self.link = link
        
    def operation(self):
        return f"Enlace: {self.nombre} -> {self.link}"
    
    def to_dict(self):
        return {
            "tipo": "Enlace",
            "nombre": self.nombre,
            "link": self.link
        }


class Proxy2(Component):
    def __init__(self, real_subject, usuarios_registrados=None):
        self.real_subject = real_subject
        self.usuarios_registrados = usuarios_registrados
        self.access_log = []
        self.access_checked = False  # Flag to track if access has been checked
        self.usuario_autenticado = False  # Flag para rastrear si el usuario está autenticado

    def operation(self):
        if not self.access_checked:  # Check access only the first time
            self.check_access()
            self.access_checked = True
        self.real_subject.operation()
        self.log_access()

    def check_access(self, nombre_usuario, contraseña) -> None:
        print("Proxy: Verificando el acceso antes de enviar una solicitud real...")
        #que pasen 3 segundos
        from time import sleep
        sleep(1)
        
        if self.usuarios_registrados:
            usuario_autenticado = any(
                user.usuario == nombre_usuario and user.contraseña == contraseña for user in self.usuarios_registrados
            )

            if usuario_autenticado:
                print("Proxy: Usuario autenticado. Acceso concedido.")
                self.usuario_autenticado = True
                nombre_usuario = nombre_usuario
                self.log_access(nombre_usuario)
                self.to_dicta()
                return True
                
            else:
                print("Proxy: Usuario no autenticado. Acceso denegado.")
                exit()  # Salir del programa si el usuario no está autenticado
        else:
            print("Proxy: No hay usuarios registrados. Acceso denegado.")
            exit()  # Salir del programa si no hay usuarios registrados


    def log_access(self,nombre_usuario) -> None:
        if self.usuario_autenticado:
            print("Proxy: Registro de la hora de la solicitud:", end="")
            print("El usuario {} accedió a la carpeta {} a las {}".format(nombre_usuario, self.real_subject.nombre, datetime.now().strftime("%H:%M:%S")))
            return True
 
    def to_dicta(self):
        return {
            'type': 'Proxy',
            'real_subject': self.real_subject.to_dict(),
            'access_log': self.access_log
        }



def cargar_estructura_desde_json5(parent, json_data):
    for child_data in json_data.get("Contiene", []):
        if child_data.get("tipo") == "Carpeta":
            child_folder = Carpeta(child_data.get("nombre"))
            parent.add(child_folder)
            cargar_estructura_desde_json5(child_folder, child_data)
        elif child_data.get("tipo") == "Documento":
            child_document = Documentos_Leaf(child_data.get("nombre"), child_data.get("tipo_documento"), child_data.get("tamanio"))
            parent.add(child_document)
        elif child_data.get("tipo") == "Enlace":
            child_link = Enlace_Leaf(child_data.get("nombre"), child_data.get("link"))
            parent.add(child_link)








def guardar_estructura_en_json(estructura, archivo_json):
    estructura_json = estructura.to_dict()
    with open(archivo_json, "w") as json_file:
        json.dump(estructura_json, json_file, indent=2)
        
        

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
    proxy = Proxy2(carpeta_principal, usuarios_registrados)
    # Autenticar al usuario mediante el Proxy
    if proxy.check_access(nombre_usuario_buscar, contraseña_buscar):
        print(f"Inicio de sesión exitoso para '{nombre_usuario_buscar}' ")
        return True
    else:
        print(f"Inicio de sesión fallido para '{nombre_usuario_buscar}' o la contraseña no coincide")
        return False
    
    
    


from añadir_carpeta import *
from borrar import *
from editar import *

def realizar_operacion(usuario_actual, carpeta_principal):
    # ... (código anterior)

    opcion1 = input("Seleccione una opción: \n 1. Añadir Documento, enlace o carpeta \n 2. Borrar Documento, enlace o carpeta \n 3. Editar Documento, enlace o carpeta \n 4. Acceder a una Carpeta (simulación) \n 5. Salir \n").lower()

    if opcion1 == "1":
        pregunta = input("¿Que desea: \n 1.añadir un documento, enlace o carpeta en la carpeta principal \n 2.añadir un documento, enlace o carpeta dentro de una carpeta ?").lower()
        if pregunta == "1":
            pregunta2 = input("¿Que desea: \n 1.añadir un documento \n 2.añadir un enlace \n 3.añadir una carpeta ? \n").lower()
            if pregunta2 == "1":
                
                
                documento1 = Documentos_Leaf("Documento1", "Texto", 10)
        
                proxy_documento1 = Proxy(documento1)
                proxy_documento1.operation()

                carpeta_principal.add(proxy_documento1)

                # Convertir la estructura a JSON
                estructura_json = carpeta_principal.to_dict()
                print(estructura_json)
                
                guardar_estructura_en_json(estructura_json, "Ejercicio Proxi/basedatos.json")

                print(f"Documento añadido correctamente.")
                exit()
            elif pregunta2 == "2":
                nombre_enlace = input("Ingrese el nombre del nuevo enlace: ")
                link_enlace = input("Ingrese el enlace: ")
                nuevo_enlace = Enlace_Leaf(nombre_enlace, link_enlace)
                carpeta_principal.add(nuevo_enlace)
                guardar_estructura_en_json(carpeta_principal, "Ejercicio Proxi/basedatos.json")
                print(f"Enlace '{nombre_enlace}' añadido correctamente.")
                exit()
                
            elif pregunta2 == "3":
                nombre_carpeta = input("Ingrese el nombre de la nueva carpeta: ")
                nueva_carpeta = Carpeta(nombre_carpeta)
                carpeta_principal.add(nueva_carpeta)
                guardar_estructura_en_json(carpeta_principal, "Ejercicio Proxi/basedatos.json")
                print(f"Carpeta '{nombre_carpeta}' añadida correctamente.")
                exit()
        elif pregunta == "2":
            agregar_elemento_a_carpeta(carpeta_principal)
            exit()
            
        
    elif opcion1 == "2":
        borrar_elemento(carpeta_principal)        
        exit()
                
    elif opcion1 == "3":
        editar_elemento(carpeta_principal)
        exit()
        
    elif opcion1 == "4":
        carpeta_principal.operation()
       # log_access(carpeta_principal.nombre)
        exit()
    elif opcion1 == "5":
        print("Gracias por usar el programa")
        exit()
    


carpeta_principal = Carpeta("Principal")
cargar_estructura_desde_json5(carpeta_principal, json.load(open("Ejercicio Proxi/basedatos.json")))

opcion = input("¿Desea registrarse (r) o iniciar sesión (i)? ").lower()

if opcion == 'r':
    # Registrarse
    registrar_usuario()
elif opcion == 'i':
    # Iniciar sesión
    if iniciar_sesion():
        
        realizar_operacion("usuario_actual", carpeta_principal)
        # Usuario autenticado, cargar estructura y realizar operaciones

else:
    print("Opción no válida. Por favor, seleccione 'r' para registrarse o 'i' para iniciar sesión.")