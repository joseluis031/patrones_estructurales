from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import csv
from builder_pizza import *
from usuario_builder import *

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
    
    def __init__(self, nombre) -> None:
        self._nombre = nombre
        
        
    def operation(self):
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._nombre in row:
                    return self._nombre

    def precio(self) -> float:
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._nombre in row:
                    return float(row[1])
                
class Leaf_pizza_personalizada(Component_menu):
    def __init__(self, nombre) -> None:
        self._nombre = nombre
        
    
        
    def operation(self):
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._nombre in row:
                    return self._nombre
        
    def precio(self) -> float:
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._nombre in row:
                    return float(row[1])
     
    def pedir_pizza(self):   
        usuario = Usuariobu()
        builder = ConcreteBuilder1()
        usuario.builder = builder


        usuario.pedir_pizza()
        builder.product_pizza.list_parts()
    def elementos(self):
        usuario = Usuariobu()
        builder = ConcreteBuilder1()
        usuario.builder = builder
         # Obtén las elecciones del cliente como una lista de strings
        detalles_pizza = usuario.builder.product_pizza.parts
        
        # Muestra las elecciones del cliente
        return detalles_pizza
        # Guarda el pedido del cliente

    
    
class Leaf_bebida(Component_menu):

    def __init__(self, nombre) -> None:
        self._nombre = nombre
    
    
    def operation(self):
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._nombre in row[3]:
                    return self._nombre
                
    def precio(self) -> float:
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._nombre in row[3]:
                    return float(row[4])
    
class Leaf_entrante(Component_menu):

    def __init__(self, nombre) -> None:
        self._nombre = nombre
        

    def operation(self):
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._nombre in row[9]:
                    return self._nombre
                
    def precio(self) -> float:
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._nombre in row[9]:
                    return float(row[10])
    
class Leaf_postre(Component_menu):

    def __init__(self, nombre) -> None:
        self._nombre = nombre
        

    def operation(self):
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._nombre in row[6]:
                    return self._nombre
                
    def precio(self) -> float:
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._nombre in row[6]:
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


