from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional, Any


class ElementoMenu:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio


class Menu:
    def __init__(self, codigo: str) -> None:
        self.codigo = codigo
        self.items: List[ElementoMenu] = []


class ConstructorMenu(ABC):
    @abstractmethod
    def construir_menu(self) -> None:
        pass

    @abstractmethod
    def agregar_entrada(self) -> None:
        pass

    @abstractmethod
    def agregar_bebida(self) -> None:
        pass

    @abstractmethod
    def agregar_pizza(self) -> None:
        pass

    @abstractmethod
    def agregar_postre(self) -> None:
        pass

    @abstractmethod
    def agregar_combo(self, sub_menu: Menu) -> None:
        pass

    @abstractmethod
    def obtener_menu(self) -> Menu:
        pass


class ConstructorMenuConcreto(ConstructorMenu):
    def __init__(self) -> None:
        self._menu = Menu("")

    def construir_menu(self) -> None:
        self._menu = Menu("")

    def agregar_entrada(self) -> None:
        lista_entrantes = ["Ensalada", "Patatas", "Croquetas", "Alitas de pollo", "Calamares", "Nachos", "Huevos rotos", "Tortilla de patatas", "Pimientos de padrón", "Pulpo a la gallega", "Jamón ibérico", "Queso manchego", "Tabla de embutidos", "Tabla de patés"]
        print("Entrantes disponibles:")
        for i, entrante in enumerate(lista_entrantes, 1):
            print(f"{i}. {entrante}")

        entrada = None

        while True:
            seleccion_entrada = input("Elige el número del entrante que quieres o introduce '0' si no quieres entrante: ")
            if seleccion_entrada == '0':
                print("No se añadirá entrante al menú(costará lo mismo).")
                break
            elif seleccion_entrada.isdigit():
                indice_entrada = int(seleccion_entrada)
                if 1 <= indice_entrada <= len(lista_entrantes):
                    entrante_elegido = lista_entrantes[indice_entrada - 1]
                    entrada = ElementoMenu(entrante_elegido, 5.0)
                    print(f"Has elegido: {entrante_elegido}")
                    self._menu.items.append(entrada)
                    break
                else:
                    print("Número de entrante no válido. Inténtalo de nuevo.")
            else:
                print("Entrada no válida. Introduce el número del entrante o '0'.")


    def agregar_bebida(self) -> None:
        lista_bebidas = ["Coca-cola", "Fanta", "Agua", "Cerveza", "Vino", "Zumo"]
        print("Bebidas disponibles:")
        for i, bebida in enumerate(lista_bebidas, 1):
            print(f"{i}. {bebida}")

        bebida = None

        while True:
            seleccion_bebida = input("Elige el número de la bebida que quieres: ")
            if seleccion_bebida.isdigit():
                indice_bebida = int(seleccion_bebida)
                if 1 <= indice_bebida <= len(lista_bebidas):
                    bebida_elegida = lista_bebidas[indice_bebida - 1]
                    bebida = ElementoMenu(bebida_elegida, 2.0)
                    print(f"Has elegido: {bebida_elegida}")
                    self._menu.items.append(bebida)
                    break
                else:
                    print("Número de bebida no válido. Inténtalo de nuevo.")
            else:
                print("Entrada no válida. Introduce el número de la bebida.")


    def agregar_pizza(self) -> None:
        lista_pizzas = ["Margarita", "Barbacoa", "4 quesos", "Carbonara", "Hawaiana", "Mediterránea", "Vegetal", "Mexicana", "Napolitana", "Romana", "Serrana", "Ibérica", "Marinera", "Tropical", "Trufa", "Gourmet", "Boloñesa", "Prosciutto", "Tartufata", "Capricciosa", "Tonno", "Diavola", "Pugliese", "Bufalina", "Parmigiana", "Frutti di Mare", "Pesto", "Bianca", "Siciliana", "Focaccia", "Calzone", "Ortolana", "Pugliese", "Rustica", "Salmone", "Salsiccia", "Sorrentina", "Tedesca", "Valtellina", "Vegetariana", "Wurstel", "Zingara"]
        print("Pizzas disponibles: ")
        for i, pizza in enumerate(lista_pizzas, 1):
            print(f"{i}. {pizza}")

        pizza = None

        while True:
            seleccion_pizza = input("Elige el número de la pizza que quieres: ")
            if seleccion_pizza.isdigit():
                indice_pizza = int(seleccion_pizza)
                if 1 <= indice_pizza <= len(lista_pizzas):
                    pizza_elegida = lista_pizzas[indice_pizza - 1]
                    pizza = ElementoMenu(pizza_elegida, 10.0)
                    print(f"Has elegido: {pizza_elegida}")
                    self._menu.items.append(pizza)
                    break
                else:
                    print("Número de pizza no válido. Inténtalo de nuevo.")
            else:
                print("Entrada no válida. Introduce el número de la pizza.")


    def agregar_postre(self) -> None:
        lista_postres = ["Tarta de queso", "Tarta de chocolate", "Tarta de manzana", "Tarta de zanahoria", "Tarta de limón", "Tarta de fresa", "Tarta de frambuesa", "Tarta de arándanos", "Tarta de plátano", "Tarta de pera", "Tarta de piña", "Tarta de melocotón", "Tarta de mango", "Tarta de coco", "Tarta de café", "Tarta de avellana", "Tarta de almendra", "Tarta de pistacho", "Tarta de violeta", "Tarta de menta", "Tarta de canela", "Tarta de vainilla", "Tarta de nata", "Tarta de galleta", "Tarta de caramelo", "Tarta de dulce de leche", "Tarta de moka", "Tarta de mantequilla", "Tarta de nuez", "Tarta de castaña", "Tarta de almíbar", "Tarta de merengue", "Tarta de crema", "Tarta de yogur", "Tarta de requesón", "Tarta de ricota", "Tarta de mascarpone", "Tarta de queso cottage", "Tarta de queso de cabra", "Tarta de queso azul", "Tarta de queso de untar", "Tarta de queso fresco", "Tarta de queso curado", "Tarta de queso semicurado", "Tarta de queso añejo"]
        print("Postres disponibles: ")
        for i, postre in enumerate(lista_postres, 1):
            print(f"{i}. {postre}")

        postre = None

        while True:
            seleccion_postre = input("Elige el número del postre que quieres o introduce '0' si no quieres postre: ")
            if seleccion_postre == '0':
                break
            elif seleccion_postre.isdigit():
                indice_postre = int(seleccion_postre)
                if 1 <= indice_postre <= len(lista_postres):
                    postre_elegido = lista_postres[indice_postre - 1]
                    postre = ElementoMenu(postre_elegido, 3.0)
                    print(f"Has elegido: {postre_elegido}")
                    self._menu.items.append(postre)
                    break
                else:
                    print("Número de postre no válido. Inténtalo de nuevo.")
            else:
                print("Entrada no válida. Introduce el número del postre o '0'.")


    def agregar_combo(self, sub_menu: Menu) -> None:
        self._menu.items.append(sub_menu)

    def obtener_menu(self) -> Menu:
        return self._menu


