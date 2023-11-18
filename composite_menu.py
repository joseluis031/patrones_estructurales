from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import csv

class Component_menu(ABC):


    @property
    def parent(self) -> Component_menu:
        return self._parent

    @parent.setter
    def parent(self, parent: Component_menu):
        self._parent = parent

    def add(self, component: Component_menu) -> None:
        pass

    def remove(self, component: Component_menu) -> None:
        pass


    @abstractmethod
    def operation(self) -> str:
        pass
    
    @abstractmethod
    def precio(self) -> float:
        pass



class Leaf_pizza(Component_menu):
    
    def __init__(self, pizza) -> None:
        self._pizza = pizza
        
    def operation(self):
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._pizza in row:
                    return self._pizza

    def precio(self) -> float:
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._pizza in row:
                    return float(row[1])
    
class Leaf_bebida(Component_menu):

    def __init__(self, bebida) -> None:
        self._bebida = bebida
    
    
    def operation(self):
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._bebida in row[3]:
                    return self._bebida
                
    def precio(self) -> float:
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._bebida in row[3]:
                    return float(row[4])
    
class Leaf_entrante(Component_menu):

    def __init__(self, entrante) -> None:
        self._entrante = entrante
        

    def operation(self):
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._entrante in row[9]:
                    return self._entrante 
                
    def precio(self) -> float:
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._entrante in row[9]:
                    return float(row[10])
    
class Leaf_postre(Component_menu):

    def __init__(self, postre) -> None:
        self._postre = postre
        

    def operation(self):
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._postre in row[6]:
                    return self._postre
                
    def precio(self) -> float:
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._postre in row[6]:
                    return float(row[7])

class Composite_menu(Component_menu):
        
    
        def __init__(self, menu) -> None:
            self._menu = menu
            self._children: List[Component_menu] = []
    
    
        def add(self, component: Component_menu) -> None:
            self._children.append(component)
            component.parent = self
    
        def remove(self, component: Component_menu) -> None:
            self._children.remove(component)
            component.parent = None
    
    
        def operation(self) -> str:
    
            results = []
            for child in self._children:
                results.append(child.operation())
            return f"({'+'.join(results)})"
    
        def precio(self) -> float:
            results = []
            for child in self._children:
                results.append(child.precio())
            return sum(results)-sum(results)*0.05 #descuento por pedir menu predeterminado

class Composite_combo1(Component_menu):
    

    def __init__(self, combo1) -> None:
        self._combo1 = combo1
        self._children: List[Component_menu] = []


    def add(self, component: Component_menu) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component_menu) -> None:
        self._children.remove(component)
        component.parent = None


    def operation(self) -> str:

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Precio del Combo: ({'+'.join(results)})"
    
    def precio(self) -> float:
        results = []
        for child in self._children:
            results.append(child.precio())
        return sum(results)-sum(results)*0.15 #descuento por pedir combo


def obtener_pizza() -> str:
    lista_pizza = ["margarita", "barbacoa", "4 quesos", "carbonara", "hawaiana", "romana", "4 estaciones", "vegetal", "napolitana", "a"]
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




