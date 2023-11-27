from composite_menu import *
from clientw3 import *


def obtener_pizza() -> str:
    lista_pizza = [ "personalizada","margarita", "barbacoa", "4 quesos", "carbonara", "hawaiana", "romana", "4 estaciones", "vegetal", "napolitana", "a"]
    pizza = input("¿Qué pizza quieres? Tenemos: " + ", ".join(lista_pizza) + ": ")
    while pizza not in lista_pizza:
        pizza = input("No tenemos esa, ¿qué pizza quieres? ")
    return pizza

def obtener_bebida() -> str:
    lista_bebida = ["coca-cola", "fanta", "agua", "aa"]
    bebida = input("¿Qué bebida quieres? Tenemos: " + ", ".join(lista_bebida) + ": ")
    while bebida not in lista_bebida:
        bebida = input("No tenemos esa, ¿qué bebida quieres? ")
    return bebida

def obtener_entrante() -> str:
    lista_entrante = ["patatas", "calamares", "ensalada", "aa"]
    entrante = input("¿Qué entrante quieres? Tenemos: " + ", ".join(lista_entrante) + ": ")
    while entrante not in lista_entrante:
        entrante = input("No tenemos esa, ¿qué entrante quieres? ")
    return entrante


def obtener_postre() -> str:
    lista_postre = ["tarta de queso", "tarta de chocolate", "helado", "a"]
    postre = input("¿Qué postre quieres? Tenemos: " + ", ".join(lista_postre) + ": ")
    while postre not in lista_postre:
        postre = input("No tenemos esa, ¿qué postre quieres? ")
    return postre

def crear_menu_personalizado() -> List[Component_menu]:
    print("Vamos a ello!!")
    pizza = obtener_pizza()
    bebida = obtener_bebida()
    entrante = obtener_entrante()
    postre = obtener_postre()

    pedido_pizza = Leaf_pizza(pizza)
    pedido_bebida = Leaf_bebida(bebida)
    pedido_entrante = Leaf_entrante(entrante)
    pedido_postre = Leaf_postre(postre)

    return [pedido_pizza, pedido_bebida, pedido_entrante, pedido_postre]


