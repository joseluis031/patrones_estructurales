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
                    return f"El precio de {self._pizza} es {row[1]}"

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
                    return f"El precio de {self._bebida} es {row[4]}"
                
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
                    return f"El precio de {self._entrante} es {row[10]}" 
                
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
                    return f"El precio de {self._postre} es {row[7]}"
                
    def precio(self) -> float:
        with open('precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if self._postre in row[6]:
                    return float(row[7])


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
    
    bienvenida = input("¿Que deseas(1,2,3 o 4): 1. Crear tu propio menu, 2. Elegir un menu ya creado, 3. Un producto suelto o 4. Nada ")
    
    
    if bienvenida == "1":
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
        
           
        pedido1_pizza = Leaf_pizza(pizza)
        pedido1_bebida = Leaf_bebida(bebida)
        pedido1_entrante = Leaf_entrante(entrante)
        pedido1_postre = Leaf_postre(postre)

        # Calcular precio total del menú
        precio_total_menu = pedido1_pizza.precio() + pedido1_bebida.precio() + pedido1_entrante.precio() + pedido1_postre.precio()
        print("El precio de tu pizza es: ", pedido1_pizza.precio())
        print("El precio de tu bebida es: ", pedido1_bebida.precio())
        print("El precio de tu entrante es: ", pedido1_entrante.precio())
        print("El precio de tu postre es: ", pedido1_postre.precio())
        
        
        print(f"El precio total del menú es: {precio_total_menu}")
        
 
        
    if bienvenida == "2":
        print("Tenemos los siguientes menus:")
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
            print(f"El precio total del menú basico es: {precio_total_menu}")
            
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
            
            print(f"El precio total del menú EEUU es: {precio_total_menu}")
            
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
            
            print(f"El precio total del menú italiano es: {precio_total_menu}")
            
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
            
            print(f"El precio total del menú  español es: {precio_total_menu}")
            
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
            
            print(f"El precio total del menú frances es: {precio_total_menu}")
            
    
    elif bienvenida == "3":
        print("Tenemos los siguientes productos: 1. Bebida, 2. Entrante, 3. Postre")
        producto = input("Elige el numero del producto que quieres: ")
        lista_producto = ["1", "2", "3"]
        while producto not in lista_producto:
            producto = input("No tenemos esa, ¿que producto quieres? ")
            
        if producto == "1":
            bebida = input("¿que bebida quieres? Tenemos: coca-cola, fanta, agua o aa :")
            lista_bebida = ["coca-cola", "fanta", "agua", "aa"]
            while bebida not in lista_bebida:
                bebida = input("No tenemos esa, ¿que bebida quieres? ")
            pedido1_bebida = Leaf_bebida(bebida)
            print("El precio de tu bebida es: ", pedido1_bebida.precio())
            
        elif producto == "2":
            entrante = input("¿que entrante quieres? Tenemos: patatas, calamares, ensalada o aa :")
            lista_entrante = ["patatas", "calamares", "ensalada", "aa"]
            while entrante not in lista_entrante:
                entrante = input("No tenemos esa, ¿que entrante quieres? ")
            pedido1_entrante = Leaf_entrante(entrante)
            print("El precio de tu entrante es: ", pedido1_entrante.precio())
            
        elif producto == "3":
            postre = input("¿que postre quieres? Tenemos: tarta de queso, tarta de chocolate, helado o a :")
            lista_postre = ["tarta de queso", "tarta de chocolate", "helado", "a"]
            while postre not in lista_postre:
                postre = input("No tenemos esa, ¿que postre quieres? ")
            pedido1_postre = Leaf_postre(postre)
            print("El precio de tu postre es: ", pedido1_postre.precio())
            
        
        
        
    
         
    else:
        print("Vale, adios")
        exit()
        