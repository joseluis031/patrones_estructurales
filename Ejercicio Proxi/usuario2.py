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

else:
    print("Opción no válida. Por favor, seleccione 'r' para registrarse o 'i' para iniciar sesión.")
'''