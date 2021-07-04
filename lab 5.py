#   Slug Race   #

#Input:
a = int(input(''))

#Algorithm:
lista = []
i = 0
j = 1
valor = 0
while i < a:
    b = input('')
    lista.append(b)
    i += 1
    
#Output:
if len(lista) > 100:
    print('Valor inválido na linha 1.')
else:
    for l in lista:
        j += 1
        x = int(l)
        if x > valor:
            valor = x
            if valor > 50:
                break
    if 0 < valor < 10:
        print('1')
    elif 20 <= valor <= 50:
        print('3')
    elif valor > 50:
        print("Valor inválido na linha " + str(j) + ".")
    else:
        print('2')
