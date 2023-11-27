from proxi import *

def borrar_elemento(carpeta):
    # Inputs
    tipo_elemento = input("Ingrese el tipo del elemento (Carpeta/Documento/Enlace): ")
    nombre_elemento = input("Ingrese el nombre del elemento que desea borrar: ")

    # Verificar si la carpeta contiene elementos
    if not carpeta._children:
        print(f"No hay elementos para borrar en la carpeta '{carpeta.nombre}'.")
        return

    # Buscar el elemento por tipo y nombre
    elemento_encontrado = None
    for elemento in carpeta._children:
        if isinstance(elemento, Carpeta) and elemento.nombre == nombre_elemento and tipo_elemento == "Carpeta":
            elemento_encontrado = elemento
            break
        elif isinstance(elemento, Documentos_Leaf) and elemento.nombre == nombre_elemento and tipo_elemento == "Documento":
            elemento_encontrado = elemento
            break
        elif isinstance(elemento, Enlace_Leaf) and elemento.nombre == nombre_elemento and tipo_elemento == "Enlace":
            elemento_encontrado = elemento
            break

    # Si se encuentra el elemento, eliminarlo y actualizar el JSON
    if elemento_encontrado:
        carpeta.remove(elemento_encontrado)
        guardar_estructura_en_json(carpeta, "Ejercicio Proxi/basedatos.json")
        print(f"Elemento '{nombre_elemento}' ({tipo_elemento}) eliminado correctamente de la carpeta '{carpeta.nombre}'.")
    else:
        print(f"No se encontró el elemento '{nombre_elemento}' ({tipo_elemento}) en la carpeta '{carpeta.nombre}'.")
        