class DirectorMenu:
    def __init__(self, constructor: ConstructorMenu) -> None:
        self._constructor = constructor

    def construir_menu(self) -> None:
        self._constructor.construir_menu()
        print("Construyendo el menú:")
        self._constructor.agregar_entrada()
        self._constructor.agregar_pizza()
        self._constructor.agregar_bebida()
        self._constructor.agregar_postre()
        desea_combo = input("¿Desea un combo para 2 personas? (si/no): ")
        if desea_combo.lower() == "si":
            sub_menu = Menu("Combo Pareja")
            for _ in range(2):
                self._constructor.agregar_combo(sub_menu)
            descuento_combo = 2.0  # Descuento de $2 para el combo pareja
            for item in sub_menu.items:
                item.precio -= descuento_combo
            print("¡Combo Pareja agregado con descuento!")

# Ejemplo de uso
constructor = ConstructorMenuConcreto()
director = DirectorMenu(constructor)
director.construir_menu()
menu = constructor.obtener_menu()

# Calcular el precio total del menú
precio_total = 0.0
for elemento in menu.items:
    if isinstance(elemento, Menu):
        for sub_elemento in elemento.items:
            precio_total += sub_elemento.precio
    else:
        precio_total += elemento.precio

print(f"\nDetalles del Menú: {menu.codigo}")
for elemento in menu.items:
    if isinstance(elemento, Menu):
        print(f"Código del Combo: {elemento.codigo}")
        for sub_elemento in elemento.items:
            print(f"  - {sub_elemento.nombre}: ${sub_elemento.precio}")
    else:
        print(f"- {elemento.nombre}: ${elemento.precio}")

print("Precio del Menú: $" + str(precio_total))
