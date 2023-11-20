import csv
from composite_menu import *
from clientw3 import *




def buscar_pedido_anterior():
    # Preguntar al usuario si ha hecho algún pedido antes

    
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        # Buscar el ID del usuario en el archivo de clientes
        id_usuario = buscar_id_usuario(nombre_usuario, contraseña)

        if id_usuario is not None:
            print("¿fue personalizjjado? (si/no): ")
            respuesta1 = input("Sí/No: ")
            if respuesta1.lower() == "no":
                buscar_combos_menu(id_usuario)
                print("¿Quieres repetirlo? (si/no):" )
                respuesta = input("Sí/No: ")
                if respuesta.lower() == "si":
                    print("Repetimos el pedido anterior.")
                    exit()
                
                else:
                    pass
                
            if respuesta1.lower() == "si":
                # Buscar los elementos asociados al ID en el archivo de pedidos
                buscar_pedidos(id_usuario)
                print("¿Quieres repetirlo? (si/no):" )
                respuesta = input("Sí/No: ")
                if respuesta.lower() == "si":
                    print("Repetimos el pedido anterior.")
                    exit()
                else:
                    pass
        else:
            print("Usuario no encontrado.")
            pass
    

def buscar_id_usuario(nombre_usuario, contraseña):
    archivo_csv_clientes = 'clientes.csv'

    with open(archivo_csv_clientes, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la primera fila (encabezados)

        for row in reader:
            if row[1] == nombre_usuario and row[2] == contraseña:
                
                return row[3]  # Devolver el ID del usuario

    return None

def buscar_pedidos(id_usuario):
    archivo_csv_pedidos = 'pedidos_cliente.csv'

    with open(archivo_csv_pedidos, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la primera fila (encabezados)
        
        print("Elementos del pedido anterior:")
        for row in reader:
            if row[0] == id_usuario:
                print(f"Elemento: {row[1]}, Precio: {row[2]}")
                
def buscar_combos_menu(id_usuario):
    archivo_csv_pedidos = 'combos_menu.csv'

    with open(archivo_csv_pedidos, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the headers

        print("Detalles del pedido anterior:")
        for row in reader:
            if row[0] == id_usuario:
                print(f"Tipo de pedido: {row[1]}, Precio: {row[2]}")
                