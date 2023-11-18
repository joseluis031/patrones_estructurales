import csv
from composite_menu import *    
import uuid  # Módulo para generar ID único

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

if __name__ == "__main__":
    # Ejemplo de cómo usar la clase Cliente
    bienvenida = input("¿Qué deseas hacer (1,2,3,4,5): 1. Crear tu propio menú, 2. Elegir un menú ya creado, 3. Un producto suelto, 4. Un Combo, 5. Nada ")

    # ... (Código existente)

    if bienvenida == "1":
        menu_personalizado = crear_menu_personalizado()

        # Calcular precio total del menú personalizado
        precio_total_menu_personalizado = sum(item.precio() for item in menu_personalizado)
        print("Detalles del menú personalizado:")
        for item in menu_personalizado:
            print(f"{item.operation()} - Precio: {item.precio()}")
        print(f"El precio total del menú personalizado es: {precio_total_menu_personalizado}")

        # Crear un cliente con la información del menú personalizado y guardar el pedido
        nombre_cliente = input("Ingrese su nombre: ")
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        # Crear un Composite_combo1 con los elementos del menú personalizado
        pedido_cliente = Composite_combo1("Menú Personalizado")
        for item in menu_personalizado:
            pedido_cliente.add(item)

        cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
        cliente.guardar_cliente()
        cliente.guardar_pedido(pedido_cliente._children)  # Guardar el pedido del cliente


        exit()
    # Resto del código...
