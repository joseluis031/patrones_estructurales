from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

#Tras el éxito inicial de su plataforma digital de creación y gestión de pizzas gourmet personalizadas, la cadena "Delizioso" desea llevar su propuesta al siguiente nivel. Ahora, aparte de permitir la personalización individual de pizzas, quiere ofrecer a sus clientes la posibilidad de combinar sus creaciones en menús personalizados, que podrían incluir entradas, bebidas, pizzas y postres. Estos menús pueden ser creados tanto por el cliente como por el equipo culinario de "Delizioso", con opciones preestablecidas que representan la esencia de la marca.

#Objetivos:

#Desarrollo de Menús Personalizados:
#Introducir la noción de un "menú", que puede contener varios elementos: entradas, bebidas, pizzas (que ya han sido definidas previamente con su sistema de creación de pizzas) y postres.
#Un "menú" puede ser simple (contener elementos básicos) o compuesto (incluir otros menús más pequeños, como un "Combo Pareja" que incluye dos menús individuales).
#Cada "menú" tendrá un código único y un precio, que se determina como la suma de los precios de sus elementos, con un descuento según la promoción aplicada.

#Desarrollo de Promociones:
#Introducir la noción de "promoción", que puede ser aplicada a un menú para ofrecer un descuento sobre su precio.
#Una promoción puede ser simple (descuento fijo) o compuesta (descuento porcentual).
#Cada promoción tendrá un código único y un descuento asociado, que se aplicará al precio del menú.

#Desarrollo de Pedidos:
#Introducir la noción de "pedido", que puede contener varios menús.
#Cada pedido tendrá un código único, un cliente asociado
#(que puede ser un usuario registrado o un cliente anónimo) y un precio total, que se determina como la suma de los precios de sus menús, con los descuentos de las promociones aplicadas.

#Desarrollo de la Interfaz de Usuario:
#Introducir la noción de "usuario", que puede ser registrado o anónimo.
#Un usuario registrado tendrá un nombre, un nombre de usuario y una contraseña.
#Un usuario anónimo tendrá un nombre de usuario y una contraseña genéricos.


#El usuario registrado podrá:
#Iniciar sesión con su nombre de usuario y contraseña.
#Ver su historial de pedidos.
#Crear un nuevo pedido, que puede contener varios menús.

#El usuario anónimo podrá:
#registrarse
#Crear un nuevo pedido, que puede contener varios menús.

#El sistema debe:
#Guardar el historial de pedidos en un archivo CSV.
#Guardar el registro de usuarios en un archivo CSV.
#Guardar el registro de menús en un archivo CSV.
#Guardar el registro de promociones en un archivo CSV.

#El sistema debe permitir al usuario elegir entre las siguientes opciones:
#Iniciar sesión.
#Registrarse.
#Crear un nuevo pedido.
#Ver historial de pedidos.



class Builder(ABC): 
    """
    La interfaz Builder especifica métodos para crear las diferentes partes de
     los objetos del Producto.
    """

    @property #Este es un decorador que permite acceder al método como si fuera un atributo.
    @abstractmethod
    def product_menu(self) -> None:
        pass

    @abstractmethod
    def tipo_de_pizza(self) -> None:
        pass

    @abstractmethod
    def bebida(self) -> None:
        pass

    @abstractmethod
    def entrante(self) -> None:
        pass
    
    @abstractmethod
    def postre(self) -> None:
        pass
    

