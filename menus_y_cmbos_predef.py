from composite_menu import *
from clientw3 import *
from buscar_precio import *
from busqueda_pedido import *
from obtener_productos import *



def menu1():
    pedido1_pizza = Leaf_pizza("margarita")
    pedido1_bebida = Leaf_bebida("agua")
    pedido1_entrante = Leaf_entrante("alitas de pollo")
    pedido1_postre = Leaf_postre("helado")
    
    pedido1_menu = Composite_menu("Menu basico")
    pedido1_menu.add(pedido1_pizza)
    pedido1_menu.add(pedido1_bebida)
    pedido1_menu.add(pedido1_entrante)
    pedido1_menu.add(pedido1_postre)
    
    print("El precio de tu pizza es: ", pedido1_pizza.precio())
    print("El precio de tu bebida es: ", pedido1_bebida.precio())
    print("El precio de tu entrante es: ", pedido1_entrante.precio())
    print("El precio de tu postre es: ", pedido1_postre.precio())
    
    print("El precio total del menu basico (con descuento)es: ", pedido1_menu.precio())
    
    cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
    cliente.guardar_cliente()

    

# Guardar el pedido del cliente
    cliente.guardar_combo_menu(pedido1_menu._children, "Menu basico")