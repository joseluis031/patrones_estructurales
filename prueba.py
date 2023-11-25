'''
def guardar_pizzapersonalizada( tipo, detalles_pizza):
        with open('pedidosnuevos.csv', mode='a', newline='') as file:
            writer = csv.writer(file)

            # Crea una nueva fila con nombre, usuario y contraseña
            row = [ tipo]

            # Agrega cada detalle de la pizza como una columna separada
            for detalle in detalles_pizza:
                
                    row.append(detalle)

            # Agrega detalles adicionales del pedido
            row.extend([""] * (7 - len(detalles_pizza)))  # Asegura que haya suficientes columnas para todos los detalles
            writer.writerow(row)
import pandas as pd
#ejemplo de uso
class Pedido():
    def __init__(self, builder):
        self.pedir_pizza = builder.producir_pizza #creo una variable para guardar la pizza
        
    def dict(self, detalles_pizza):
        diccionario_pedido = {
            "tipo de masa": detalles_pizza[0],
            "salsa base": detalles_pizza[1],
            "ingredientes principales": detalles_pizza[2],
            "tecnicas de coccion": detalles_pizza[3],
            "presentacion": detalles_pizza[4],
            "maridajes recomendados": detalles_pizza[5],
            "extras": detalles_pizza[6]
        }
        for key in diccionario_pedido:
            diccionario_pedido[key] = ' '.join(diccionario_pedido[key])
        return diccionario_pedido
    
    def guardar_pedido(self, detalles_pizza):
        diccionario_pedido = self.dict(detalles_pizza)
        df = pd.read_csv('pedidosnuevos.csv')
        df = pd.concat([df, pd.DataFrame(diccionario_pedido, index=[0])], ignore_index=True)
        df.to_csv('pedidosnuevos.csv', index=False)
'''
        
'''
ejemplo de uso
if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Pizza personalizada:")
    director.build_pizza()
    detalles_pizza = director.listar_pizza()
    pedido = Pedido(builder)
    pedido.guardar_pedido(detalles_pizza)
    print("\n")

'''


import csv


import os
def guardar_pedido_en_csv(cliente, choices):
    file_exists = os.path.isfile('pedidosnuevos.csv')

    with open('pedidosnuevos.csv', mode='a', newline='') as file:
        fieldnames = ['Cliente', 'Elecciones']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({'Cliente': cliente, 'Elecciones': choices})
    
    
'''
director = Director()
builder = ConcreteBuilder1()
director.builder = builder

print("Pizza personalizada:")
director.build_pizza()
detalles_pizza = director.listar_pizza()


pedido_actual = director.builder.producir_pizza.get_choices_str()
guardar_pedido_en_csv('Nombre del Cliente', pedido_actual)
'''