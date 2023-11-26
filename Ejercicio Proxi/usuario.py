from proxi import *


import json
import csv
from datetime import datetime

class Usuario:
    def __init__(self, nombre_usuario, contrasenia):
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia

class Proxy(Component):
    def __init__(self, real_subject, usuarios_registrados):
        self.real_subject = real_subject
        self.access_log = {}
        self.usuarios_registrados = usuarios_registrados
        self.usuario_actual = None

    def registrar_usuario(self, nombre_usuario, contrasenia):
        nuevo_usuario = Usuario(nombre_usuario, contrasenia)
        self.usuarios_registrados.append(nuevo_usuario)
        print(f"Usuario {nombre_usuario} registrado exitosamente.")

    def iniciar_sesion(self, nombre_usuario, contrasenia):
        for usuario in self.usuarios_registrados:
            if usuario.nombre_usuario == nombre_usuario and usuario.contrasenia == contrasenia:
                self.usuario_actual = usuario
                print(f"Sesión iniciada para {nombre_usuario}.")
                return True
        print("Nombre de usuario o contraseña incorrectos.")
        return False

    def cerrar_sesion(self):
        self.usuario_actual = None
        print("Sesión cerrada.")

    def operation(self):
        if self.usuario_actual:
            document_name = self.real_subject.nombre
            if self.check_access(document_name):
                self.real_subject.operation()
                self.access_log[document_name] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            print("Acceso denegado. Inicie sesión para continuar.")

    def check_access(self, document_name) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        # Aquí puedes agregar lógica adicional según tus requisitos
        return True

def guardar_en_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def cargar_desde_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def guardar_en_csv(data, filename):
    header = ["nombre_usuario", "contrasenia"]
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for usuario in data:
            writer.writerow([usuario.nombre_usuario, usuario.contrasenia])

def cargar_desde_csv(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = [Usuario(row["nombre_usuario"], row["contrasenia"]) for row in reader]
            return data
    except FileNotFoundError:
        return []

# Ejemplo de uso:
usuarios_registrados = cargar_desde_csv("Ejercicio Proxi/usuarios.csv")

proxy = Proxy(Documentos_Leaf("Documento1", "Texto", 1024), usuarios_registrados)

# Registro de un nuevo usuario
proxy.registrar_usuario("as", "as")

# Inicio de sesión
proxy.iniciar_sesion("am", "am")

# Acceso a un documento
proxy.operation()

# Guardar información en JSON y CSV
usuarios_registrados.append(Usuario("kj", "kl"))
guardar_en_json([vars(usuario) for usuario in usuarios_registrados], "Ejercicio Proxi/usuarios.json")
guardar_en_csv(usuarios_registrados, "Ejercicio Proxi/usuarios.csv")
