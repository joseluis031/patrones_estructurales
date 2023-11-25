from abc import ABC, abstractmethod
from typing import List

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

    def __init__(self):
        self._children = List[Component] = []
    
    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self
        
    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None
    
    def operation(self) -> str:
        result = []
        for child in self._children:
            result.append(child.operation())
        return result
            
        
class Documentos_Leaf(Component):
    def __init__(self, nombre) -> None:
        self._nombre = nombre
        
    def operation(self):
        return self._nombre

class Enlace_Leaf(Component):
    def __init__(self, nombre) -> None:
        self._nombre = nombre
        
    def operation(self):
        return self._nombre


class Proxy(Subject):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: Subject) -> None:
    """
    The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, you
    can extend your proxy from the real subject's class.
    """

    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)