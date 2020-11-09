#   Minicalculadora:    #


#Entrada:
a = input('')
b = input('')
c = input('')

#Início do Algoritmo:
if a.isdigit():
    x = int(a)
    tipo_numero1 = 'int'
else:
    tipo_numero1 = 'float'
    x = float(a)

if c.isdigit():
    y = int(c)
    tipo_numero2 = 'int'
else:
    tipo_numero2 = 'float'
    y = float(c)
    
#Saída:
if b == '+':
    if tipo_numero1 == 'int' and tipo_numero2 == 'int':
        print(x+y)
    else:
        print(format(x + y, '.2f'))
elif b == '/':
    if y == 0:
        print('Erro.')
    else:
        print(format(x/y, '.2f'))
elif b == '**':
    if tipo_numero1 == 'int' and tipo_numero2 == 'int':
        print(x ** y)
    else:
        print(format(x ** y, '.2f'))
elif b == '-':
    if tipo_numero1 == 'int' and tipo_numero2 == 'int':
        print(x - y)
    else:
        print(format(x - y, '.2f'))
elif b == '//':
    if y == 0:
        print('Erro.')
    elif tipo_numero1 == 'int' and tipo_numero2 == 'int':
        print(x // y)
    else:
        print(format(x // y, '.2f'))
elif b == '*':
    if tipo_numero1 == 'int' and tipo_numero2 == 'int':
        print(x * y)
    else:
        print(format(x * y, '.2f'))
elif b == '%':
    if y == 0:
        print('Erro.')
    elif tipo_numero1 == 'int' and tipo_numero2 == 'int':
        print(x % y)
    else:
        print(format(x % y, '.2f'))
