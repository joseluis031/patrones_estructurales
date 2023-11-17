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
    



class Leaf_pizza(Component_menu):
    
    def __init__(self, pizza) -> None:
        self._pizza = pizza
        
    def operation(self):
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._pizza in row:
                    return f"El precio de {self._pizza} es {row[1]}"


    
class Leaf_bebida(Component_menu):

    def __init__(self, bebida) -> None:
        self._bebida = bebida
    
    
    def operation(self):
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._bebida in row[3]:
                    return f"El precio de {self._bebida} es {row[4]}"
    
class Leaf_entrante(Component_menu):

    def __init__(self, entrante) -> None:
        self._entrante = entrante
        

    def operation(self):
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._entrante in row[9]:
                    return f"El precio de {self._entrante} es {row[10]}" 
    
class Leaf_postre(Component_menu):

    def __init__(self, postre) -> None:
        self._postre = postre
        

    def operation(self):
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._postre in row[6]:
                    return f"El precio de {self._postre} es {row[7]}"


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
        return sum(results)


def client_code(component: Component_menu) -> None:
    """
    The client code works with all of the components via the base interface.
    """

    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Component_menu, component2: Component_menu) -> None:
    """
    Thanks to the fact that the child-management operations are declared in the
    base Component class, the client code can work with any component, simple or
    complex, without depending on their concrete classes.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    
    
    bienvenida = input("¿quieres un menu? (si/no) ")
    
    if bienvenida == "si":
        print("Vamos a ello!!")
        pizza = input("¿que pizza quieres? Tenemos:  margarita, barbacoa, 4 quesos, carbonara, hawaiana, romana, 4 estaciones, vegetal, napolitana o a :")
        lista_pizza = [ "margarita", "barbacoa", "4 quesos", "carbonara", "hawaiana", "romana", "4 estaciones", "vegetal", "napolitana", "a"]
        while pizza not in lista_pizza:
            pizza = input("No tenemos esa, ¿que pizza quieres? ")
            
        bebida = input("¿que bebida quieres? Tenemos: coca-cola, fanta, agua o aa :")
        lista_bebida = ["coca-cola", "fanta", "agua", "aa"]
        while bebida not in lista_bebida:
            bebida = input("No tenemos esa, ¿que bebida quieres? ")
            
        entrante = input("¿que entrante quieres? Tenemos: patatas, calamares, ensalada o aa :")
        lista_entrante = ["patatas", "calamares", "ensalada", "aa"]
        while entrante not in lista_entrante:
            entrante = input("No tenemos esa, ¿que entrante quieres? ")
            
        postre = input("¿que postre quieres? Tenemos: tarta de queso, tarta de chocolate, helado o a :")
        lista_postre = ["tarta de queso", "tarta de chocolate", "helado", "a"]
        while postre not in lista_postre:
            postre = input("No tenemos esa, ¿que postre quieres? ")
        
        print ("Tu pedido es: ", pizza, bebida, entrante, postre, " y el precio total es: ")
            
        
        
        
        
            
        pedido1_pizza = Leaf_pizza(pizza)
        print(pedido1_pizza.operation())
        
        pedido1_bebida = Leaf_bebida(bebida)
        print(pedido1_bebida.operation())
        
        pedido1_entrante = Leaf_entrante(entrante)
        print(pedido1_entrante.operation())
        
        pedido1_postre = Leaf_postre(postre)
        print(pedido1_postre.operation())
        
        
        
        
        
    
    
    
    
    else:
        print("hasta otra")
        exit()