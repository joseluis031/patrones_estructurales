from abc import ABC, abstractmethod
from typing import List
from datetime import datetime
import json
import sqlite3
from time import sleep

class Component(ABC):
    @abstractmethod
    def operation(self) -> None:
        pass
    
    def to_dict(self):
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
        results = [f"Contiene:"]
        for child in self._children:
            results.append(child.operation())
        return '\n'.join(results)
    
    def to_dict(self):
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
        return  f"Documento: {self.nombre} ({self.tipo_documento}, {self.tamaño} KB)"
    
    def to_dict(self):
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
'''
class Proxy(Component):
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
        
'''     
class ProxyDB:
    def __init__(self, real_subject):
        self.real_subject = real_subject
        self.conn = sqlite3.connect('Ejercicio Proxi/usuarios.db')
        self.cursor = self.conn.cursor()

    def check_access(self, nombre_usuario, contraseña) -> bool:
        print("ProxyDB: Verificando el acceso antes de enviar una solicitud real...")
        sleep(1)

        # Tu lógica para verificar el acceso usando la base de datos
        usuario_autenticado = self.verify_access_from_db(nombre_usuario, contraseña)

        if usuario_autenticado:
            print(f"ProxyDB: Usuario autenticado. Acceso concedido.")
            self.usuario_autenticado = True
            self.log_access(nombre_usuario)
            self.guardar_hora_inicio_sesion(nombre_usuario)
            
            return True
        else:
            print("ProxyDB: Usuario no autenticado. Acceso denegado.")
            return False

    def verify_access_from_db(self, nombre_usuario, contraseña) -> bool:
        # Conectar a la base de datos
        conn = sqlite3.connect('Ejercicio Proxi/usuarios.db')
        cursor = conn.cursor()

        # Verificar si el usuario y la contraseña coinciden
        query = "SELECT COUNT(*) FROM usuarios WHERE usuario = ? AND contraseña = ?"
        cursor.execute(query, (nombre_usuario, contraseña))
        count = cursor.fetchone()[0]

        # Cerrar la conexión
        conn.close()

        # Si count es mayor que 0, el usuario está autenticado
        return count > 0

    def log_access(self, nombre_usuario):
        print("Proxy: Registro de la hora de la solicitud:", end="")
        print("El usuario {} accedió a la carpeta {} a las {}".format(
            nombre_usuario, self.real_subject.nombre, datetime.now().strftime("%H:%M:%S")
        ))
        return True
    
    def guardar_hora_inicio_sesion(self, nombre_usuario):
        # Conectar a la base de datos
        conn = sqlite3.connect('Ejercicio Proxi/usuarios.db')
        cursor = conn.cursor()
        # Insertar nueva sesión
        query = "INSERT INTO sesiones (usuario, hora_inicio_sesion) VALUES (?, ?)"
        cursor.execute(query, (nombre_usuario, datetime.now().strftime("%H:%M:%S")))
        

        # Confirmar y cerrar la conexión
        conn.commit()
        conn.close()
        
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
        
carpeta_principal = Carpeta("Principal")