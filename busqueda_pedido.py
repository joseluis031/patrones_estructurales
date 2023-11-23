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
                print("¿fue una pizza by you Delizioso? (si/no):" )
                respuesta2 = input("Sí/No: ")
                if respuesta2.lower() == "si":
                    buscar_pizza_personalizada(id_usuario)
                    print("¿Quieres repetirlo? (si/no):" )
                    respuesta = input("Sí/No: ")
                    if respuesta.lower() == "si":
                        print("Repetimos el pedido anterior.")
                        exit()
                    else:
                        pass
                else:
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
        
        print("Detalles del pedido anterior:")
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
                # Obtener el detalle del pedido formateado
                detalle_formateado = eval(row[3])  # Convertir la cadena a una lista de Python
                print(f"Pedido: {row[1]}, Precio: {row[2]}, Contiene: {', '.join(detalle_formateado)}")
                
import csv

def buscar_pizza_personalizada(id_usuario):
    with open('pedidosnuevos.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        encontrado = False
        fila_anterior = None

        for row in reader:
            if row and row[0] == id_usuario:
                # Si se encontró la fila con el id_usuario, imprime la fila anterior
                if fila_anterior is not None:
                    masa = fila_anterior[2]
                    salsa = fila_anterior[3]
                    otros_ingredientes = fila_anterior[4:5]
                    metodo = fila_anterior[-4]
                    presentacion = fila_anterior[-3]
                    maridaje = fila_anterior[-2]
                    ingredientes_extra = fila_anterior[-1]

                    resultado = "Tu anterior pedido de pizza:\nMasa: {}\nSalsa: {}\nIngredientes: {}\nMétodo de cocción: {}\nPresentación: {}\nMaridaje: {}\nIngredientes extra: {}".format(masa, salsa, "\n".join(otros_ingredientes), metodo, presentacion, maridaje, ingredientes_extra)
                    print(resultado)
                    print()
                    encontrado = True
                break

            # Guarda la fila actual como la fila anterior
            fila_anterior = row

    if not encontrado:
        print(f"No se encontró un pedido para el usuario con ID {id_usuario}")

                                