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

    FILA.append(nó)  # Coloca o vértice inicial 'A' em FILA
    STATUS[nó] = 2  # muda o STATUS de 'A' para 2

    while FILA:  # Até a FILA estar vazia
        N = FILA.pop(0)  # Remova o vértice da frente (N) de FILA
        processados.append(N)  # Adiciona N para a lista de processados
        STATUS[N] = 3  # muda o STATUS de N para 3

        for J in vértices[N]:  # Para cada vizinho (J) de N
            if STATUS[J] == 1:  # Se o STATUS de J for igual a 1
                FILA.append(J)  # Adicione J ao final da FILA
                STATUS[J] = 2  # Mude o STATUS de J para 2

            elif STATUS[J] == 2 or STATUS[J] == 3:  # Se o STATUS de J for igual a 2 ou 3
                continue  # Ignore o vértice J

# Usa a função que realiza a Busca em Largura

busca_em_largura(vértices, STATUS, 'A')

# Apresenta o resultado da Busca em Largura
print('Resultado da Busca em Largura:')
print(processados)
