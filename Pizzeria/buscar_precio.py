import csv

def buscar_preciopizza(pizza):
        with open('Pizzeria/Datos/precio_elementos.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if pizza in row:
                    return f"El precio de {pizza} es {row[1]}"
                
      

def buscar_precioentrante(entrante):
    with open('Pizzeria/Datos/precio_elementos.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            if entrante in row[9]:
                return f"El precio de {entrante} es {row[10]}" 
    

def buscar_preciobebida(bebida):
    with open('Pizzeria/Datos/precio_elementos.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            if bebida in row[3]:
                return f"El precio de {bebida} es {row[4]}"
            


def buscar_preciopostre(postre):
    with open('Pizzeria/Datos/precio_elementos.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            if postre in row[6]:
                return f"El precio de {postre} es {row[7]}"
            


