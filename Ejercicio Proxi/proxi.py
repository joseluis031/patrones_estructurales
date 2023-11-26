from abc import ABC, abstractmethod
from typing import List
from datetime import datetime

class Component(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def operation(self) -> None:
        pass


class Carpeta(Component):

    def __init__(self, name):
        self.name = name
        self._children = []
    
    def add(self, component: Component) -> None:
        self._children.append(component)
        
    def remove(self, component: Component) -> None:
        self._children.remove(component)
    
    def operation(self) -> str:
        results = [f"Composite: {self.name}"]
        for child in self._children:
            results.append(child.operation())
        return '\n'.join(results)
            
        
class Documentos_Leaf(Component):
    def __init__(self, nombre, tipo_documento, tamaño):
        self.nombre = nombre
        self.tipo_documento = tipo_documento
        self.tamaño = tamaño
        
    def operation(self):
        return  f"Leaf: {self.nombre} ({self.tipo_documento}, {self.tamaño} KB)"

class Enlace_Leaf(Component):
    def __init__(self, nombre, link):
        self.nombre = nombre
        self.link = link
        
    def operation(self):
        return f"Enlace: {self.nombre} -> {self.link}"


class Proxy(Component):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_subject):
        self.real_subject = real_subject
        self.access_log = {}

    def operation(self):
        document_name = self.real_subject.nombre
        if self.check_access(document_name):
            self.real_subject.operation()
            self.access_log[document_name] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       
    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True





 