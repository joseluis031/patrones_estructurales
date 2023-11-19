tipo_pedido = row[1]
a = len(row[3])
print(f"Tipo: {tipo_pedido}, Precio: {row[2]}, Pedido: {row[3][1:a-1]}")