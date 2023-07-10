lista = [2, 5, 18, 22, 25, 32, 44, 50] # lista ordenada em ordem crescente

início = 0 # posição inicial da lista
final = len(lista) - 1 # posição final da lista
metade = (início + final) // 2 # posição central da lista

valor = int(input('Escolha um valor: ')) # valor que será buscado na lista

while True:
    if valor == lista[metade]: # se o valor procurado estiver no centro da lista
        print(f'{valor} está na lista!') # o valor foi encontrado
        break

    elif valor > lista[metade]: # se o valor procurado for maior que o valor no centro da lista
        início = metade + 1 # realiza a próxima busca na metade direita da lista
               
    elif valor < lista[metade]: # se o valor procurado for menor que o valor no centro da lista
        final = metade - 1 # realiza a próxima busca na metade esquerda da lista

    if início > final: # se a posição inicial for maior que a posição final
        print(f'{valor} não está na lista!') # o valor não está na lista
        break

    metade = (início + final) // 2 # calcula a posição central a cada iteração
