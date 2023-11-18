import csv
from composite_menu import *    


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
                
def buscar_pedido_anterior():
    # Preguntar al usuario si ha hecho algún pedido antes
    respuesta = input("¿Has hecho algún pedido antes? (si/no): ")

    if respuesta.lower() == "si":
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        # Buscar el ID del usuario en el archivo de clientes
        id_usuario = buscar_id_usuario(nombre_usuario, contraseña)

        if id_usuario is not None:
            # Buscar los elementos asociados al ID en el archivo de pedidos
            buscar_pedidos(id_usuario)
        else:
            print("Usuario no encontrado.")
    else:
        print("No has hecho ningún pedido anteriormente.")

def buscar_id_usuario(nombre_usuario, contraseña):
    archivo_csv_clientes = 'clientes.csv'

    with open(archivo_csv_clientes, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la primera fila (encabezados)

        for row in reader:
            if row[1] == nombre_usuario and row[2] == contraseña:
                
                return row[3]  # Devolver el ID del usuario

    return None

def buscar_pedidos(id_usuario):
    archivo_csv_pedidos = 'pedidos_cliente.csv'

    with open(archivo_csv_pedidos, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la primera fila (encabezados)
        
        print("Elementos del pedido anterior:")
        for row in reader:
            if row[0] == id_usuario:
                print(f"Elemento: {row[1]}, Precio: {row[2]}")

if __name__ == "__main__":
    # Ejemplo de cómo usar la clase Cliente
    nombre_cliente = input("Ingrese su nombre: ")
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    bienvenida = input("¿Qué deseas hacer (1,2,3,4,5): 1. Crear tu propio menú, 2. Elegir un menú ya creado, 3. Un producto suelto, 4. Un Combo, 5. Nada ")

    # ... (Código existente)

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
            
            # Calcular precio total del menú
            precio_total_menu = pedido1_pizza.precio() + pedido1_bebida.precio() + pedido1_entrante.precio() + pedido1_postre.precio()
            print("El precio de tu pizza es: ", pedido1_pizza.precio())
            print("El precio de tu bebida es: ", pedido1_bebida.precio())
            print("El precio de tu entrante es: ", pedido1_entrante.precio())
            print("El precio de tu postre es: ", pedido1_postre.precio())
            descuento = precio_total_menu*0.05
            precio_final = precio_total_menu - descuento
            print(f"El precio total del menú basico es: {precio_final}")
            
            cliente = Cliente(nombre_cliente, nombre_usuario, contraseña)
            cliente.guardar_cliente()

            # Crear un Composite_combo1 con los elementos del menú seleccionado
            pedido_cliente = Composite_combo1("Menú Básico")
            pedido_cliente.add(pedido1_pizza)
            pedido_cliente.add(pedido1_bebida)
            pedido_cliente.add(pedido1_entrante)
            pedido_cliente.add(pedido1_postre)

        # Guardar el pedido del cliente
            cliente.guardar_pedido(pedido_cliente._children)
            
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
            descuento = precio_total_menu*0.05
            precio_final = precio_total_menu - descuento
            
            print(f"El precio total del menú EEUU es: {precio_final}")
            
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
            descuento = precio_total_menu*0.05
            precio_final = precio_total_menu - descuento
            
            print(f"El precio total del menú italiano es: {precio_final}")
            
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
            descuento = precio_total_menu*0.05
            precio_final = precio_total_menu - descuento
            
            print(f"El precio total del menú  español es: {precio_final}")
            
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
            descuento = precio_total_menu*0.05
            precio_final = precio_total_menu - descuento
            
            print(f"El precio total del menú frances es: {precio_final}")
            
    elif bienvenida =="3":
        buscar_pedido_anterior()
