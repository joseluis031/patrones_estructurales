from builder import *
import csv
from cliente2 import *
from Guardar_pizza import *
from lectura_csv import *
from interfaz import *

def pedido():
    usuario = Usuario()
    builder = ConcreteBuilder1()
    usuario.builder = builder
    usuario.pedir_nombre()
    usuario.pedir_usuario()
    usuario.pedir_contraseña()
    usuario.pedir_pedido()
    usuario.pedir_pizza()
    builder.product_pizza.list_parts()