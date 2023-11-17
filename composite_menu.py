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
    
    def __init__(self, pizza: str, precio: float) -> None:
        self._pizza = pizza
        self._precio = precio
        
    def buscar_preciopizza(self, pizza):
        with open('precio_elemento.csv', newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                if pizza in row:
                    return row[1]

    def operation(self) -> str:
        return f"{self._pizza} cuesta:  {self._precio}€"

    
class Leaf_bebida(Component_menu):

    def __init__(self, bebida: str, precio: float) -> None:
        self._bebida = bebida
        self._precio = precio
    
    
    def operation(self) -> str:
        return f"{self._bebida} cuesta:  {self._precio}€"
    
class Leaf_entrante(Component_menu):

    def __init__(self, entrante: str, precio: float) -> None:
        self._entrante = entrante
        self._precio = precio
        

    def operation(self) -> str:
        return f"{self._entrante} cuesta:  {self._precio}€"
    
    
class Leaf_postre(Component_menu):

    def __init__(self, postre: str, precio: float) -> None:
        self._postre = postre
        self._precio = precio
        

    def operation(self) -> str:
        return f"{self._postre} cuesta:  {self._precio}€"


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
    
    
    