class ConcreteBuilder1(Builder):
    
    def __init__(self) -> None:
        """
        Una instancia de constructor concreto debe estar asociada con un objeto
         de producto en particular. Una instancia de constructor concreto no debe
         estar vinculado a productos de otro tipo.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Menu1()

    @property
    def product_menu(self) -> Menu1:
        """
        El constructor concreto debe proporcionar su propia implementación de
         los pasos de construcción del producto. Tenga en cuenta que estos pasos
         puede haber sido ya implementado, por ejemplo, por una clase de producto
         abstracto.
        """
        product = self._product
        self.reset()
        return product

    def tipo_de_pizza(self) -> None:
        self._product.add("Pizza de masa fina")

    def bebida(self) -> None:
        self._product.add("Agua")

    def entrante(self) -> None:
        self._product.add("Ensalada")

    def postre(self) -> None:
        self._product.add("Tiramisú")
        
class ConcreteBuilder2(Builder):
        
        def __init__(self) -> None:
            """
            Una instancia de constructor concreto debe estar asociada con un objeto
            de producto en particular. Una instancia de constructor concreto no debe
            estar vinculado a productos de otro tipo.
            """
            self.reset()
    
        def reset(self) -> None:
            self._product = Menu2()
    
        @property
        def product_menu(self) -> Menu2:
            """
            El constructor concreto debe proporcionar su propia implementación de
            los pasos de construcción del producto. Tenga en cuenta que estos pasos
            puede haber sido ya implementado, por ejemplo, por una clase de producto
            abstracto.
            """
            product = self._product
            self.reset()
            return product
    
        def tipo_de_pizza(self) -> None:
            self._product.add("Pizza de masa gruesa")
    
        def bebida(self) -> None:
            self._product.add("Cerveza")
    
        def entrante(self) -> None:
            self._product.add("Patatas fritas")
    
        def postre(self) -> None:
            self._product.add("Tarta de queso")
            
class ConcreteBuilder3(Builder):
    
    def __init__(self) -> None:
        """
        Una instancia de constructor concreto debe estar asociada con un objeto
         de producto en particular. Una instancia de constructor concreto no debe
         estar vinculado a productos de otro tipo.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Menu3()

    @property
    def product_menu(self) -> Menu3:
        """
        El constructor concreto debe proporcionar su propia implementación de
         los pasos de construcción del producto. Tenga en cuenta que estos pasos
         puede haber sido ya implementado, por ejemplo, por una clase de producto
         abstracto.
        """
        product = self._product
        self.reset()
        return product

    def tipo_de_pizza(self) -> None:
        self._product.add("Pizza de masa fina")

    def bebida(self) -> None:
        self._product.add("Refresco")

    def entrante(self) -> None:
        self._product.add("Ensalada")

    def postre(self) -> None:
        self._product.add("Tiramisú")
        
        
        
class Menu1:
    """
    Es útil tener una clase de producto donde pueda configurar el producto.
    """
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)
        
    def list_parts(self):
        print(f"Partes del menú: {', '.join(self.parts)}", end="")
        
class Menu2:
    """
    Es útil tener una clase de producto donde pueda configurar el producto.
    """
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)
        
    def list_parts(self):
        print(f"Partes del menú: {', '.join(self.parts)}", end="")
        
        
class Menu3:
    """
    Es útil tener una clase de producto donde pueda configurar el producto.
    """
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)
        
    def list_parts(self):
        print(f"Partes del menú: {', '.join(self.parts)}", end="")
        
        
class Director:
    """
    El director solo funciona con el constructor, evitando así dependencias
    concretas de productos.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        """
        El director funciona con cualquier instancia de constructor que el código del cliente
        pasa a él. De esta manera, el código del cliente puede alterar el tipo final
        del producto recién ensamblado.
        """
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        El director funciona con cualquier instancia de constructor que el código del cliente
        pasa a él. De esta manera, el código del cliente puede alterar el tipo final
        del producto recién ensamblado.
        """
        self._builder = builder

    """
    El director puede construir varias configuraciones de producto utilizando el mismo
    pasos de construcción.
    """

    def build_menu1(self) -> None:
        self.builder.tipo_de_pizza()
        self.builder.bebida()
        self.builder.entrante()
        self.builder.postre()
        
    def build_menu2(self) -> None:
        self.builder.tipo_de_pizza()
        self.builder.bebida()
        self.builder.entrante()
        self.builder.postre()
           
        
    def build_menu3(self) -> None:
        self.builder.tipo_de_pizza()
        self.builder.bebida()
        self.builder.entrante()
        self.builder.postre()
        

if __name__ == "__main__":
    """
    El código del cliente crea un objeto constructor, lo pasa al director y luego
    inicia el proceso de construcción. El resultado final se recupera del
    objeto constructor.
    """
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder
    
    director2 = Director()
    builder2 = ConcreteBuilder2()
    director2.builder = builder2
    
    director3 = Director()
    builder3 = ConcreteBuilder3()
    director3.builder = builder3

    print("Menú 1:")
    director.build_menu1()
    builder.product_menu.list_parts()
    
    print("\n")

    print("Menú 2:")
    director2.build_menu2()
    builder2.product_menu.list_parts()
    
    print("\n")

    print("Menú 3:")
    director3.build_menu3()
    builder3.product_menu.list_parts()
    
    