if __name__ == "__main__":
    
    bienvenida = input("¿Que deseas(1,2,3,4 0 5): 1. Crear tu propio menu, 2. Elegir un menu ya creado, 3. Un producto suelto, 4. Un Combo o 5. Nada ")
    
    
    if bienvenida == "1":
        menu_personalizado = crear_menu_personalizado()

        # Calcular precio total del menú personalizado
        precio_total_menu_personalizado = sum(item.precio() for item in menu_personalizado)
        print("Detalles del menú personalizado:")
        for item in menu_personalizado:
            print(f"{item.operation()} - Precio: {item.precio()}")
        print(f"El precio total del menú personalizado es: {precio_total_menu_personalizado}")
        exit()

        
 
        
    if bienvenida == "2":
        print("Tenemos los siguientes menus(cada menu ya creado tiene 5% descontado del precio total final):")
        print("1. Menu basico: alitas, Pizza margarita, agua y helado")
        print("2. Menu EEUU: patatas, Pizza barbacoa, coca-cola y tarta de queso")
        print("3. Menu italiano: calamares, Pizza 4 quesos, vino y helado")
        print("4. Menu español: ensalada, Pizza carbonara, agua y tarta de chocolate")
        print("5. Menu frances: patatas, Pizza hawaiana, coca-cola y helado")
        menu = input("Elige el numero del menu que quieres: ")
        lista_menu = ["1", "2", "3", "4", "5"]
        while menu not in lista_menu:
            menu = input("No tenemos esa, ¿que menu quieres? ")
            
        if menu == "1":
            pedido1_pizza = Leaf_pizza("margarita")
            pedido1_bebida = Leaf_bebida("agua")
            pedido1_entrante = Leaf_entrante("alitas de pollo")
            pedido1_postre = Leaf_postre("helado")
            
            # Calcular precio total del menú
            precio_total_menu = pedido1_pizza.precio() + pedido1_bebida.precio() + pedido1_entrante.precio() + pedido1_postre.precio()
            print("El precio de tu pizza es: ", pedido1_pizza.precio())
            print("El precio de tu bebida es: ", pedido1_bebida.precio())
            print("El precio de tu entrante es: ", pedido1_entrante.precio())
            print("El precio de tu postre es: ", pedido1_postre.precio())
            descuento = precio_total_menu*0.05
            precio_final = precio_total_menu - descuento
            print(f"El precio total del menú basico es: {precio_final}")
            
        elif menu == "2":
            pedido1_pizza = Leaf_pizza("barbacoa")
            pedido1_bebida = Leaf_bebida("coca-cola")
            pedido1_entrante = Leaf_entrante("patatas")
            pedido1_postre = Leaf_postre("tarta de queso")
            
            # Calcular precio total del menú
            precio_total_menu = pedido1_pizza.precio() + pedido1_bebida.precio() + pedido1_entrante.precio() + pedido1_postre.precio()
            print("El precio de tu pizza es: ", pedido1_pizza.precio())
            print("El precio de tu bebida es: ", pedido1_bebida.precio())
            print("El precio de tu entrante es: ", pedido1_entrante.precio())
            print("El precio de tu postre es: ", pedido1_postre.precio())
            descuento = precio_total_menu*0.05
            precio_final = precio_total_menu - descuento
            
            print(f"El precio total del menú EEUU es: {precio_final}")
            
        elif menu == "3":
            pedido1_pizza = Leaf_pizza("4 quesos")
            pedido1_bebida = Leaf_bebida("vino")
            pedido1_entrante = Leaf_entrante("calamares")
            pedido1_postre = Leaf_postre("helado")
            
            # Calcular precio total del menú
            precio_total_menu = pedido1_pizza.precio() + pedido1_bebida.precio() + pedido1_entrante.precio() + pedido1_postre.precio()
            print("El precio de tu pizza es: ", pedido1_pizza.precio())
            print("El precio de tu bebida es: ", pedido1_bebida.precio())
            print("El precio de tu entrante es: ", pedido1_entrante.precio())
            print("El precio de tu postre es: ", pedido1_postre.precio())
            descuento = precio_total_menu*0.05
            precio_final = precio_total_menu - descuento
            
            print(f"El precio total del menú italiano es: {precio_final}")
            
        elif menu == "4":
            pedido1_pizza = Leaf_pizza("carbonara")
            pedido1_bebida = Leaf_bebida("agua")
            pedido1_entrante = Leaf_entrante("ensalada")
            pedido1_postre = Leaf_postre("tarta de chocolate")
            
            # Calcular precio total del menú
            precio_total_menu = pedido1_pizza.precio() + pedido1_bebida.precio() + pedido1_entrante.precio() + pedido1_postre.precio()
            print("El precio de tu pizza es: ", pedido1_pizza.precio())
            print("El precio de tu bebida es: ", pedido1_bebida.precio())
            print("El precio de tu entrante es: ", pedido1_entrante.precio())
            print("El precio de tu postre es: ", pedido1_postre.precio())
            descuento = precio_total_menu*0.05
            precio_final = precio_total_menu - descuento
            
            print(f"El precio total del menú  español es: {precio_final}")
            
        elif menu == "5":
            pedido1_pizza = Leaf_pizza("hawaiana")
            pedido1_bebida = Leaf_bebida("coca-cola")
            pedido1_entrante = Leaf_entrante("patatas")
            pedido1_postre = Leaf_postre("helado")
            
            # Calcular precio total del menú
            precio_total_menu = pedido1_pizza.precio() + pedido1_bebida.precio() + pedido1_entrante.precio() + pedido1_postre.precio()
            print("El precio de tu pizza es: ", pedido1_pizza.precio())
            print("El precio de tu bebida es: ", pedido1_bebida.precio())
            print("El precio de tu entrante es: ", pedido1_entrante.precio())
            print("El precio de tu postre es: ", pedido1_postre.precio())
            descuento = precio_total_menu*0.05
            precio_final = precio_total_menu - descuento
            
            print(f"El precio total del menú frances es: {precio_final}")
            
    
    elif bienvenida == "3":
        print("Tenemos los siguientes productos: 1. Bebida, 2. Entrante, 3. Postre")
        producto = input("Elige el numero del producto que quieres: ")
        lista_producto = ["1", "2", "3"]
        while producto not in lista_producto:
            producto = input("No tenemos esa, ¿que producto quieres? ")
            
        if producto == "1":
            bebida = obtener_bebida()
            pedido1_bebida = Leaf_bebida(bebida)
            print("El precio de tu ",pedido1_bebida.operation()," es: ", pedido1_bebida.precio())
            
        elif producto == "2":
            entrante = obtener_entrante()
            pedido1_entrante = Leaf_entrante(entrante)
            print("El precio de tu ",pedido1_entrante.operation()," es: ", pedido1_entrante.precio())
            
        elif producto == "3":
            postre = obtener_postre()
            pedido1_postre = Leaf_postre(postre)
            print("El precio de tu ",pedido1_postre.operation()," es: ", pedido1_postre.precio())
            
        
        
        
    elif bienvenida == "4":
        print("Los combos tienen un 15% de descuento respecto del precio total")
        print("Tenemos los siguientes combos:")
        print("1. Combo Pareja: 2 pizzas: margarita y 4 quesos, 2 refrescos, aceitunas y croquetas  y 2 helados")
        print("2. Combo Familiar: 2 pizzas margarita y 2 barbacoa, 2 aguas y 2 refrescos, 2 alitas y 2 de patatas y 4 tartas de queso")
        print("3. Combo Maxi muerte por chocolat: 6 pizzas barbacoa, 6 agua, 6 alitas de pollo y 6 tarta de chocolate")
        combo = input("Elige el numero del combo que quieres: ")
        lista_combo = ["1", "2", "3"]
        while combo not in lista_combo:
            combo = input("No tenemos esa, ¿que combo quieres? ")
            
        if combo == "1":
            combo1 = Composite_combo1("Combo Pareja")
            pedido1_pizza = Leaf_pizza("margarita")
            pedido1_pizza2 = Leaf_pizza("4 quesos")
            pedido1_bebida = Leaf_bebida("fanta")
            pedido1_bebida2 = Leaf_bebida("coca-cola")
            pedido1_entrante = Leaf_entrante("aceitunas")
            pedido1_entrante2 = Leaf_entrante("croquetas")
            pedido1_postre = Leaf_postre("helado")
            pedido1_postre2 = Leaf_postre("helado")
            
            
            combo1.add(pedido1_pizza)
            combo1.add(pedido1_pizza2)

            combo1.add(pedido1_bebida)
            combo1.add(pedido1_bebida2)
            combo1.add(pedido1_entrante)
            combo1.add(pedido1_entrante2)
            
            combo1.add(pedido1_postre)
            combo1.add(pedido1_postre2)
            
            print(f"El precio total del combo pareja es: {combo1.precio()}")
            
        elif combo == "2":
            combo1 = Composite_combo1("Combo Familiar")
            pedido1_pizza = Leaf_pizza("margarita")
            pedido1_pizza2 = Leaf_pizza("barbacoa")
            pedido1_pizza3 = Leaf_pizza("margarita")
            pedido1_pizza4   = Leaf_pizza("barbacoa")
            pedido1_bebida = Leaf_bebida("agua")
            pedido1_bebida2 = Leaf_bebida("agua")
            pedido1_bebida3 = Leaf_bebida("coca-cola")
            pedido1_bebida4 = Leaf_bebida("coca-cola")
            
            pedido1_entrante = Leaf_entrante("alitas de pollo")
            pedido1_entrante2 = Leaf_entrante("alitas de pollo")
            pedido1_entrante3 = Leaf_entrante("patatas")
            pedido1_entrante4 = Leaf_entrante("patatas")
            
            
            pedido1_postre = Leaf_postre("tarta de queso")
            pedido1_postre2 = Leaf_postre("tarta de queso")
            pedido1_postre3 = Leaf_postre("tarta de queso")
            pedido1_postre4 = Leaf_postre("tarta de queso")
            
            
            combo1.add(pedido1_pizza)
            combo1.add(pedido1_pizza2)
            combo1.add(pedido1_pizza3)
            combo1.add(pedido1_pizza4)
            combo1.add(pedido1_bebida)
            combo1.add(pedido1_bebida2)
            combo1.add(pedido1_bebida3)
            combo1.add(pedido1_bebida4)
            combo1.add(pedido1_entrante)
            combo1.add(pedido1_entrante2)
            combo1.add(pedido1_entrante3)
            combo1.add(pedido1_entrante4)
            
            combo1.add(pedido1_postre)
            combo1.add(pedido1_postre2)
            combo1.add(pedido1_postre3)
            combo1.add(pedido1_postre4)
            
            print(f"El precio total del combo familiar es: {combo1.precio()}")
            
        elif combo == "3":
            combo1 = Composite_combo1("Combo Maxi")
            pedido1_pizza = Leaf_pizza("barbacoa")
            pedido1_pizza2 = Leaf_pizza("barbacoa")
            pedido1_pizza3 = Leaf_pizza("barbacoa")
            pedido1_pizza4   = Leaf_pizza("barbacoa")
            pedido1_pizza5 = Leaf_pizza("barbacoa")
            pedido1_pizza6 = Leaf_pizza("barbacoa")
            pedido1_bebida = Leaf_bebida("agua")
            pedido1_bebida2 = Leaf_bebida("agua")
            pedido1_bebida3 = Leaf_bebida("agua")
            pedido1_bebida4 = Leaf_bebida("agua")
            pedido1_bebida5 = Leaf_bebida("agua")
            pedido1_bebida6 = Leaf_bebida("agua")
            
            pedido1_entrante = Leaf_entrante("alitas de pollo")
            pedido1_entrante2 = Leaf_entrante("alitas de pollo")
            pedido1_entrante3 = Leaf_entrante("alitas de pollo")
            pedido1_entrante4 = Leaf_entrante("alitas de pollo")
            pedido1_entrante5 = Leaf_entrante("alitas de pollo")
            pedido1_entrante6 = Leaf_entrante("alitas de pollo")
            
            pedido1_postre = Leaf_postre("tarta de chocolate")
            pedido1_postre2 = Leaf_postre("tarta de chocolate")
            pedido1_postre3 = Leaf_postre("tarta de chocolate")
            pedido1_postre4 = Leaf_postre("tarta de chocolate")
            pedido1_postre5 = Leaf_postre("tarta de chocolate")
            pedido1_postre6 = Leaf_postre("tarta de chocolate")
            
            combo1.add(pedido1_pizza)
            combo1.add(pedido1_pizza2)
            combo1.add(pedido1_pizza3)
            combo1.add(pedido1_pizza4)
            combo1.add(pedido1_pizza5)
            combo1.add(pedido1_pizza6)
            combo1.add(pedido1_bebida)
            combo1.add(pedido1_bebida2)
            combo1.add(pedido1_bebida3)
            combo1.add(pedido1_bebida4)
            combo1.add(pedido1_bebida5)
            combo1.add(pedido1_bebida6)
            combo1.add(pedido1_entrante)
            combo1.add(pedido1_entrante2)
            combo1.add(pedido1_entrante3)
            combo1.add(pedido1_entrante4)
            combo1.add(pedido1_entrante5)
            combo1.add(pedido1_entrante6)
            combo1.add(pedido1_postre)
            combo1.add(pedido1_postre2)
            combo1.add(pedido1_postre3)
            combo1.add(pedido1_postre4)
            combo1.add(pedido1_postre5)
            combo1.add(pedido1_postre6)
            
            
            print(f"El precio total del combo maxi es: {combo1.precio()}")
            
        
         
    else:
        print("Vale, adios")
        exit()
        