def realizar_operacion(self):
        carpeta_principal = Carpeta("Principal")
        estructura_json = self.real_subject.to_dict()
        if not self.usuario_actual:
            print("Debe iniciar sesión primero.")
            return

        print("Operaciones disponibles:")
        print("1. Acceder a una Carpeta (simulación)")
        print("2. Editar documento (simulación)")
        print("3. Añadir documento (simulación)")
        print("4. Añadir enlace (simulación)")
        print("5. Añadir carpeta (simulación)")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            self.real_subject.operation()
            self.log_access(self.real_subject.nombre)
        elif opcion == "2":
            print("Realizando operación específica en el documento (simulación)...")
            self.log_access("Operación específica")
        elif opcion == "3":
            self.agregar_documento()
        elif opcion == "4":
            self.agregar_enlace()
        elif opcion == "5":
            self.agregar_carpeta()
        else:
            print("Opción no válida.")
            
        with open("Ejercicio Proxi/basedatos.json", "w") as json_file:
            json.dump(estructura_json, json_file, indent=2)

    def agregar_documento(self):
        nombre_documento = input("Ingrese el nombre del nuevo documento: ")
        tipo_documento = input("Ingrese el tipo del nuevo documento: ")
        tamaño_documento = input("Ingrese el tamaño del nuevo documento (KB): ")

        nuevo_documento = Documentos_Leaf(nombre_documento, tipo_documento, tamaño_documento)
        self.real_subject.add(nuevo_documento)

        print(f"Documento '{nombre_documento}' añadido correctamente.")

    def agregar_enlace(self):
        # Crear el nuevo enlace
        nuevo_enlace = {
            "tipo": "Enlace",
            "nombre": input("Ingrese el nombre del nuevo enlace: "),
            "link": input("Ingrese el enlace: ")
        }

        # Preguntar al usuario si desea agregar el nuevo enlace dentro de una carpeta
        opcion = input("¿Quieres 1.agregar el nuevo enlace dentro de una carpeta existente o 2.crear una nueva carpeta para el enlace? (1 o 2): ")
        if opcion == "1":
            # Elegir la carpeta dentro de la cual agregar el nuevo enlace
            carpeta_seleccionada = self.elegir_carpeta(self.real_subject.to_dict())
            if carpeta_seleccionada:
                if "children" not in carpeta_seleccionada:
                    carpeta_seleccionada["children"] = []  # Crear la lista de hijos si no existe
                carpeta_seleccionada["children"].append(nuevo_enlace)
                print(f"Nuevo enlace '{nuevo_enlace['nombre']}' agregado dentro de '{carpeta_seleccionada['nombre']}'.")
            else:
                print("No se pudo agregar el nuevo enlace.")
        elif opcion == "2":
            # Crear una nueva carpeta para el enlace
            nueva_carpeta = {
                "tipo": "Carpeta",
                "nombre": input("Ingrese el nombre de la nueva carpeta para el enlace: "),
                "children": [nuevo_enlace]
            }
            self.real_subject.add(nueva_carpeta)
            print(f"Nueva carpeta '{nueva_carpeta['nombre']}' creada en el sistema con el enlace '{nuevo_enlace['nombre']}'.")
        else:
            print("Opción no válida.")

    def agregar_carpeta(self):
        nombre_carpeta = input("Ingrese el nombre de la nueva carpeta: ")
        pregunta = input("¿Quieres 1.agregar una nueva carpeta dentro de otra carpeta o 2.crear una nueva carpeta en el sistema?(1 o 2)")
        if pregunta == "1":
            estructura_json = self.real_subject.to_dict()

            # Manejar diferentes formatos de estructuras
            if "tipo" in estructura_json and estructura_json["tipo"] == "Carpeta":
                carpetas_disponibles = [estructura_json["nombre"]]
            elif "children" in estructura_json:
                carpetas_disponibles = [child["nombre"] for child in estructura_json["children"] if child["tipo"] == "Carpeta"]
            else:
                carpetas_disponibles = [child["nombre"] for child in estructura_json if child["tipo"] == "Carpeta"]

            print("Carpetas disponibles:")
            for i, carpeta in enumerate(carpetas_disponibles, start=1):
                print(f"{i}. {carpeta}")

            if not carpetas_disponibles:
                print("No hay carpetas disponibles.")
                return None

            # Solicitar al usuario que elija una carpeta
            opcion = input("Seleccione una carpeta: ")
            try:
                opcion = int(opcion)
                if 1 <= opcion <= len(carpetas_disponibles):
                    nombre_carpeta_seleccionada = carpetas_disponibles[opcion - 1]

                    # Manejar diferentes formatos de estructuras
                    if "children" in estructura_json:
                        carpeta_seleccionada = next(child for child in estructura_json["children"] if child["nombre"] == nombre_carpeta_seleccionada)
                        carpeta_principal = Carpeta("Principal")
                    else:
                        carpeta_seleccionada = estructura_json

                else:
                    print("Opción no válida.")
                    return None
            except ValueError:
                print("Opción no válida.")
                return None
                
                
        elif pregunta == "2":
                nueva_carpeta = Carpeta(nombre_carpeta)
                self.real_subject.add(nueva_carpeta)

                print(f"Carpeta '{nombre_carpeta}' añadida correctamente.")
        
        
        
        
    def acceder_carpeta(self):
        # Aquí puedes implementar la lógica para que el usuario elija la carpeta a la que desea acceder.
        # Puedes mostrar la lista de carpetas disponibles y permitir que el usuario seleccione una.

        print("Acceder a una carpeta (simulación)...")
        carpeta_seleccionada = self.elegir_carpeta()
        
        if carpeta_seleccionada:
            carpeta_seleccionada.operation()
            self.log_access(f"Acceso a la carpeta {carpeta_seleccionada.nombre}")
            
    def elegir_carpeta(self):
        # Aquí deberías implementar la lógica para mostrar las carpetas disponibles y permitir al usuario elegir una.
        # Puedes devolver la carpeta seleccionada.
        # Por ahora, devolvemos una carpeta de ejemplo.
        return Carpeta("CarpetaEjemplo")
    
    
    
    


