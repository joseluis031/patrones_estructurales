from builder import *
from cliente2 import *
import csv
from Guardar_pizza import *
from interfaz import *
from pedido import *


def lectura(nombre_usuario, nombre_usuario2, contrasenia):
            with open('pedidosnuevos.csv', mode='r', newline='') as file:
                reader = csv.reader(file)
                encontrado = False
                for row in reader:  #tiene que coincidir el nombre de usuario, el nombre y la contraseña para poder verificar que es el usuario
                    if row and row[0] == nombre_usuario and row[1] == nombre_usuario2 and row[2] == contrasenia:
                        
                                print("¡Bienvenido de nuevo, {}!".format(nombre_usuario))
                                #lee y printea los nombre de la columna 0 del csva partir de Masa
                                    #   
                                ingredientes = row[3:]
                                masa = ingredientes[0]
                                salsa = ingredientes[1]
                                otros_ingredientes = ingredientes[2:-4]
                                metodo = ingredientes[-4]
                                presentacion = ingredientes[-3]
                                maridaje = ingredientes[-2]
                                ingredientes_extra = ingredientes[-1]

                                resultado = "Tu anterior pedido de pizza:\nMasa: {}\nSalsa: {}\nIngredientes: {}\nMétodo de cocción: {}\nPresentación: {}\nMaridaje: {}\nIngredientes extra: {}".format(masa, salsa, "\n".join(otros_ingredientes), metodo, presentacion, maridaje, ingredientes_extra)

                                print(resultado)

                                print()
                                encontrado = True
                                print("¿Quieres repetir el pedido?")
                                respuesta = input("Sí/No: ")
                                if respuesta.lower() == "si":
                                    print("Repetimos el pedido anterior.")
                                    break
                                else:
                                    print("Comencemos el proceso de creación de la pizza.")
                                    pedido_usuario()
                                    break

                if not encontrado:
                    print("No encontramos tu usuario o la contraseña es incorrecta. Continúa con el proceso de creación de la pizza.")
                    pedido_usuario()