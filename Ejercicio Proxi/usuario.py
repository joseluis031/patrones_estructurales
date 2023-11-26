from proxi import *


import json
import csv
from datetime import datetime


class Usuario:
    def __init__(self, nombre_usuario, contrasenia):
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia


    def cargar_desde_csv(filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                data = [Usuario(row["nombre_usuario"], row["contrasenia"]) for row in reader]
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

    def iniciar_sesion(usuarios_registrados, nombre_usuario, contrasenia):
        for usuario in usuarios_registrados:
            if usuario.nombre_usuario == nombre_usuario and usuario.contrasenia == contrasenia:
                print(f"Sesión iniciada para {nombre_usuario}.")
                return usuario
        print("Nombre de usuario o contraseña incorrectos.")
        return None

    def registrar_usuario(usuarios_registrados, nombre_usuario, contrasenia):
        nuevo_usuario = Usuario(nombre_usuario, contrasenia)
        usuarios_registrados.append(nuevo_usuario)
        print(f"Usuario {nombre_usuario} registrado exitosamente.")

# Ejemplo de uso:
usuarios_registrados = cargar_desde_csv("usuarios.csv")
proxy = Proxy(Documentos_Leaf("Documento1", "Texto", 1024))

# Solicitar al usuario que inicie sesión o se registre
opcion = input("Seleccione una opción:\n1. Iniciar Sesión\n2. Registrarse\n")
if opcion == "1":
    usuario = input("Introduzca su usuario: ")
    contraseña = input("Introduzca su contraseña: ")
    proxy.usuario_actual = iniciar_sesion(usuarios_registrados, usuario, contraseña)
    if proxy.usuario_actual:
        proxy.operation()
else:
    usuario = input("Introduzca su nuevo usuario: ")
    contraseña = input("Introduzca su nueva contraseña: ")
    registrar_usuario(usuarios_registrados, usuario, contraseña)
    proxy.usuario_actual = iniciar_sesion(usuarios_registrados, usuario, contraseña)
    proxy.operation()

# Guardar información en JSON y CSV
guardar_en_csv(usuarios_registrados, "usuarios.csv")
guardar_en_json(proxy.access_log, "registro_operaciones.json")