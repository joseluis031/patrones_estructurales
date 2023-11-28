from proxi import *
from añadir_carpeta import *
from borrar import *
from editar import *

def realizar_operacion(usuario_actual, carpeta_principal):
    # ... (código anterior)

    opcion1 = input("Seleccione una opción: \n 1. Añadir Documento, enlace o carpeta \n 2. Borrar Documento, enlace o carpeta \n 3. Editar Documento, enlace o carpeta \n 4. Acceder a una Carpeta/documento/enlace \n 5. Salir \n").lower()

    if opcion1 == "1":
        pregunta = input("¿Que desea: \n 1.añadir un documento, enlace o carpeta en la carpeta principal \n 2.añadir un documento, enlace o carpeta dentro de una carpeta ?").lower()
        if pregunta == "1":
            pregunta2 = input("¿Que desea: \n 1.añadir un documento \n 2.añadir un enlace \n 3.añadir una carpeta ? \n").lower()
            if pregunta2 == "1":
                nombre_documento = input("Ingrese el nombre del nuevo documento: ")
                tipo_documento = input("Ingrese el tipo del nuevo documento: ")
                tamaño_documento = input("Ingrese el tamaño del nuevo documento (KB): ")

                nuevo_documento = Documentos_Leaf(nombre_documento, tipo_documento, tamaño_documento)
                carpeta_principal.add(nuevo_documento)
                
                
                
                guardar_estructura_en_json(carpeta_principal, "Ejercicio Proxi/basedatos.json")

                print(f"Documento '{nombre_documento}' añadido correctamente.")
                exit()
            elif pregunta2 == "2":
                nombre_enlace = input("Ingrese el nombre del nuevo enlace: ")
                link_enlace = input("Ingrese el enlace: ")
                nuevo_enlace = Enlace_Leaf(nombre_enlace, link_enlace)
                carpeta_principal.add(nuevo_enlace)
                guardar_estructura_en_json(carpeta_principal, "Ejercicio Proxi/basedatos.json")
                print(f"Enlace '{nombre_enlace}' añadido correctamente.")
                exit()
                
            elif pregunta2 == "3":
                nombre_carpeta = input("Ingrese el nombre de la nueva carpeta: ")
                nueva_carpeta = Carpeta(nombre_carpeta)
                carpeta_principal.add(nueva_carpeta)
                guardar_estructura_en_json(carpeta_principal, "Ejercicio Proxi/basedatos.json")
                print(f"Carpeta '{nombre_carpeta}' añadida correctamente.")
                exit()
        elif pregunta == "2":
            agregar_elemento_a_carpeta(carpeta_principal)
            exit()
            
        
    elif opcion1 == "2":
        borrar_elemento(carpeta_principal)        
        exit()
                
    elif opcion1 == "3":
        editar_elemento(carpeta_principal)
        exit()
        
    elif opcion1 == "4":
        pregunta = input("¿Que desea: \n 1.acceder a una carpeta \n 2.acceder a un documento o enlace ?").lower()
        if pregunta == "1":
            nombre_carpeta = input("Ingrese el nombre de la carpeta a la que desea acceder: ")
            for child in carpeta_principal._children:
                if child.nombre == nombre_carpeta:
                    print(f"Accediendo a la carpeta '{nombre_carpeta}'...")
                    print(child.operation())
                    exit()
            print(f"La carpeta '{nombre_carpeta}' no existe.")
            exit()
        elif pregunta == "2":
            nombre_documento = input("Ingrese el nombre del documento o enlace al que desea acceder: ")
            for child in carpeta_principal._children:
                if child.nombre == nombre_documento:
                    print(f"Accediendo al documento o enlace '{nombre_documento}'...")
                    print(child.operation())
                    exit()
            print(f"El documento o enlace '{nombre_documento}' no existe.")
            exit()
    elif opcion1 == "5":
        print("Gracias por usar el programa")
        exit()
    