# dicionário contendo os vértices e suas ligações
vértices = {
    'A': ['B', 'C', 'D'],
    'B': [],
    'C': ['E', 'F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

# dicionário contendo o status de cada vértice
status = {
    'A': 1,
    'B': 1,
    'C': 1,
    'D': 1,
    'E': 1,
    'F': 1,
    'G': 1
}

# listas que receberão os vértices
fila = []
processados = []

# cria a função que realiza a Busca em Largura
def busca_em_largura(vértices, status, nó):

    fila.append(nó)  # coloca o vértice inicial na fila
    status[nó] = 2  # muda o status do vértice inicial para 2

    while fila:  # enquanto houver elementos na fila
        primeiro = fila.pop(0)  # remove o primeiro elemento da fila
        processados.append(primeiro)  # adiciona o primeiro elemento na lista de processados
        status[primeiro] = 3  # muda o status do primeiro elemento para 3

        for vizinho in vértices[primeiro]:  # para cada vizinho do primeiro elemento da fila
            if status[vizinho] == 1:  # se o status do vizinho for igual a 1
                fila.append(vizinho)  # adicione o vizinho ao final da fila
                status[vizinho] = 2  # mude o status do vizinho para 2

            elif status[vizinho] == 2 or status[vizinho] == 3:  # se o status do vizinho for igual a 2 ou 3
                continue  # ignore esse vizinho

# chama a função que realiza a Busca em Largura
busca_em_largura(vértices, status, 'A') # o vértice "A" é definido como nó inicial

# apresenta o resultado da Busca em Largura
print('Resultado da Busca em Largura:')
print(processados)
