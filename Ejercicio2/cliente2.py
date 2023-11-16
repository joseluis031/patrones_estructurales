from builder import *
from cliente2 import *
import csv
from Guardar_pizza import *
from composite import *


director = Director()
builder = ConcreteBuilder1()
director.builder = builder

import csv

#creame una clase Usuario que pida el nombre del usuario, contraseña y pedido y quiero que para que elija el pedido pase al builder
#y que el builder cree la pizza que el usuario ha pedido


#clase usuario
class Usuario:
    def __init__(self):
         self._builder = None
         self._nombre = None
         self.usuario = None
         self._contrasenia = None
         self._pedido = None
         self._pizza = None

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

        # para guardar el pedido en un csv
        detalles_pizza = self.builder.product_pizza.get_parts_pizza()
        guardar_pedido_en_csv(self._nombre, self._usuario, self._contrasenia, detalles_pizza)



