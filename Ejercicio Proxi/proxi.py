from abc import ABC, abstractmethod
from typing import List
from datetime import datetime
import json


class Component(ABC):
    @abstractmethod
    def operation(self) -> None:
        pass
    
    def to_dict(self):
        raise NotImplementedError("to_dict method must be implemented in subclasses")
    
    def realizar_operacion(self):
        pass

class Carpeta(Component):
    def __init__(self, nombre):
        self.nombre = nombre
        self._children = []
    
    def add(self, component: Component) -> None:
        self._children.append(component)
        
    def remove(self, component: Component) -> None:
        self._children.remove(component)
    
    def operation(self) -> str:
        results = [f"Composite: {self.nombre}"]
        for child in self._children:
            results.append(child.operation())
        return '\n'.join(results)
    
    def to_dict(self):
        return {
            "tipo": "Carpeta",
            "nombre": self.nombre,
            "Contiene": [child.to_dict() for child in self._children]
        }
            
class Documentos_Leaf(Component):
    def __init__(self, nombre, tipo_documento, tamaño):
        self.nombre = nombre
        self.tipo_documento = tipo_documento
        self.tamaño = tamaño
        
        
    def operation(self):
        return  f"Leaf: {self.nombre} ({self.tipo_documento}, {self.tamaño} KB)"
    
    def to_dict(self):
        return {
            "tipo": "Documento",
            "nombre": self.nombre,
            "tipo_documento": self.tipo_documento,
            "tamanio": self.tamaño,
        }

class Enlace_Leaf(Component):
    def __init__(self, nombre, link):
        self.nombre = nombre
        self.link = link
        
    def operation(self):
        return f"Enlace: {self.nombre} -> {self.link}"
    
    def to_dict(self):
        return {
            "tipo": "Enlace",
            "nombre": self.nombre,
            "link": self.link
        }

class Proxy(Component):
    def __init__(self, real_subject, usuario_actual=None):
        self.real_subject = real_subject
        self.usuario_actual = usuario_actual
        self.access_log = []
        self.access_checked = False  # Flag to track if access has been checked

    def operation(self):
        document_name = self.real_subject.nombre
        if not self.access_checked:  # Check access only the first time
            self.check_access(document_name)
            self.access_checked = True
        self.real_subject.operation()
        self.log_access(document_name)
       
    def check_access(self, document_name) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.access_log.append({'Modificado por Usuario': document_name , 'timestamp': timestamp})
        return True

    def log_access(self, document_name) -> None:
        print("Proxy: Logging the time of request.", end="")

    def to_dict(self):
        return {
            'type': 'Proxy',
            'real_subject': self.real_subject.to_dict(),
            'access_log': self.access_log
        }