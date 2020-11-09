# -*- coding: utf-8 -*-

#   ASCII art   #


#Entrada:
a = input('')
b = int(input(''))
c = input('')

#Início do Algoritmo:
d = b - (b//2)
g = b - (b//2) - 1
e = d
v = d - 1
f = d + b - 1
x = 0
y = 0
z = 2 * b - 1

#Saída:
if a == 'TR' and b >= 3:
    for i in range(1, b+1, 2):
        print(i * c)
elif a == 'TRI' and b >= 3:
    for i in range(b, 0, -2):
        print(i * c)
elif a == 'TI' and b >= 3:
    while d != 3:
        for j in range(1, b + 1, 2):
            d = d - 1
            print(d * ' ' + j * c)
        break
elif a == 'TII' and b >= 3:
    while x != d:
        for j in range(b, -1, -2):
            print(x * ' ' + j * c)
            x = x + 1
        break
elif a == 'A' and b >= 3:
    while x != d:
        for j in range(b, -1, -2):
            print(x * ' ' + j * c)
            x = x + 1
        break
    while x != 0:
        for i in range(3, b + 1, 2):
            g = g - 1
            print(g * ' ' + i * c)
        break
elif a == 'E' and b >= 3:
    while d != 0:
        for i in range(1, b - 1, 2):
            f = f - 1
            print(f * ' ', i * c)
        break
    print(3 * b * c)
    while x != d:
        for j in range(b - 2, -1, -2):
            print(x * ' ', j * c, (b + y) * ' ', j * c)
            x = x + 1
            y = y + 2
        for k in range(3, b - 1, 2):
            g = g - 1
            z = z - 2
            print(g * ' ' + k * c + z * ' ' + k * c)
        break
    print(3 * b * c)
    while x != d:
        x = x + d
        for l in range(b - 2, -1, -2):
            print(x * ' ', l * c)
            x = x + 1
        break
elif b < 3 or b % 2 == 0:
    print('Base inválida.')
elif a != 'TR' or a != 'TRI' or a != 'TI' or a != 'TII' or a != 'A' or a != 'E':
    print('Objeto inválido.')
