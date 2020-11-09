#   Algoritmos de Ordenação #


#Importação:
import copy

#Funções:
def desenho(lista):
    maximo = 0
    meio_desenho = ''
    lista_desenho = lista.copy()
    for i in lista_desenho:
        j = int(i)
        if j > maximo:
            maximo = j
    while maximo != 0:
        contador = -1
        linha = []
        linha.append('.')
        for i in lista_desenho:
            j = int(i)
            contador += 1
            if j != maximo:
                linha.append(' ')
            else:
                linha.append('|')
                lista_desenho[contador] = j -1
        linha.append('.')
        a = ''.join(linha)
        maximo -= 1
        meio_desenho += a
        meio_desenho += '\n'
    return((len(lista) + 2) * '.'+ '\n' + meio_desenho + (len(lista) + 2) * '.')

#Entrada:
metodo = input()
lista = input().split()

#Saída:
if metodo == 'selection':
    print(desenho(lista))
    for fillslot in range(len(lista) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if lista[location] > lista[positionOfMax]:
                positionOfMax = location
        antes = copy.deepcopy(lista)
        if int(lista[fillslot]) != int(lista[positionOfMax]):
            temp = lista[fillslot]
            lista[fillslot] = lista[positionOfMax]
            lista[positionOfMax] = temp
            if antes != lista:
                print(desenho(lista))
        else:
            continue

if metodo == 'bubble':
    print(desenho(lista))
    exchanges = True
    passnum = len(lista) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if int(lista[i]) > int(lista[i + 1]):
                exchanges = True
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
        passnum = passnum - 1
        if exchanges:
            print(desenho(lista))

if metodo == 'insertion':
    for index in range(1, len(lista)):

        currentvalue = int(lista[index])
        position = int(index)
        antes = copy.deepcopy(lista)
        while int(position) > 0 and int(lista[position - 1]) > currentvalue:

            lista[position] = lista[position - 1]
            position = position - 1

        lista[position] = currentvalue
        print(desenho(lista))
