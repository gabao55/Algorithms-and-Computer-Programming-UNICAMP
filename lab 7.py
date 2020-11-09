nota_atividades = [float(x) for x in input().split()]
def tupla_float_int(x):
    x = x[1:-1]
    x = x.split(',')
    f = float(x[0])
    i = int(x[1])
    return(f,i)
nota_labs = [tupla_float_int(x) for x in input().split()]
nota_provas = [float(x) for x in input().split()]
frequência = int(input(''))
soma_atividades = 0
n_atividades = len(nota_atividades)
for i in nota_atividades:
    soma_atividades += i
media_atividades = ((soma_atividades/n_atividades))
#ate aqui ta tudo certo
soma_labs = 0
soma_pesos = 0
for j in nota_labs:
    soma_labs += j[0] * j[1]
    soma_pesos += j[1]
media_labs = (soma_labs/soma_pesos)
media_provas = ((2 * nota_provas[0] + 3 * nota_provas[1])/5)
media_ponderada = ((0.6 *media_provas + 0.3 * media_labs + 0.1 * media_atividades))
#quero descobrir como deixar a media ponderada com 1 casa decimal
lista = []
lista.append(media_provas)
lista.append(media_ponderada)
lista.append(media_labs)
media_preliminar = min(lista)
#ja sei todas as medias, falta colocar a media final, as condições de aprovação e reprovação e o print de todas as medias.
#as medias que tenho sao chamadas de media_atividades, media_labs, media_provas, media_ponderada e media_preliminar.
if frequência < 75:
    print('Média das atividades conceituais:', format(media_atividades, '.1f'))
    print('Média das tarefas de laboratório:', format(media_labs, '.1f'))
    print('Média das provas:', format(media_provas, '.1f'))
    print('Média ponderada dos elementos:', format(media_ponderada, '.1f'))
    print('Média preliminar:', format(media_preliminar, '.1f'))
    print('Reprovado(a) por frequência.')
    print('Média final:', format(media_preliminar, '.1f'))
elif frequência >= 75 and media_preliminar < 2.5:
    print('Média das atividades conceituais:', format(media_atividades, '.1f'))
    print('Média das tarefas de laboratório:', format(media_labs, '.1f'))
    print('Média das provas:', format(media_provas, '.1f'))
    print('Média ponderada dos elementos:', format(media_ponderada, '.1f'))
    print('Média preliminar:', format(media_preliminar, '.1f'))
    print('Reprovado(a) por nota.')
    print('Média final:', format(media_preliminar, '.1f'))
elif frequência >= 75 and 2.5 <= media_preliminar < 5.0:
    exame = float(input(''))
    print('Média das atividades conceituais:', format(media_atividades, '.1f'))
    print('Média das tarefas de laboratório:', format(media_labs, '.1f'))
    print('Média das provas:', format(media_provas, '.1f'))
    print('Média ponderada dos elementos:', format(media_ponderada, '.1f'))
    print('Média preliminar:', format(media_preliminar, '.1f'))
    print('Nota no exame:' , format(exame, '.1f'))
    douglas = (media_preliminar + exame)/2
    if douglas < 5.0:
        print('Reprovado(a) por nota.')
        print('Média final:', format(douglas, '.1f'))
    else:
        print('Aprovado(a) por nota e frequência.')
        print('Média final:', format(douglas, '.1f'))
elif frequência >= 75 and media_preliminar >= 5.0:
    print('Média das atividades conceituais:', format(media_atividades, '.1f'))
    print('Média das tarefas de laboratório:', format(media_labs, '.1f'))
    print('Média das provas:', format(media_provas, '.1f'))
    print('Média ponderada dos elementos:', format(media_ponderada, '.1f'))
    print('Média preliminar:', format(media_preliminar, '.1f'))
    print('Aprovado(a) por nota e frequência.')
    print('Média final:' , format(media_ponderada, '.1f'))