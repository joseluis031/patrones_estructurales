from builder import *
from cliente2 import *
import csv
from composite import *

def guardar_pedido_en_csv(nombre, usuario, contrasenia, product):
    with open('pedidosnuevos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        # Crea una nueva fila con nombre, usuario y contraseña
        row = [nombre, usuario, contrasenia]

        # Agrega cada detalle de la pizza como una columna separada
        for detalle in product.get_parts_pizza():
            if ":" in detalle:
                key, value = detalle.split(": ", 1)
                row.append(value)
            else:
                row.append(detalle)

        writer.writerow(row)