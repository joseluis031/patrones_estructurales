import csv
from composite_menu import *    
from obtener_productos import *
from busqueda_pedido import *

import ast
class Cliente:
    def __init__(self, nombre, usuario, contraseña):
        self.nombre = nombre
        self.usuario = usuario
        self.contraseña = contraseña

    def guardar_cliente(self):
        # Nombre del archivo CSV
        archivo_csv = 'clientes.csv'
        self.id = hash((self.nombre, self.usuario, self.contraseña))


        # Crear o abrir el archivo en modo de escritura
        with open(archivo_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            row = [self.nombre, self.usuario, self.contraseña,self.id]
            # Si el archivo está vacío, escribir las columnas
            if file.tell() == 0:
                writer.writerow(['nombre', 'usuario', 'contrasenia', 'id'])

            # Escribir la información del cliente y su pedido
            writer = csv.writer(file)
            writer.writerow(row)
            
    def guardar_pedido(self, pedido):
        # Nombre del archivo CSV para los pedidos
        archivo_pedidos = 'pedidos_cliente.csv'

        # Crear o abrir el archivo en modo de escritura
        with open(archivo_pedidos, mode='a', newline='') as file:
            writer = csv.writer(file)

            # Si el archivo está vacío, escribir las columnas
            if file.tell() == 0:
                writer.writerow(['id', 'elemento', 'precio'])

            # Escribir el pedido del cliente con su ID
            for item in pedido:
                writer.writerow([self.id, item.operation(), item.precio()])
                
    def guardar_combo_menu(self, pedido, tipo):
        archivo_pedidos = 'combos_menu.csv'

        with open(archivo_pedidos, mode='a', newline='') as file:
            writer = csv.writer(file)
            precio_total = sum(item.precio() for item in pedido)
            if precio_total < 50:
                precio_con_descuento = precio_total - precio_total * 0.05 #menu
            else:
                precio_con_descuento = precio_total - precio_total * 0.15 #combo
            if file.tell() == 0:
                writer.writerow(['id', 'tipo_pedido', 'Precio', 'Pedido'])

            # Escribir el pedido del cliente con su ID
            nombres_elementos = [item._nombre for item in pedido]

        # Escribir el pedido del cliente con su ID
            writer.writerow([self.id, tipo, precio_con_descuento, self.format_pedido_detalle(nombres_elementos)])
    def format_pedido_detalle(self, pedido):
        from collections import Counter
    
    # Obtener un contador de elementos en el pedido
        contador_elementos = Counter(pedido)
    
    # Convertir el contador en una lista de cadenas con el formato "cantidad x elemento"
        formatted_pedido = [f"{cantidad} x {elemento}" for elemento, cantidad in contador_elementos.items()]
    
        return formatted_pedido
            
        
                


                
if __name__ == "__main__":
    
    pedido_anterior = input("¿Has hecho algún pedido anteriormente? (si/no): ")
    
    if pedido_anterior.lower() == "si":
        
        
        buscar_pedido_anterior()
        
    
        nombre_cliente = input("Introduce tu nombre: ")
        nombre_usuario = input("Introduce tu nombre de usuario: ")
        contraseña = input("Introduce tu contraseña: ")   
        
        bienvenida = input("¿Qué deseas hacer (1,2,3,4,5): 1. Crear tu propio menú, 2. Elegir un menú ya creado, 3. Un producto suelto, 4. Un Combo, 5. Nada ")


        if bienvenida == "1":
            menu_personalizado = crear_menu_personalizado()

            # Calcular precio total del menú personalizado
            precio_total_menu_personalizado = sum(item.precio() for item in menu_personalizado)
            print("Detalles del menú personalizado:")
            for item in menu_personalizado:
                print(f"{item.operation()} - Precio: {item.precio()}")
            print(f"El precio total del menú personalizado es: {precio_total_menu_personalizado}")

            

            # Crear un Composite_combo1 con los elementos del menú personalizado
            pedido_cliente = Composite_menu("Menú Personalizado")
            for item in menu_personalizado:
                pedido_cliente.add(item)
            
            cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
            cliente.guardar_cliente()
            cliente.guardar_pedido(pedido_cliente._children)  # Guardar el pedido del cliente


            exit()
        # Resto del código...
        if bienvenida == "2":
            print("Tenemos los siguientes menus(cada menu ya creado tiene 5% descontado del precio total final):")
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
                
                pedido1_menu = Composite_menu("Menu basico")
                pedido1_menu.add(pedido1_pizza)
                pedido1_menu.add(pedido1_bebida)
                pedido1_menu.add(pedido1_entrante)
                pedido1_menu.add(pedido1_postre)
                
                
                
                # Calcular precio total del menú
                print("El precio de tu pizza es: ", pedido1_pizza.precio())
                print("El precio de tu bebida es: ", pedido1_bebida.precio())
                print("El precio de tu entrante es: ", pedido1_entrante.precio())
                print("El precio de tu postre es: ", pedido1_postre.precio())
                
                print("El precio total del menu basico (con descuento)es: ", pedido1_menu.precio())
                
                
                cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                cliente.guardar_cliente()

                

            # Guardar el pedido del cliente
                cliente.guardar_combo_menu(pedido1_menu._children, "Menu basico")
                
            elif menu == "2":
                pedido1_pizza = Leaf_pizza("barbacoa")
                pedido1_bebida = Leaf_bebida("coca-cola")
                pedido1_entrante = Leaf_entrante("patatas")
                pedido1_postre = Leaf_postre("tarta de queso")
                
                pedido2_menu = Composite_menu("Menu EEUU")
                pedido2_menu.add(pedido1_pizza)
                pedido2_menu.add(pedido1_bebida)
                pedido2_menu.add(pedido1_entrante)
                pedido2_menu.add(pedido1_postre)
                
                # Calcular precio total del menú
                print("El precio de tu pizza es: ", pedido1_pizza.precio())
                print("El precio de tu bebida es: ", pedido1_bebida.precio())
                print("El precio de tu entrante es: ", pedido1_entrante.precio())
                print("El precio de tu postre es: ", pedido1_postre.precio())
                
                
                print("El precio total del menu EEUU (con descuento)es: ", pedido2_menu.precio()) 
                
                cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                cliente.guardar_cliente()
                
                # Guardar el pedido del cliente
                cliente.guardar_combo_menu(pedido2_menu._children, "Menu EEUU")            
            
            elif menu == "3":
                pedido1_pizza = Leaf_pizza("4 quesos")
                pedido1_bebida = Leaf_bebida("vino")
                pedido1_entrante = Leaf_entrante("calamares")
                pedido1_postre = Leaf_postre("helado")
                
                pedido3_menu = Composite_menu("Menu italiano")
                pedido3_menu.add(pedido1_pizza)
                pedido3_menu.add(pedido1_bebida)
                pedido3_menu.add(pedido1_entrante)
                pedido3_menu.add(pedido1_postre)
                
                # Calcular precio total del menú
                print("El precio de tu pizza es: ", pedido1_pizza.precio())
                print("El precio de tu bebida es: ", pedido1_bebida.precio())
                print("El precio de tu entrante es: ", pedido1_entrante.precio())
                print("El precio de tu postre es: ", pedido1_postre.precio())
                
                
                print("El precio total del menu italiano (con descuento)es: ", pedido3_menu.precio())
                
                cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                cliente.guardar_cliente()
                
                # Guardar el pedido del cliente
                cliente.guardar_combo_menu(pedido3_menu._children, "Menu italiano")                
                            
            elif menu == "4":
                pedido1_pizza = Leaf_pizza("carbonara")
                pedido1_bebida = Leaf_bebida("agua")
                pedido1_entrante = Leaf_entrante("ensalada")
                pedido1_postre = Leaf_postre("tarta de chocolate")
                
                pedido4_menu = Composite_menu("Menu español")
                pedido4_menu.add(pedido1_pizza)
                pedido4_menu.add(pedido1_bebida)
                pedido4_menu.add(pedido1_entrante)
                pedido4_menu.add(pedido1_postre)
                
                # Calcular precio total del menú
                print("El precio de tu pizza es: ", pedido1_pizza.precio())
                print("El precio de tu bebida es: ", pedido1_bebida.precio())
                print("El precio de tu entrante es: ", pedido1_entrante.precio())
                print("El precio de tu postre es: ", pedido1_postre.precio())
                
                print(f"El precio total del menu español (con descuento)es: {pedido4_menu.precio()}")
                
                cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                cliente.guardar_cliente()
                
                # Guardar el pedido del cliente
                cliente.guardar_combo_menu(pedido4_menu._children, "Menu español")
                                            
            elif menu == "5":
                pedido1_pizza = Leaf_pizza("hawaiana")
                pedido1_bebida = Leaf_bebida("coca-cola")
                pedido1_entrante = Leaf_entrante("patatas")
                pedido1_postre = Leaf_postre("helado")
                
                pedido5_menu = Composite_menu("Menu frances")
                pedido5_menu.add(pedido1_pizza)
                pedido5_menu.add(pedido1_bebida)
                pedido5_menu.add(pedido1_entrante)
                pedido5_menu.add(pedido1_postre)
                
                # Calcular precio total del menú
                print("El precio de tu pizza es: ", pedido1_pizza.precio())
                print("El precio de tu bebida es: ", pedido1_bebida.precio())
                print("El precio de tu entrante es: ", pedido1_entrante.precio())
                print("El precio de tu postre es: ", pedido1_postre.precio())
            
                
                print(f"El precio total del menu frances (con descuento)es: {pedido5_menu.precio()}") 
                
                cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                cliente.guardar_cliente()
                
                # Guardar el pedido del cliente
                cliente.guardar_combo_menu(pedido5_menu._children, "Menu frances")
                
                                
        elif bienvenida =="3":
            print("Tenemos los siguientes productos: 1. Bebida, 2. Entrante, 3. Postre")
            producto = input("Elige el numero del producto que quieres: ")
            lista_producto = ["1", "2", "3"]
            while producto not in lista_producto:
                producto = input("No tenemos esa, ¿que producto quieres? ")
                
            if producto == "1":
                bebida = obtener_bebida()
                pedido1_bebida = Leaf_bebida(bebida)
                print("El precio de tu ",pedido1_bebida.operation()," es: ", pedido1_bebida.precio())
                
                cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                cliente.guardar_cliente()
                
                # Guardar el pedido del cliente
                cliente.guardar_pedido([pedido1_bebida])
                
            elif producto == "2":
                entrante = obtener_entrante()
                pedido1_entrante = Leaf_entrante(entrante)
                print("El precio de tu ",pedido1_entrante.operation()," es: ", pedido1_entrante.precio())
                
                cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                cliente.guardar_cliente()
                
                # Guardar el pedido del cliente
                cliente.guardar_pedido([pedido1_entrante])
                
                
            elif producto == "3":
                postre = obtener_postre()
                pedido1_postre = Leaf_postre(postre)
                print("El precio de tu ",pedido1_postre.operation()," es: ", pedido1_postre.precio())
                
                cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                cliente.guardar_cliente()

                # Guardar el pedido del cliente
                cliente.guardar_pedido([pedido1_postre])
                
        elif bienvenida =="4":
            print("Los combos tienen un 15% de descuento respecto del precio total")
            print("Tenemos los siguientes combos:")
            print("1. Combo Pareja: 2 pizzas: barbacoa y 4 quesos, 1vino y 1 champagne, calamares y croquetas  y tarta de chocolate y tarta de queso")
            print("2. Combo Familiar: 2 pizzas margarita y 2 barbacoa, 2 aguas y 2 refrescos, 2 alitas y 2 de patatas y 4 tartas de queso")
            print("3. Combo Maxi muerte por chocolat: 6 pizzas barbacoa, 6 agua, 6 alitas de pollo y 6 tarta de chocolate")
            combo = input("Elige el numero del combo que quieres: ")
            lista_combo = ["1", "2", "3"]
            while combo not in lista_combo:
                combo = input("No tenemos esa, ¿que combo quieres? ")
                
            if combo == "1":
                combo1 = Composite_combo1("Combo Pareja")
                pedido1_pizza = Leaf_pizza("barbacoa")
                pedido1_pizza2 = Leaf_pizza("4 quesos")
                pedido1_bebida = Leaf_bebida("  vino")
                pedido1_bebida2 = Leaf_bebida("champagne")
                pedido1_entrante = Leaf_entrante("calamares")
                pedido1_entrante2 = Leaf_entrante("croquetas")
                pedido1_postre = Leaf_postre("tarta de chocolate")
                pedido1_postre2 = Leaf_postre("tarta de queso")
                
                
                combo1.add(pedido1_pizza)
                combo1.add(pedido1_pizza2)

                combo1.add(pedido1_bebida)
                combo1.add(pedido1_bebida2)
                combo1.add(pedido1_entrante)
                combo1.add(pedido1_entrante2)
                
                combo1.add(pedido1_postre)
                combo1.add(pedido1_postre2)
                
                print(f"El precio total del combo pareja es: {combo1.precio()}")
                
                cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                cliente.guardar_cliente()
                
                # Guardar el pedido del cliente
                cliente.guardar_pedido(combo1._children)
                                
            elif combo == "2":
                combo1 = Composite_combo1("Combo Familiar")
                pedido1_pizza = Leaf_pizza("margarita")
                pedido1_pizza2 = Leaf_pizza("barbacoa")
                pedido1_pizza3 = Leaf_pizza("margarita")
                pedido1_pizza4   = Leaf_pizza("barbacoa")
                pedido1_bebida = Leaf_bebida("agua")
                pedido1_bebida2 = Leaf_bebida("agua")
                pedido1_bebida3 = Leaf_bebida("coca-cola")
                pedido1_bebida4 = Leaf_bebida("coca-cola")
                
                pedido1_entrante = Leaf_entrante("alitas de pollo")
                pedido1_entrante2 = Leaf_entrante("alitas de pollo")
                pedido1_entrante3 = Leaf_entrante("patatas")
                pedido1_entrante4 = Leaf_entrante("patatas")
                
                
                pedido1_postre = Leaf_postre("tarta de queso")
                pedido1_postre2 = Leaf_postre("tarta de queso")
                pedido1_postre3 = Leaf_postre("tarta de queso")
                pedido1_postre4 = Leaf_postre("tarta de queso")
                
                
                combo1.add(pedido1_pizza)
                combo1.add(pedido1_pizza2)
                combo1.add(pedido1_pizza3)
                combo1.add(pedido1_pizza4)
                combo1.add(pedido1_bebida)
                combo1.add(pedido1_bebida2)
                combo1.add(pedido1_bebida3)
                combo1.add(pedido1_bebida4)
                combo1.add(pedido1_entrante)
                combo1.add(pedido1_entrante2)
                combo1.add(pedido1_entrante3)
                combo1.add(pedido1_entrante4)
                
                combo1.add(pedido1_postre)
                combo1.add(pedido1_postre2)
                combo1.add(pedido1_postre3)
                combo1.add(pedido1_postre4)
                
                print(f"El precio total del combo familiar es: {combo1.precio()}")
                
                cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                cliente.guardar_cliente()
                
                # Guardar el pedido del cliente
                cliente.guardar_pedido(combo1._children)
                                
            elif combo == "3":
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
                
                cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                cliente.guardar_cliente()
                
                # Guardar el pedido del cliente
                cliente.guardar_pedido(combo1._children)                
            
            
        else:
            print("Vale, adios")
            exit()
    else:
            nombre_cliente = input("Introduce tu nombre: ")
            nombre_usuario = input("Introduce tu nombre de usuario: ")
            contraseña = input("Introduce tu contraseña: ")   
            
            bienvenida = input("¿Qué deseas hacer (1,2,3,4,5): 1. Crear tu propio menú, 2. Elegir un menú ya creado, 3. Un producto suelto, 4. Un Combo, 5. Nada ")


            if bienvenida == "1":
                menu_personalizado = crear_menu_personalizado()

                # Calcular precio total del menú personalizado
                precio_total_menu_personalizado = sum(item.precio() for item in menu_personalizado)
                print("Detalles del menú personalizado:")
                for item in menu_personalizado:
                    print(f"{item.operation()} - Precio: {item.precio()}")
                print(f"El precio total del menú personalizado es: {precio_total_menu_personalizado}")

                

                # Crear un Composite_combo1 con los elementos del menú personalizado
                pedido_cliente = Composite_menu("Menú Personalizado")
                for item in menu_personalizado:
                    pedido_cliente.add(item)
                
                cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                cliente.guardar_cliente()
                cliente.guardar_pedido(pedido_cliente._children)  # Guardar el pedido del cliente


                exit()
            if bienvenida == "2":
                print("Tenemos los siguientes menus(cada menu ya creado tiene 5% descontado del precio total final):")
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
                    
                    pedido1_menu = Composite_menu("Menu basico")
                    pedido1_menu.add(pedido1_pizza)
                    pedido1_menu.add(pedido1_bebida)
                    pedido1_menu.add(pedido1_entrante)
                    pedido1_menu.add(pedido1_postre)
                    
                    
                    
                    # Calcular precio total del menú
                    print("El precio de tu pizza es: ", pedido1_pizza.precio())
                    print("El precio de tu bebida es: ", pedido1_bebida.precio())
                    print("El precio de tu entrante es: ", pedido1_entrante.precio())
                    print("El precio de tu postre es: ", pedido1_postre.precio())
                    
                    print("El precio total del menu basico (con descuento)es: ", pedido1_menu.precio())
                    
                    
                    cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                    cliente.guardar_cliente()

                    

                # Guardar el pedido del cliente
                    cliente.guardar_combo_menu(pedido1_menu._children, "Menu basico")
                                        
                elif menu == "2":
                    pedido1_pizza = Leaf_pizza("barbacoa")
                    pedido1_bebida = Leaf_bebida("coca-cola")
                    pedido1_entrante = Leaf_entrante("patatas")
                    pedido1_postre = Leaf_postre("tarta de queso")
                    
                    pedido2_menu = Composite_menu("Menu EEUU")
                    pedido2_menu.add(pedido1_pizza)
                    pedido2_menu.add(pedido1_bebida)
                    pedido2_menu.add(pedido1_entrante)
                    pedido2_menu.add(pedido1_postre)
                    
                    # Calcular precio total del menú
                    print("El precio de tu pizza es: ", pedido1_pizza.precio())
                    print("El precio de tu bebida es: ", pedido1_bebida.precio())
                    print("El precio de tu entrante es: ", pedido1_entrante.precio())
                    print("El precio de tu postre es: ", pedido1_postre.precio())
                    
                    
                    print("El precio total del menu EEUU (con descuento)es: ", pedido2_menu.precio()) 
                    
                    cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                    cliente.guardar_cliente()
                    
                    # Guardar el pedido del cliente
                    cliente.guardar_combo_menu(pedido2_menu._children, "Menu EEUU")                
                
                elif menu == "3":
                    pedido1_pizza = Leaf_pizza("4 quesos")
                    pedido1_bebida = Leaf_bebida("vino")
                    pedido1_entrante = Leaf_entrante("calamares")
                    pedido1_postre = Leaf_postre("helado")
                    
                    pedido3_menu = Composite_menu("Menu italiano")
                    pedido3_menu.add(pedido1_pizza)
                    pedido3_menu.add(pedido1_bebida)
                    pedido3_menu.add(pedido1_entrante)
                    pedido3_menu.add(pedido1_postre)
                    
                    # Calcular precio total del menú
                    print("El precio de tu pizza es: ", pedido1_pizza.precio())
                    print("El precio de tu bebida es: ", pedido1_bebida.precio())
                    print("El precio de tu entrante es: ", pedido1_entrante.precio())
                    print("El precio de tu postre es: ", pedido1_postre.precio())
                    
                    
                    print("El precio total del menu italiano (con descuento)es: ", pedido3_menu.precio())
                    
                    cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                    cliente.guardar_cliente()
                    
                    # Guardar el pedido del cliente
                    cliente.guardar_combo_menu(pedido3_menu._children, "Menu italiano")                    
                                
                elif menu == "4":
                    pedido1_pizza = Leaf_pizza("carbonara")
                    pedido1_bebida = Leaf_bebida("agua")
                    pedido1_entrante = Leaf_entrante("ensalada")
                    pedido1_postre = Leaf_postre("tarta de chocolate")
                    
                    pedido4_menu = Composite_menu("Menu español")
                    pedido4_menu.add(pedido1_pizza)
                    pedido4_menu.add(pedido1_bebida)
                    pedido4_menu.add(pedido1_entrante)
                    pedido4_menu.add(pedido1_postre)
                    
                    # Calcular precio total del menú
                    print("El precio de tu pizza es: ", pedido1_pizza.precio())
                    print("El precio de tu bebida es: ", pedido1_bebida.precio())
                    print("El precio de tu entrante es: ", pedido1_entrante.precio())
                    print("El precio de tu postre es: ", pedido1_postre.precio())
                    
                    print(f"El precio total del menu español (con descuento)es: {pedido4_menu.precio()}")
                    
                    cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                    cliente.guardar_cliente()
                    
                    # Guardar el pedido del cliente
                    cliente.guardar_combo_menu(pedido4_menu._children, "Menu español")
                                                    
                elif menu == "5":
                    pedido1_pizza = Leaf_pizza("hawaiana")
                    pedido1_bebida = Leaf_bebida("coca-cola")
                    pedido1_entrante = Leaf_entrante("patatas")
                    pedido1_postre = Leaf_postre("helado")
                    
                    pedido5_menu = Composite_menu("Menu frances")
                    pedido5_menu.add(pedido1_pizza)
                    pedido5_menu.add(pedido1_bebida)
                    pedido5_menu.add(pedido1_entrante)
                    pedido5_menu.add(pedido1_postre)
                    
                    # Calcular precio total del menú
                    print("El precio de tu pizza es: ", pedido1_pizza.precio())
                    print("El precio de tu bebida es: ", pedido1_bebida.precio())
                    print("El precio de tu entrante es: ", pedido1_entrante.precio())
                    print("El precio de tu postre es: ", pedido1_postre.precio())
                
                    
                    print(f"El precio total del menu frances (con descuento)es: {pedido5_menu.precio()}") 
                    
                    cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                    cliente.guardar_cliente()
                    
                    # Guardar el pedido del cliente
                    cliente.guardar_combo_menu(pedido5_menu._children, "Menu frances")
                                        
            elif bienvenida =="3":
                print("Tenemos los siguientes productos: 1. Bebida, 2. Entrante, 3. Postre")
                producto = input("Elige el numero del producto que quieres: ")
                lista_producto = ["1", "2", "3"]
                while producto not in lista_producto:
                    producto = input("No tenemos esa, ¿que producto quieres? ")
                    
                if producto == "1":
                    bebida = obtener_bebida()
                    pedido1_bebida = Leaf_bebida(bebida)
                    print("El precio de tu ",pedido1_bebida.operation()," es: ", pedido1_bebida.precio())
                    
                    cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                    cliente.guardar_cliente()
                    
                    # Guardar el pedido del cliente
                    cliente.guardar_pedido([pedido1_bebida])
                    
                elif producto == "2":
                    entrante = obtener_entrante()
                    pedido1_entrante = Leaf_entrante(entrante)
                    print("El precio de tu ",pedido1_entrante.operation()," es: ", pedido1_entrante.precio())
                    
                    cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                    cliente.guardar_cliente()
                    
                    # Guardar el pedido del cliente
                    cliente.guardar_pedido([pedido1_entrante])
                    
                    
                elif producto == "3":
                    postre = obtener_postre()
                    pedido1_postre = Leaf_postre(postre)
                    print("El precio de tu ",pedido1_postre.operation()," es: ", pedido1_postre.precio())
                    
                    cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                    cliente.guardar_cliente()

                    # Guardar el pedido del cliente
                    cliente.guardar_pedido([pedido1_postre])
                    
            elif bienvenida =="4":
                print("Los combos tienen un 15% de descuento respecto del precio total")
                print("Tenemos los siguientes combos:")
                print("1. Combo Pareja: 2 pizzas: barbacoa y 4 quesos, 1vino y 1 champagne, calamares y croquetas  y tarta de chocolate y tarta de queso")
                print("2. Combo Familiar: 2 pizzas margarita y 2 barbacoa, 2 aguas y 2 refrescos, 2 alitas y 2 de patatas y 4 tartas de queso")
                print("3. Combo Maxi muerte por chocolat: 6 pizzas barbacoa, 6 agua, 6 alitas de pollo y 6 tarta de chocolate")
                combo = input("Elige el numero del combo que quieres: ")
                lista_combo = ["1", "2", "3"]
                while combo not in lista_combo:
                    combo = input("No tenemos esa, ¿que combo quieres? ")
                    
                if combo == "1":
                    combo1 = Composite_combo1("Combo Pareja")
                    pedido1_pizza = Leaf_pizza("barbacoa")
                    pedido1_pizza2 = Leaf_pizza("4 quesos")
                    pedido1_bebida = Leaf_bebida("vino")
                    pedido1_bebida2 = Leaf_bebida("champagne")
                    pedido1_entrante = Leaf_entrante("calamares")
                    pedido1_entrante2 = Leaf_entrante("croquetas")
                    pedido1_postre = Leaf_postre("tarta de chocolate")
                    pedido1_postre2 = Leaf_postre("tarta de queso")
                    
                    
                    combo1.add(pedido1_pizza)
                    combo1.add(pedido1_pizza2)

                    combo1.add(pedido1_bebida)
                    combo1.add(pedido1_bebida2)
                    combo1.add(pedido1_entrante)
                    combo1.add(pedido1_entrante2)
                    
                    combo1.add(pedido1_postre)
                    combo1.add(pedido1_postre2)
                    
                    print(f"El precio total del combo pareja es: {combo1.precio()}")
                    
                    cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                    cliente.guardar_cliente()
                    
                    # Guardar el pedido del cliente
                    cliente.guardar_combo_menu(combo1._children, "Combo Pareja")
                                        
                elif combo == "2":
                    combo1 = Composite_combo1("Combo Familiar")
                    pedido1_pizza = Leaf_pizza("margarita")
                    pedido1_pizza2 = Leaf_pizza("barbacoa")
                    pedido1_pizza3 = Leaf_pizza("margarita")
                    pedido1_pizza4   = Leaf_pizza("barbacoa")
                    pedido1_bebida = Leaf_bebida("agua")
                    pedido1_bebida2 = Leaf_bebida("agua")
                    pedido1_bebida3 = Leaf_bebida("coca-cola")
                    pedido1_bebida4 = Leaf_bebida("coca-cola")
                    
                    pedido1_entrante = Leaf_entrante("alitas de pollo")
                    pedido1_entrante2 = Leaf_entrante("alitas de pollo")
                    pedido1_entrante3 = Leaf_entrante("patatas")
                    pedido1_entrante4 = Leaf_entrante("patatas")
                    
                    
                    pedido1_postre = Leaf_postre("tarta de queso")
                    pedido1_postre2 = Leaf_postre("tarta de queso")
                    pedido1_postre3 = Leaf_postre("tarta de queso")
                    pedido1_postre4 = Leaf_postre("tarta de queso")
                    
                    
                    combo1.add(pedido1_pizza)
                    combo1.add(pedido1_pizza2)
                    combo1.add(pedido1_pizza3)
                    combo1.add(pedido1_pizza4)
                    combo1.add(pedido1_bebida)
                    combo1.add(pedido1_bebida2)
                    combo1.add(pedido1_bebida3)
                    combo1.add(pedido1_bebida4)
                    combo1.add(pedido1_entrante)
                    combo1.add(pedido1_entrante2)
                    combo1.add(pedido1_entrante3)
                    combo1.add(pedido1_entrante4)
                    
                    combo1.add(pedido1_postre)
                    combo1.add(pedido1_postre2)
                    combo1.add(pedido1_postre3)
                    combo1.add(pedido1_postre4)
                    
                    print(f"El precio total del combo familiar es: {combo1.precio()}")
                    
                    cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                    cliente.guardar_cliente()
                    
                    # Guardar el pedido del cliente
                    cliente.guardar_combo_menu(combo1._children, "Combo Familiar")
                                        
                elif combo == "3":
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
                    
                    cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
                    cliente.guardar_cliente()
                    
                    # Guardar el pedido del cliente
                    cliente.guardar_combo_menu(combo1._children, "Combo Maxi")                    
                
                
            else:
                print("Vale, adios")
                    

                    