import json
usuario_actual = None
# Solicitar al usuario que elija entre registrarse e iniciar sesión
def cargar_estructura_desde_json(parent, json_data):
    for child_data in json_data.get("Contiene", []):
        if child_data["tipo"] == "Carpeta":
            child_folder = Carpeta(child_data["nombre"])
            parent.add(child_folder)
            cargar_estructura_desde_json(child_folder, child_data)
        elif child_data["type"] == "Documento":
            child_document = Documentos_Leaf(child_data["nombre"], child_data["tipo_documento"], child_data["tamano"])
            parent.add(child_document)
        elif child_data["type"] == "Enlace":
            child_link = Enlace_Leaf(child_data["nombre"], child_data["link"])
            parent.add(child_link)

carpeta_principal = Carpeta("Principal")

# Cargar contenido existente del archivo JSON si existe
try:
    with open("Ejercicio Proxi/basedatos.json", "r") as json_file:
        estructura_json = json.load(json_file)
        cargar_estructura_desde_json(carpeta_principal, estructura_json)
except FileNotFoundError:
    # Si el archivo no existe, simplemente continuamos con una carpeta vacía
    estructura_json = carpeta_principal.to_dict()
carpeta_principal = Carpeta("Principal")
documento1 = Documentos_Leaf("Documento1", "Texto", 10)
documento2 = Documentos_Leaf("Documento2", "Imagen", 20)
enlace1 = Enlace_Leaf("Enlace1", "http://enlace1.com")
proxy_documento1 = Proxy(documento1)
proxy_documento1.operation()
proxi_documento2 = Proxy(documento2)

proxi_documento2.operation()
carpeta_principal.add(proxy_documento1)
carpeta_principal.add(documento2)

carpeta_principal.add(proxi_documento2)
# Convertir la estructura a JSON
estructura_json = carpeta_principal.to_dict()
with open("Ejercicio Proxi/basedatos.json", "w") as json_file:
    json.dump(estructura_json, json_file, indent=2)


