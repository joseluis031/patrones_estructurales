from builder_pizza import *


director = Director()
#si quito para que sea privado, me da ellist part pero sigo sin poder acceder a las partes

import csv

#creame una clase Usuario que pida el nombre del usuario, contraseña y pedido y quiero que para que elija el pedido pase al builder
#y que el builder cree la pizza que el usuario ha pedido


#clase usuario
class Usuariobu:
    def __init__(self):
         self._builder = None
         self.nombre = None
         self.usuario = None
         
         self.contrasenia = None
         self.id = hash((self.nombre, self.usuario, self.contrasenia))
         self._pedido = None
         self._pizza = None
         self.parteslista = []

    @property
    def builder(self) -> Builder:
         return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
         """
         El Director trabaja con cualquier instancia de constructor que pase el código del cliente.
          lo. De esta manera, el código del cliente puede alterar el tipo final del nuevo
          producto ensamblado.
         """
         self._builder = builder

    #funciones para pedir nombre, usuario, contraseña y pedido
    def pedir_nombre(self) -> None:
        self._nombre = input("Introduzca su nombre: ")
        print("Bienvenido", self._nombre)

    def pedir_usuario(self) -> None:
        self._usuario = input("Introduzca su usuario: ")
        print("Usuario correcto")

    def pedir_contraseña(self) -> None:
        self._contrasenia = input("Introduzca su contraseña: ")
        print("Contraseña guardada")

    def pedir_pedido(self) -> None:

        self._pedido = input("¿Quieres realizar un pedido? (si/no) ")
        if self._pedido == "Si" or "si" or "S" or "s":
            print("Vamos a ello!!")


    
    def pedir_pizza(self) -> None:
        self.builder.tipo_de_masa()
        self.builder.salsa_base()
        self.builder.ingredientes_principales()
        self.builder.tecnicas_de_coccion()
        self.builder.presentacion()
        self.builder.maridajes_recomendados()
        self.builder.extras()
        
        #para  guardar el pedido en un csv
        detalles_pizza = self.builder.producir_pizza.parts
        
        def guardar_pizza( tipo, detalles_pizza):
            with open('Pizzeria/Datos/pedido_pizzapers.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                id = self.nombre
                # Crea una nueva fila con nombre, usuario y contraseña
                row = [id, tipo]

                # Agrega cada detalle de la pizza como una columna separada
                for detalle in detalles_pizza:
                    if ":" in detalle:
                        key, value = detalle.split(": ", 1)
                        row.append(value)
                    else:
                        row.append(detalle)

                # Agrega detalles adicionales del pedido
                row.extend([""] * (7 - len(detalles_pizza)))  # Asegura que haya suficientes columnas para todos los detalles
                writer.writerow(row)
        guardar_pizza("Pizza personaliza",detalles_pizza)
        print(detalles_pizza)

    def elecciones(self):
        # Esta función toma los detalles de la pizza y guarda solo las elecciones en un archivo CSV
        self.partes=self.builder.producir_pizza.parts
        return(self.partes)
        
        
        
#funcion para guardar el pedido en un csv   



