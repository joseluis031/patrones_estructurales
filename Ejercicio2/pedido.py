from builder import *
import csv
from cliente2 import *
from Guardar_pizza import *
from lectura_csv import *
from interfaz import *

def pedido_usuario():
    usuario = Usuario()
    builder = ConcreteBuilder1()
    usuario.builder = builder
    usuario.pedir_nombre()
    usuario.pedir_usuario()
    usuario.pedir_contraseña()
    usuario.pedir_pedido()
    usuario.pedir_pizza()
    # Accede directamente a los elementos del Composite
    detalles_pizza = builder.product_pizza.operation()
    detalles_pizza = detalles_pizza.replace("Branch(", "").replace(")", "").replace("+", ",").replace(" ", "")
    detalles_pizza = ",".join(part.split(":")[1] for part in detalles_pizza.split(","))

    # Guarda el pedido en el CSV
    guardar_pedido_en_csv(usuario._nombre, usuario._usuario, usuario._contrasenia, detalles_pizza)