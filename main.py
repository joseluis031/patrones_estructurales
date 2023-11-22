from composite_menu import *
from clientw3 import *

from pedir import *



if __name__ == "__main__":
    
    pedido_anterior = input("¿Has hecho algún pedido anteriormente? (si/no): ")
    
    if pedido_anterior.lower() == "si":
        buscar_pedido_anterior()
        pedido1() 
        exit()    
                
    else:
        pedido1()
        exit()