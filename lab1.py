#Entradas:
tipodonumero1 = input('')

#Início do Algoritmo:
if tipodonumero1=='i':
    a = int(input(''))
elif tipodonumero1=='f':
    a = float(input(''))
tipodonumero2 = input('')
if tipodonumero2=='i':
    b = int(input(''))
elif tipodonumero2=='f':
    b = float(input(''))
    
#Saída:
print(format(a + b, '.2f')) if (tipodonumero1=='f' or tipodonumero2=='f') else print(a + b)
