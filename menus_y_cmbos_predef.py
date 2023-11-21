from composite_menu import *
from clientw3 import *
from obtener_productos import *



def combo3():
    
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
        

        
        # Guardar el pedido del cliente
        Cliente.guardar_combo_menu(combo1._children, "Combo Maxi")    