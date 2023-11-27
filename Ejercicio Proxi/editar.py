from proxi import *


def editar_elemento(carpeta):
    tipo_a_editar = input("Ingrese el tipo a editar (Documento, Enlace, Carpeta): ")
    nombre_a_editar = input("Ingrese el nombre a editar: ")

    if tipo_a_editar == "Documento":
        editar_documento(carpeta, nombre_a_editar)
    elif tipo_a_editar == "Enlace":
        editar_enlace(carpeta, nombre_a_editar)
    elif tipo_a_editar == "Carpeta":
        editar_carpeta(carpeta, nombre_a_editar)
    else:
        print("Tipo no válido.")
        
def editar_documento(carpeta, nombre_documento):
    for child in carpeta._children:
        if isinstance(child, Documentos_Leaf) and child.nombre == nombre_documento:
            print(f"Documento encontrado: {child.operation()}")
            nuevo_nombre = input("Ingrese el nuevo nombre del documento: ")
            nuevo_tipo = input("Ingrese el nuevo tipo de documento: ")
            nuevo_tamaño = int(input("Ingrese el nuevo tamaño del documento en KB: "))
            
            child.nombre = nuevo_nombre
            child.tipo_documento = nuevo_tipo
            child.tamaño = nuevo_tamaño
            
            guardar_estructura_en_json(carpeta, "Ejercicio Proxi/basedatos.json")
            
            print(f"Documento '{nombre_documento}' editado correctamente.")
            return

    print(f"Documento '{nombre_documento}' no encontrado.")
    
def editar_enlace(carpeta, nombre_enlace):
    for child in carpeta._children:
        if isinstance(child, Enlace_Leaf) and child.nombre == nombre_enlace:
            print(f"Enlace encontrado: {child.operation()}")
            nuevo_nombre = input("Ingrese el nuevo nombre del enlace: ")
            nuevo_link = input("Ingrese el nuevo enlace: ")
            
            child.nombre = nuevo_nombre
            child.link = nuevo_link
            
            guardar_estructura_en_json(carpeta, "Ejercicio Proxi/basedatos.json")
            
            print(f"Enlace '{nombre_enlace}' editado correctamente.")
            return

    print(f"Enlace '{nombre_enlace}' no encontrado.")
    
def editar_carpeta(carpeta, nombre_carpeta):
    for child in carpeta._children:
        if isinstance(child, Carpeta) and child.nombre == nombre_carpeta:
            print(f"Carpeta encontrada: {child.operation()}")
            nuevo_nombre = input("Ingrese el nuevo nombre de la carpeta: ")
            
            child.nombre = nuevo_nombre
            
            guardar_estructura_en_json(carpeta, "Ejercicio Proxi/basedatos.json")
            
            print(f"Carpeta '{nombre_carpeta}' editada correctamente.")
            return

    print(f"Carpeta '{nombre_carpeta}' no encontrada.")