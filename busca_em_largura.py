# Dicionário contendo os vértices e suas ligações
vértices = {
    'A': ['B', 'C', 'D'],
    'B': [],
    'C': ['E', 'F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

# Dicionário contendo o STATUS de cada vértice
STATUS = {
    'A': 1,
    'B': 1,
    'C': 1,
    'D': 1,
    'E': 1,
    'F': 1,
    'G': 1
}

# Listas que receberão os vértices
FILA = []
processados = []

# Cria a função que realiza a Busca em Largura
def busca_em_largura(vértices, STATUS, nó):

    FILA.append(nó)  # Coloca o vértice inicial na FILA
    STATUS[nó] = 2  # muda o STATUS do vértice inicial para 2

    while FILA:  # Até a FILA estar vazia
        primeiro = FILA.pop(0)  # Remove o primeiro elemento da FILA
        processados.append(primeiro)  # Adiciona o primeiro elemento na lista de processados
        STATUS[primeiro] = 3  # muda o STATUS do primeiro elemento para 3

        for vizinho in vértices[primeiro]:  # Para cada vizinho do primeiro elemento da FILA
            if STATUS[vizinho] == 1:  # Se o STATUS do vizinho for igual a 1
                FILA.append(vizinho)  # Adicione o vizinho ao final da FILA
                STATUS[vizinho] = 2  # Mude o STATUS do vizinho para 2

            elif STATUS[vizinho] == 2 or STATUS[vizinho] == 3:  # Se o STATUS do vizinho for igual a 2 ou 3
                continue  # Ignore esse vizinho

# Usa a função que realiza a Busca em Largura
busca_em_largura(vértices, STATUS, 'A') # O vértice "A" é definido como nó inicial

# Apresenta o resultado da Busca em Largura
print('Resultado da Busca em Largura:')
print(processados)
