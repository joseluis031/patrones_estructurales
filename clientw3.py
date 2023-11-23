import csv
from composite_menu import *    
from obtener_productos import *
from busqueda_pedido import *

import ast
class Cliente:
    def __init__(self, nombre, usuario, contraseña):
        self.nombre = nombre
        self.usuario = usuario
        self.contraseña = contraseña

    def guardar_cliente(self):
        # Nombre del archivo CSV
        archivo_csv = 'clientes.csv'
        self.id = hash((self.nombre, self.usuario, self.contraseña))


        # Crear o abrir el archivo en modo de escritura
        with open(archivo_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            row = [self.nombre, self.usuario, self.contraseña,self.id]
            # Si el archivo está vacío, escribir las columnas
            if file.tell() == 0:
                writer.writerow(['nombre', 'usuario', 'contrasenia', 'id'])

            # Escribir la información del cliente y su pedido
            writer = csv.writer(file)
            writer.writerow(row)
            
    def guardar_pedido(self, pedido):
        # Nombre del archivo CSV para los pedidos
        archivo_pedidos = 'pedidos_cliente.csv'

        # Crear o abrir el archivo en modo de escritura
        with open(archivo_pedidos, mode='a', newline='') as file:
            writer = csv.writer(file)

            # Si el archivo está vacío, escribir las columnas
            if file.tell() == 0:
                writer.writerow(['id', 'elemento', 'precio'])

            # Escribir el pedido del cliente con su ID
            for item in pedido:
                writer.writerow([self.id, item.operation(), item.precio()])
                
    def guardar_combo_menu(self, pedido, tipo):
        archivo_pedidos = 'combos_menu.csv'

        with open(archivo_pedidos, mode='a', newline='') as file:
            writer = csv.writer(file)
            precio_total = sum(item.precio() for item in pedido)
            if precio_total < 50:
                precio_con_descuento = precio_total - precio_total * 0.05 #menu
            else:
                precio_con_descuento = precio_total - precio_total * 0.15 #combo
            if file.tell() == 0:
                writer.writerow(['id', 'tipo_pedido', 'Precio', 'Pedido'])

            # Escribir el pedido del cliente con su ID
            nombres_elementos = [item._nombre for item in pedido]

        # Escribir el pedido del cliente con su ID
            writer.writerow([self.id, tipo, precio_con_descuento, self.format_pedido_detalle(nombres_elementos)])
    
    def format_pedido_detalle(self, pedido):
        from collections import Counter
    
    # Obtener un contador de elementos en el pedido
        contador_elementos = Counter(pedido)
    
    # Convertir el contador en una lista de cadenas con el formato "cantidad x elemento"
        formatted_pedido = [f"{cantidad} x {elemento}" for elemento, cantidad in contador_elementos.items()]
    
        return formatted_pedido
    
    
    def guardar_pizzapersonalizada(self):
        with open('pedidosnuevos.csv', mode='a', newline='') as file:
            writer = csv.writer(file)

            # Crea una nueva fila con nombre, usuario y contraseña
            row = [self.id]

             # Asegura que haya suficientes columnas para todos los detalles
            writer.writerow(row)
            
        
                


                
