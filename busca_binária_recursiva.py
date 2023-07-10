def busca_binária_recursiva(lista, num):

    if len(lista) == 0: # se a lista estiver vazia
        return False # o número procurado não está na lista

    metade = len(lista) // 2 # posição do elemento central da lista

    if num == lista[metade]: # se o número procurado for igual ao número na posição central da lista
        return True # o número procurado está na lista

    elif num > lista[metade]: # se o número procurado é maior que o número na posição central da lista
        return busca_binária_recursiva(lista[metade + 1:], num) # realiza uma nova busca a partir do segundo elemento da lista

    elif num < lista[metade]: # se o número procurado é menor que o número na posição central da lista
        return busca_binária_recursiva(lista[:metade], num) # realiza uma nova busca a partir do primeiro elemento da lista até o penúltimo


elementos = [4, 13, 20, 25, 44, 50, 52] # lista que será usada como parâmetro da função
número = int(input('Escolha um número: ')) # número que será buscado na lista

print(busca_binária_recursiva(elementos, número)) # apresentação do resultado da busca binária recursiva
