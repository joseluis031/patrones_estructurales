from builder import *
import csv
from cliente2 import *
from Guardar_pizza import *
from lectura_csv import *
from pedido import *


def interfaz(pedido_anterior):
    

    if pedido_anterior.lower() == "si":
        nombre_usuario = input("Por favor, introduce tu nombre: ")
        nombre_usuario2 = input("Por favor, introduce tu nombre de usuario: ")
        contrasenia = input("Por favor, introduce tu contraseña: ")
        lectura(nombre_usuario, nombre_usuario2, contrasenia)
            

    else:
        print("Comencemos el proceso de creación de la pizza.")
        pedido_usuario()
            
        

