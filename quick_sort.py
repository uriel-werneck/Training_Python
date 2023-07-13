def quick_sort(lista):
    if len(lista) <= 1: # se o comprimento da lista for menor ou igual a 1
        return lista # retorne a lista

    i = -1 # primeiro contador
    j = 0 # segundo contador

    pivo = lista[-1] # o pivô representa o último elemento da lista

    while j <= len(lista) - 2: # o "j" vai de 0 até a penúltima posição da lista
        if lista[j] < pivo: # se o elemento na posição "j" for menor que o pivô
            i += 1 # aumenta "i" em +1
            lista[i], lista[j] = lista[j], lista[i] # troca o elemento na posição "i" com o elemento na posição "j"
            j += 1 # aumenta o "j" em +1

        elif lista[j] >= pivo: # se o elemento na posição "j" for maior ou igual ao pivô
            j += 1 # aumenta o "j" em +1

    i += 1 # aumenta o "i" em +1 para saber a posição onde ficará o pivô
    lista[-1], lista[i] = lista[i], lista[-1] # troca o pivô com o elemento na posição "i"

    esquerda = lista[:i] # cria uma lista contendo todos os elementos à esquerda do pivô
    direita = lista[i + 1:] # cria uma lista contendo todos os elementos à direita do pivô

    return quick_sort(esquerda) + [lista[i]] + quick_sort(direita) # usa recursividade para organizar o lado esquerdo e direito da lista


lista = [8, 2, 4, 7, 1, 3, 9, 6, 5] # lista usada como exemplo
print('Lista desorganizada:', lista) # apresenta a lista desorganizada

resultado = quick_sort(lista) # organiza a lista usando a função quick_sort()
print('Lista organizada:', resultado) # apresenta a lista organizada
