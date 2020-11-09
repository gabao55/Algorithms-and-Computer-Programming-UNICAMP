pessoas = {}
pessoas['assassino'] = []
pessoas['vitima'] = []
pessoas['detetive'] = []
linhas = int(input(''))
teste = linhas
todos = []

if linhas == 0:
    print('Valor inválido na entrada.')

while linhas != 0:
    assassino, vitima, detetive = input().split()
    pessoas['assassino'].append(assassino)
    pessoas['vitima'].append(vitima)
    pessoas['detetive'].append(detetive)
    linhas -= 1
for i in pessoas['assassino']:
    if i not in todos:
        todos.append(i)
for j in pessoas['vitima']:
    if j not in todos:
        todos.append(j)
for k in pessoas['detetive']:
    if k not in todos:
        todos.append(k)
todos.sort()


for i in todos:
    if i in pessoas['assassino'] and i in pessoas['vitima'] and i not in pessoas['detetive']:
        print(60 * '-')
        contador_vitima = 0
        contador_assassino = 0
        contador_detetive = 0
        posicao = 0
        vit = 0
        print(i + ' (in memoriam): assassino(a).')
        for j in range(len(pessoas['assassino'])):
            if i == pessoas['assassino'][j]:
                posicao = j
                vit = pessoas['vitima'][j]
                if vit in pessoas['assassino'] and vit not in pessoas['detetive']:
                    contador_assassino += 1
                elif vit in pessoas['detetive']:
                    contador_detetive += 1
                elif vit in pessoas['vitima'] and vit not in pessoas['detetive'] and vit not in pessoas['assassino']:
                    contador_vitima += 1
        if contador_assassino > 0 and contador_vitima > 0 and contador_detetive > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
            print('  Matou', contador_detetive, 'detetive(s).')
            print('  Matou', contador_vitima, 'inocente(s).')
        elif contador_assassino > 0 and contador_detetive > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
            print('  Matou', contador_detetive, 'detetive(s).')
        elif contador_assassino > 0 and contador_vitima > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
            print('  Matou', contador_vitima, 'inocente(s).')
        elif contador_detetive > 0 and contador_vitima > 0:
            print('  Matou', contador_detetive, 'detetive(s).')
            print('  Matou', contador_vitima, 'inocente(s).')
        elif contador_assassino > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
        elif contador_detetive > 0:
            print('  Matou', contador_detetive, 'detetive(s).')
        elif contador_vitima > 0:
            print('  Matou', contador_vitima, 'inocente(s).')
    elif i in pessoas['assassino'] and i not in pessoas['detetive'] and i not in pessoas['vitima']: #precisa identificar as vitimas
        print(60 * '-')
        contador_vitima = 0
        contador_assassino = 0
        contador_detetive = 0
        posicao = 0
        vit = 0
        print(i + ': assassino(a).')
        for j in range(len(pessoas['assassino'])):
            if i == pessoas['assassino'][j]:
                posicao = j
                vit = pessoas['vitima'][j]
                if vit in pessoas['assassino'] and vit not in pessoas['detetive']:
                    contador_assassino += 1
                elif vit in pessoas['detetive']:
                    contador_detetive += 1
                elif vit in pessoas['vitima'] and vit not in pessoas['detetive'] and vit not in pessoas['assassino']:
                    contador_vitima += 1
        if contador_assassino > 0 and contador_vitima > 0 and contador_detetive > 0:
            print('  Matou', contador_detetive, 'detetive(s).')
            print('  Matou', contador_assassino, 'assassino(s).')
            print('  Matou', contador_vitima, 'inocente(s).')
        elif contador_assassino > 0 and contador_detetive > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
            print('  Matou', contador_detetive, 'detetive(s).')
        elif contador_assassino > 0 and contador_vitima > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
            print('  Matou', contador_vitima, 'inocente(s).')
        elif contador_detetive > 0 and contador_vitima > 0:
            print('  Matou', contador_detetive, 'detetive(s).')
            print('  Matou', contador_vitima, 'inocente(s).')
        elif contador_assassino > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
        elif contador_detetive > 0:
            print('  Matou', contador_detetive, 'detetive(s).')
        elif contador_vitima > 0:
            print('  Matou', contador_vitima, 'inocente(s).')
    elif i in pessoas['detetive'] and i in pessoas['vitima'] and i not in pessoas['assassino']:
        print(60 * '-')
        contador_casos = 0
        print(i + ' (in memoriam): detetive.')
        for k in pessoas['detetive']:
            if i == k:
                contador_casos += 1
        print('  Resolveu', contador_casos, 'caso(s).')
        contador_vitima = 0
        contador_assassino = 0
        contador_detetive = 0
        posicao = 0
        vit = 0
        for j in range(len(pessoas['assassino'])):
            if i == pessoas['assassino'][j]:
                posicao = j
                vit = pessoas['vitima'][j]
                if vit in pessoas['assassino'] and vit not in pessoas['detetive']:
                    contador_assassino += 1
                elif vit in pessoas['detetive']:
                    contador_detetive += 1
                elif vit in pessoas['vitima'] and vit not in pessoas['detetive'] and vit not in pessoas['assassino']:
                    contador_vitima += 1
        if contador_assassino > 0 and contador_vitima > 0 and contador_detetive > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
            print('  Matou', contador_detetive, 'detetive(s).')
            print('  Matou', contador_vitima, 'inocente(s).')
        elif contador_assassino > 0 and contador_detetive > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
            print('  Matou', contador_detetive, 'detetive(s).')
        elif contador_assassino > 0 and contador_vitima > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
            print('  Matou', contador_vitima, 'inocente(s).')
        elif contador_detetive > 0 and contador_vitima > 0:
            print('  Matou', contador_detetive, 'detetive(s).')
            print('  Matou', contador_vitima, 'inocente(s).')
        elif contador_assassino > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
        elif contador_detetive > 0:
            print('  Matou', contador_detetive, 'detetive(s).')
        elif contador_vitima > 0:
            print('  Matou', contador_vitima, 'inocente(s).')
    elif i in pessoas['detetive'] and i in pessoas['assassino'] and i in pessoas['vitima']: #precisa identificar as vitimas
        print(60 * '-')
        contador_casos = 0
        print(i + ' (in memoriam): detetive.')
        for k in pessoas['detetive']:
            if i == k:
                contador_casos += 1
        print('  Resolveu', contador_casos, 'caso(s).')
        contador_vitima = 0
        contador_assassino = 0
        contador_detetive = 0
        posicao = 0
        vit = 0
        for j in range(len(pessoas['assassino'])):
            if i == pessoas['assassino'][j]:
                posicao = j
                vit = pessoas['vitima'][j]
                if vit in pessoas['assassino'] and vit not in pessoas['detetive']:
                    contador_assassino += 1
                elif vit in pessoas['detetive']:
                    contador_detetive += 1
                elif vit in pessoas['vitima'] and vit not in pessoas['detetive'] and vit not in pessoas['assassino']:
                    contador_vitima += 1
        if contador_assassino > 0 and contador_vitima > 0 and contador_detetive > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
            print('  Matou', contador_detetive, 'detetive(s).')
            print('  Matou', contador_vitima, 'inocente(s).')
        elif contador_assassino > 0 and contador_detetive > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
            print('  Matou', contador_detetive, 'detetive(s).')
        elif contador_assassino > 0 and contador_vitima > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
            print('  Matou', contador_vitima, 'inocente(s).')
        elif contador_detetive > 0 and contador_vitima > 0:
            print('  Matou', contador_detetive, 'detetive(s).')
            print('  Matou', contador_vitima, 'inocente(s).')
        elif contador_assassino > 0:
            print('  Matou', contador_assassino, 'assassino(s).')
        elif contador_detetive > 0:
            print('  Matou', contador_detetive, 'detetive(s).')
        elif contador_vitima > 0:
            print('  Matou', contador_vitima, 'inocente(s).')
    elif i in pessoas['detetive'] and i in pessoas['assassino'] and i not in pessoas['vitima']: #precisa identificar as vitimas
        print(60 * '-')
        contador_casos = 0
        print(i + ': detetive.')
        for k in pessoas['detetive']:
            if i == k:
                contador_casos += 1
        print('  Resolveu', contador_casos, 'caso(s).')
        contador_vitima = 0
        contador_assassino = 0
        contador_detetive = 0
        posicao = 0
        vit = 0
        for j in range(len(pessoas['assassino'])):
            if i == pessoas['assassino'][j]:
                posicao = j
                vit = pessoas['vitima'][j]
                if vit in pessoas['assassino'] and vit not in pessoas['detetive']:
                    contador_assassino += 1
                elif vit in pessoas['detetive']:
                    contador_detetive += 1
                elif vit not in pessoas['assassino'] and vit not in pessoas['detetive']:
                    contador_vitima += 1
            x = int(contador_assassino)
            y = int(contador_detetive)
            z = int(contador_vitima)
        if contador_assassino > 0 and contador_vitima > 0 and contador_detetive > 0:
            print('  Matou', y, 'detetive(s).')
            print('  Matou', x, 'assassino(s).')
            print('  Matou', z, 'inocente(s).')
        elif contador_assassino > 0 and contador_detetive > 0:
            print('  Matou', x, 'assassino(s).')
            print('  Matou', y, 'detetive(s).')
        elif contador_assassino > 0 and contador_vitima > 0:
            print('  Matou', x, 'assassino(s).')
            print('  Matou', z, 'inocente(s).')
        elif contador_detetive > 0 and contador_vitima > 0:
            print('  Matou', y, 'detetive(s).')
            print('  Matou', z, 'inocente(s).')
        elif contador_assassino > 0:
            print('  Matou', x, 'assassino(s).')
        elif contador_detetive > 0:
            print('  Matou', y, 'detetive(s).')
        elif contador_vitima > 0:
            print('  Matou', z, 'inocente(s).')
    elif i in pessoas['detetive'] and i not in pessoas['assassino'] and i not in pessoas['vitima']:
        print(60 * '-')
        contador = 0
        for j in pessoas['detetive']:
            if i == j:
                contador += 1
        print(i + ': detetive.' + '\n' + '  ' + 'Resolveu' , contador , 'caso(s).')
    elif i in pessoas['vitima'] and i not in pessoas['detetive'] and i not in pessoas['assassino']:
        print(60 * '-')
        for j in pessoas['vitima']:
            if i == j:
                print(i + ' (in memoriam): vítima inocente.')
if teste != 0:
    print(60 * '-')
