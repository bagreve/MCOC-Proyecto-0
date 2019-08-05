# -*- coding: utf-8 -*-
"""
Created on Sun Aug 04 16:22:09 2019

@author: 
"""

# una perdida de significancia ocurre con el cambio de numeros flotantes a binarios debido a que tienen un sesgo de
# aproximacion al tener que sumar 127 al sector de exponentes no siendo exacto.
# un caso donde se puede ver es en la funcion de aproximacion, si se aproxima a la decima estos numeros dan el mismo resultado

print round(3.45, 1)
# = 3,5
print round(3.55, 1)
# = 3,5


# El cambio ocurre ya que el programa toma el numero, lo pasa a binario, lo aproxima y lo pasa a numero nuevamente
# pero al pasar a binario acurre lo siguiente:

from decimal import Decimal
print Decimal(3.45)
#3.45000000000000017763568394002504646778106689453125
print Decimal(3.55)
#3.54999999999999982236431605997495353221893310546875

# Estos errores de aproximacion son solo un ejemplo de perdida de significancia, dentro de la pequeña variacion de decimales
# que se produce por el cambio a binario y biceversa.
# Al redondear, estas pequeñas variaciones son las que dicen si se aproxima hacia arriba o hacia abajo 

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input("Introduzca la parte entera del numero a convertir en binario: "))
if numero>=0:
    signo=0
if numero<0:
    signo=1
bit=binarizar(numero)
print"En binario:",(binarizar(numero))


x = float(raw_input("Introduzca la parte decimal del numero a convertir en binario: "))
p = 0
while ((2**p)*x) %1 != 0:
    p += 1
    # print p

    num = int (x * (2 ** p))
    # print num

    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num%2) + result
        num = num / 2

    for i in range (p - len(result)):
        result = '0' + result
    result = result[0:-p] + result[-p:]

print "En binario:", result 
print ""
n=int(binarizar(numero))
exponente=0
while n > 2:
    exponente += 1
    n= n/10
    
print "Exponente igual a:", exponente, "donde se debe sumar", 127
mantiza= int(bit) * 10**(22-exponente)

# es decir para pasar el numero ingresado a binario hay que pasar este nuevo exponente abinario e irá en el sector de exponente

print "Es decir, el sector binario de excedente será",binarizar(exponente+127)
print ""
print "Y el número completo en binario se escribirá como:"
print signo,binarizar(exponente+127),mantiza





