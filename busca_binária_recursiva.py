def busca_binária_recursiva(lista, número):
    if len(lista) == 0: # se a lista estiver vazia
        return False # o número procurado não está na lista

    metade = len(lista) // 2 # posição do elemento central da lista

    if número == lista[metade]: # se o número procurado for igual ao número na posição central da lista
        return True # o número procurado está na lista

    elif número > lista[metade]: # se o número procurado é maior que o número na posição central da lista
        return busca_binária_recursiva(lista[metade + 1:], número) # realiza uma nova busca na metade direita da lista

    elif número < lista[metade]: # se o número procurado é menor que o número na posição central da lista
        return busca_binária_recursiva(lista[:metade], número) # realiza uma nova busca na metade esquerda da lista


lista = [4, 13, 20, 25, 44, 50, 52] # lista, em ordem crescente, que será usada como parâmetro da função
número = int(input('Escolha um número: ')) # número que será buscado na lista

print(busca_binária_recursiva(lista, número)) # apresenta o resultado da busca binária recursiva
