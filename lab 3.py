# -*- coding: utf-8 -*-
#   Caracterização de Triângulos    #


#Entrada:
a = float(input(''))
b = float(input(''))
c = float(input(''))

#Início do Algoritmo e Saída juntos:
if a == b and a == c:
    print('Triângulo equilátero.')
    if a**2 > b**2 + c**2 or b**2 > a**2 + c**2 or c**2 > a**2 + b**2:
        print('Triângulo obtusângulo.')
    elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print('Triângulo retângulo.')
    else:
        print('Triângulo acutângulo.')
elif (a == b and a != c) or (b == c and b != a) or (a == c and a != b):
    print('Triângulo isósceles.')
    if a**2 > b**2 + c**2 or b**2 > a**2 + c**2 or c**2 > a**2 + b**2:
        print('Triângulo obtusângulo.')
    elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print('Triângulo retângulo.')
    else:
        print('Triângulo acutângulo.')
elif a <= 0 or b <= 0 or c <= 0:
    print('Valores inválidos na entrada.')
elif a >= b + c or b >= a + c or c >= a + b:
    print('Valores inválidos na entrada.')
else:
    print('Triângulo escaleno.')
    if a**2 > b**2 + c**2 or b**2 > a**2 + c**2 or c**2 > a**2 + b**2:
        print('Triângulo obtusângulo.')
    elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print('Triângulo retângulo.')
    else:
        print('Triângulo acutângulo.')
