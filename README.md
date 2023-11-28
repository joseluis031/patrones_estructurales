# patrones_estructurales

El link de este repositorio es el siguiente: [GitHub](https://github.com/joseluis031/patrones_estructurales.git)

## Pizzeria
Mi pizzeria delizioso consta de una interfaz que pregunta al cliente si ha hecho algun pedido anteriormente o no, si la respuesta es si,
aportando el usuario su nombre de usuario y contraseña, se busca en la base de datos su pedido, se le enseña por pantalla y se le da la opción
de repetir el pedido o pedir otro nuevo(Cuando el usuario dice su nombre y contraseña, se busca en clientes.csv y se coge el id que tenga ese usuario y ese id se busca en
el csv de pedidos y cuando se encuentra, se muestra el pedido), en caso de no haber realizado anteriormente ningun pedido, el cliente debe registrarse y realizar el pedido.
Tambien hay un csv donde se encuentran todos los precios de todos los elementos y cuando el cliente va haciendo su pedido, el programa va viendo cual es el precio de cada producto
### Opciones del cliente:
[1.](#id1) EL cliente puede crear su propio menu, que consta de entrante, pizza, bebida y postre (mediante patron composite)


[2.](#id2) El cliente puede elegir un menu ya predefinido por la pizzeria y que tiene un descuento respecto a la creación de un menú personalizado (mediante patron composite)


[3.](#id3) El cliente puede elegir un producto suelto, ya sea una bebida, una pizza, un postre o un entrante (mediante patron composite)


[4.](#id4) El cliente puede elegir un combo ya predefinido(comida para 2 personas o un grupo de personas mayor), en este caso el descuento es mayor todavia (mediante patron composite)


[5.](#id5) El cliente puede elegir una Pizza by you Delizioso y asi poder personalizada todos los ingredientes de la pizza desde el inicio (mediante patron composite--->builder)



#### Menu Personalizado <a name="id1"></a>
Si el cliente elige un Menu Personalizado
La interfaz por terminal seria esta:
```
¿Has hecho algún pedido anteriormente? (si/no): no
Introduce tu nombre: miguel
Introduce tu nombre de usuario: miguel1
Introduce tu contraseña: miguel2
¿Qué deseas hacer (1,2,3,4,5): 1. Crear tu propio menú, 2. Elegir un menú ya creado, 3. Un producto suelto, 4. Un Combo, 5. Pizza by you Delizioso o 6. Salir 1
Vamos a ello!!
¿Qué pizza quieres? Tenemos: personalizada, margarita, barbacoa, 4 quesos, carbonara, hawaiana, romana, 4 estaciones, vegetal, napolitana, a: carbonara
¿Qué bebida quieres? Tenemos: coca-cola, fanta, agua, aa: fanta
¿Qué entrante quieres? Tenemos: patatas, calamares, ensalada, aa: patatas
¿Qué postre quieres? Tenemos: tarta de queso, tarta de chocolate, helado, a: helado
Detalles del menú personalizado:
carbonara - Precio: 13.0
fanta - Precio: 2.0
patatas - Precio: 3.0
helado - Precio: 2.0
El precio total del menú personalizado es: 20.0
```
y si ya ha pedido un menu personalizado recientemente se vera asi:
```
¿Has hecho algún pedido anteriormente? (si/no): si
Ingrese su nombre de usuario: miguel1
Ingrese su contraseña: miguel2
¿fue personalizado? (si/no):
Sí/No: si
¿fue una pizza by you Delizioso? (si/no):
Sí/No: no
Detalles del pedido anterior:
Elemento: carbonara, Precio: 13.0
Elemento: fanta, Precio: 2.0
Elemento: patatas, Precio: 3.0
Elemento: helado, Precio: 2.0
¿Quieres repetirlo? (si/no):
Sí/No: si
Repetimos el pedido anterior.
```
El pedido se guarda en un csv llamado pedido_menupers.csv
y el usuario se guarda en clientes.csv


#### Menu ya predefinido por la pizzeria <a name="id2"></a>
Si el cliente elige un Menu predefinido por la pizzeria,
La interfaz por terminal seria esta:

```
¿Has hecho algún pedido anteriormente? (si/no): no
Introduce tu nombre: carlos
Introduce tu nombre de usuario: carlos11
Introduce tu contraseña: carlos2
¿Qué deseas hacer (1,2,3,4,5): 1. Crear tu propio menú, 2. Elegir un menú ya creado, 3. Un producto suelto, 4. Un Combo, 5. Pizza by you Delizioso o 6. Salir 2
Tenemos los siguientes menus(cada menu ya creado tiene 5% descontado del precio total final):
1. Menu basico: alitas, Pizza margarita, agua y helado
2. Menu EEUU: patatas, Pizza barbacoa, coca-cola y tarta de queso
3. Menu italiano: calamares, Pizza 4 quesos, vino y helado
4. Menu español: ensalada, Pizza carbonara, agua y tarta de chocolate
5. Menu frances: patatas, Pizza hawaiana, coca-cola y helado
Elige el numero del menu que quieres: 4
El precio de tu pizza es:  13.0
El precio de tu bebida es:  1.0
El precio de tu entrante es:  7.0
El precio de tu postre es:  5.0
El precio total del menu español (con descuento)es: 24.7

```
y si ya ha pedido un menu predeterminado recientemente se vera asi:
```
¿Has hecho algún pedido anteriormente? (si/no): si
Ingrese su nombre de usuario: carlos11
Ingrese su contraseña: carlos2
¿fue personalizado? (si/no):
Sí/No: no
Detalles del pedido anterior:
Pedido: Menu español, Precio: 24.7, Contiene: 1 x carbonara, 1 x agua, 1 x ensalada, 1 x tarta de chocolate
¿Quieres repetirlo? (si/no):
Sí/No: si
Repetimos el pedido anterior.

```
El pedido se guarda en un csv llamado combos_menupredet y el usuario se guarda en clientes.csv



#### Producto Suelto <a name="id3"></a>
Si el cliente elige un producto suelto,
La interfaz por terminal seria esta:
```
¿Has hecho algún pedido anteriormente? (si/no): no
Introduce tu nombre: lucia
Introduce tu nombre de usuario: lucia1
Introduce tu contraseña: lucia2
¿Qué deseas hacer (1,2,3,4,5): 1. Crear tu propio menú, 2. Elegir un menú ya creado, 3. Un producto suelto, 4. Un Combo, 5. Pizza by you Delizioso o 6. Salir 3
Tenemos los siguientes productos: 1. Bebida, 2. Entrante, 3. Postre
Elige el numero del producto que quieres: 3
¿Qué postre quieres? Tenemos: tarta de queso, tarta de chocolate, helado, a: tarta de queso
El precio de tu  tarta de queso  es:  4.0

```
y si ya ha pedido un producto suelto recientemente se vera asi:

```
¿Has hecho algún pedido anteriormente? (si/no): si
Ingrese su nombre de usuario: lucia1
Ingrese su contraseña: lucia2
¿fue personalizado? (si/no):
Sí/No: si
¿fue una pizza by you Delizioso? (si/no):
Sí/No: no
Detalles del pedido anterior:
Elemento: tarta de queso, Precio: 4.0
¿Quieres repetirlo? (si/no):
Sí/No: si
Repetimos el pedido anterior.
```
El pedido se guarda en un csv llamado pedido_menupers.csv
y el cliente en clientes.csv

#### Combo Predefinido <a name="id4"></a>
Si el cliente elige un combo predefinido por la pizzeria,
La interfaz por terminal seria esta:
```
¿Has hecho algún pedido anteriormente? (si/no): no 
Introduce tu nombre: mario
Introduce tu nombre de usuario: mario1
Introduce tu contraseña: mario2
¿Qué deseas hacer (1,2,3,4,5): 1. Crear tu propio menú, 2. Elegir un menú ya creado, 3. Un producto suelto, 4. Un Combo, 5. Pizza by you Delizioso o 6. Salir 4
Los combos tienen un 15% de descuento respecto del precio total
Tenemos los siguientes combos:
1. Combo Pareja: 2 pizzas: barbacoa y 4 quesos, 1vino y 1 champagne, calamares y croquetas  y tarta de chocolate y tarta de queso      
2. Combo Familiar: 2 pizzas margarita y 2 barbacoa, 2 aguas y 2 refrescos, 2 alitas y 2 de patatas y 4 tartas de queso
3. Combo Maxi muerte por chocolat: 6 pizzas barbacoa, 6 agua, 6 alitas de pollo y 6 tarta de chocolate
Elige el numero del combo que quieres: 3
El precio total del combo maxi es: 132.6
```
y si ya ha pedido un combo predefinido recientemente se vera asi, ya que mediante una funcion, 
si se repite una bebida o postre... se muestra 1 vez el producto multiplicado por la veces que lo contiene el combo

```
¿Has hecho algún pedido anteriormente? (si/no): si
Ingrese su nombre de usuario: mario1
Ingrese su contraseña: mario2
¿fue personalizado? (si/no):
Sí/No: no
Detalles del pedido anterior:
Pedido: Combo Maxi, Precio: 132.6, Contiene: 6 x barbacoa, 6 x agua, 6 x alitas de pollo, 6 x tarta de chocolate
¿Quieres repetirlo? (si/no):
Sí/No: si
Repetimos el pedido anterior.
```
El pedido se guarda en un csv llamado combos_menupredet y el usuario se guarda en clientes.csv


#### Pizza by you Delizioso <a name="id5"></a>
Si el cliente elige personalizar una pizza desde 0,
La interfaz por terminal seria esta:
```
¿Has hecho algún pedido anteriormente? (si/no): no
Introduce tu nombre: juan
Introduce tu nombre de usuario: juan1
Introduce tu contraseña: juan2
¿Qué deseas hacer (1,2,3,4,5): 1. Crear tu propio menú, 2. Elegir un menú ya creado, 3. Un producto suelto, 4. Un Combo, 5. Pizza by you Delizioso o 6. Salir 5
Vamos a crear tu pizza
Introduzca el tipo de masa(normal, fina, extrafina o doble): fina
Introduzca la salsa base(tomate, carbonara, barbacoa, pesto o vegana): tomate
1. jamon
2. queso
3. bacon
4. champinones
5. pimiento
6. cebolla
7. atun
8. aceitunas
9. pollo
10. carne
11. gambas
12. anchoas
13. salami
14. chorizo
15. tomate
16. maiz
17. piña
18. rucula
Introduce el número del ingrediente o '0' si no quieres mas ingredientes: 3
Has elegido: bacon
1. jamon
2. queso
3. bacon
4. champinones
5. pimiento
6. cebolla
7. atun
8. aceitunas
9. pollo
10. carne
11. gambas
12. anchoas
13. salami
14. chorizo
15. tomate
16. maiz
17. piña
18. rucula
Introduce el número del ingrediente o '0' si no quieres mas ingredientes: 4
Has elegido: champinones
1. jamon
2. queso
3. bacon
4. champinones
5. pimiento
6. cebolla
7. atun
8. aceitunas
9. pollo
10. carne
11. gambas
12. anchoas
13. salami
14. chorizo
15. tomate
16. maiz
17. piña
18. rucula
Introduce el número del ingrediente o '0' si no quieres mas ingredientes: 5
Has elegido: pimiento
1. jamon
2. queso
3. bacon
4. champinones
5. pimiento
6. cebolla
7. atun
8. aceitunas
9. pollo
10. carne
11. gambas
12. anchoas
13. salami
14. chorizo
15. tomate
16. maiz
17. piña
18. rucula
Introduce el número del ingrediente o '0' si no quieres mas ingredientes: 0
Introduzca las tecnicas de coccion(horno, parrilla, sarten o microondas,): horno
Introduzca la presentacion(cuadrada, redonda, premium, calzone o sorpresa): redonda
Introduzca los maridajes recomendados(cerveza, vino, refresco o agua): agua
Elige extras de la lista:
1. queso doble
2. doble de ingredientes
3. doble de salsa
4. trufa
5. caviar
6. bordes de queso
7. salsa  ranchera
8. salsa de ajo
9. salsa de soja
10. salsa de yogur
11. salsa de curry
Introduce el número del extra o '0' para terminar: 3
Has elegido: doble de salsa
Elige extras de la lista:
1. queso doble
2. doble de ingredientes
3. doble de salsa
4. trufa
5. caviar
6. bordes de queso
7. salsa  ranchera
8. salsa de ajo
9. salsa de soja
10. salsa de yogur
11. salsa de curry
Introduce el número del extra o '0' para terminar: 4
Has elegido: trufa
Elige extras de la lista:
1. queso doble
2. doble de ingredientes
3. doble de salsa
4. trufa
5. caviar
6. bordes de queso
7. salsa  ranchera
8. salsa de ajo
9. salsa de soja
10. salsa de yogur
11. salsa de curry
Introduce el número del extra o '0' para terminar: 5
Has elegido: caviar
Elige extras de la lista:
1. queso doble
2. doble de ingredientes
3. doble de salsa
4. trufa
5. caviar
6. bordes de queso
7. salsa  ranchera
8. salsa de ajo
9. salsa de soja
10. salsa de yogur
11. salsa de curry
Introduce el número del extra o '0' para terminar: 0
['masa elegida: fina', 'salsa base elegida: tomate', 'ingredientes principales elegidos: bacon, champinones, pimiento', 'tecnicas de coccion elegidas: horno', 'presentacion elegida: redonda', 'maridajes elegidos: agua', 'extras elegidos: doble de salsa, trufa, caviar'] 
El cliente ha elegido su pizza.
El precio de tu  personalizada  es:  22.0
```
y si ya ha personalizado una pizza anteriormente:
```
¿Has hecho algún pedido anteriormente? (si/no): si
Ingrese su nombre de usuario: juan1
Ingrese su contraseña: juan2
¿fue personalizado? (si/no):
Sí/No: si
¿fue una pizza by you Delizioso? (si/no):
Sí/No: si
Tu anterior pedido de pizza:
Masa: fina
Salsa: tomate
Ingredientes: bacon, champinones, pimiento
Método de cocción: horno
Presentación: redonda
Maridaje: agua
Ingredientes extra: doble de salsa, trufa, caviar

¿Quieres repetirlo? (si/no):
Sí/No: si
Repetimos el pedido anterior.
```
El pedido se guarda en un csv llamado pedido_pizzapers.csv
y el cliente en clientes.csv



## Ejercicio Proxy
