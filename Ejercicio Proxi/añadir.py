from proxi import *

def agregar_elemento_a_carpeta(carpeta_principal):
    # Mostrar las carpetas disponibles
    print("Carpetas disponibles:")
    for i, child in enumerate(carpeta_principal._children):
        if isinstance(child, Carpeta):
            print(f"{i + 1}. {child.nombre}")

    # Elegir la carpeta
    try:
        indice_carpeta = int(input("Seleccione una carpeta (por número): ")) - 1
        carpeta_seleccionada = carpeta_principal._children[indice_carpeta]

        # Pedir detalles del nuevo elemento
        tipo_elemento = input("Ingrese el tipo de elemento (Documento, Enlace, Carpeta): ")
        nombre_elemento = input("Ingrese el nombre del nuevo elemento: ")

        if tipo_elemento == "Documento":
            tipo_documento = input("Ingrese el tipo de documento: ")
            tamaño_documento = int(input("Ingrese el tamaño del documento en KB: "))
            nuevo_elemento = Documentos_Leaf(nombre_elemento, tipo_documento, tamaño_documento)
        elif tipo_elemento == "Enlace":
            enlace = input("Ingrese el enlace: ")
            nuevo_elemento = Enlace_Leaf(nombre_elemento, enlace)
        elif tipo_elemento == "Carpeta":
            nuevo_elemento = Carpeta(nombre_elemento)
        else:
            print("Tipo de elemento no válido.")
            return

        carpeta_seleccionada.add(nuevo_elemento)
        guardar_estructura_en_json(carpeta_principal, "Ejercicio Proxi/basedatos.json")
        print(f"Elemento '{nombre_elemento}' añadido correctamente a la carpeta '{carpeta_seleccionada.nombre}'.")
    except (ValueError, IndexError):
        print("Selección no válida.")