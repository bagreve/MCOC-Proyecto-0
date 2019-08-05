# MCOC-Proyecto-0
Perdida de significancia:
En este ejemplo se usa la función round() de python que redondea los numeros. En Python los números decimales se almacenan internamente en binario con 53 bits de precisión, según la norma IEEE-754. Esto provoca una serie de variaciones en los decimales produciendo errores como en el redondeo. El problema es debido a que es necesario pasar los numeros a binario para poder trabajar con ellos y en este cambio para los numeros flotantes, que se escriben fragmentados en tres(signo,exponente y mantiza), se deben aproximar sus exponentes sumando por 127 para luego escribirlos como binarios trabajando con ellos y luego volverlos a número, esto provoca una pequeña variación en decimales del orden del dieciseisavo número después de la coma, pero suficiente para cambiar la solución de una redondeada en el punto critico como por ejemplo en el 0.5 que si el programa lo toma como 0.499999999999999998 se aproxima a 0, como un error, ya que deberia redondearse a 1.    



# OUTPUT DE LA CONSOLA:

3.5

3.5

3.45000000000000017763568394002504646778106689453125
3.54999999999999982236431605997495353221893310546875
Introduzca la parte entera del numero a convertir en binario: 98
En binario: 1100010
Introduzca la parte decimal del numero a convertir en binario: 0.98
En binario: 111110101110000101000111101011100001010001111010111

Exponente igual a: 6 donde se debe sumar 127
Es decir, el sector binario de excedente será 10000101

Y el número completo en binario se escribirá como:
0 10000101 11000100000000000000000
