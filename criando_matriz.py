numero_linhas = int(input('Insira a quantidade de linhas: '))
numero_colunas = int(input('Insira a quantidade de colunas: '))

matriz = [] # lista contendo todas as linhas e colunas da matriz

for lin in range(numero_linhas): # laço responsável pela quantidade de linhas
    linha = [] # lista temporária que representa cada linha
    
    for col in range(numero_colunas): # laço responsavel pela quantidade de colunas
        valor = input(f'Insira o {col + 1}º valor da {lin + 1}º linha: ').center(3) # Define os valores e centraliza-os em 3 caracteres
        linha.append(valor) # adiciona o valor à lista
        
    matriz.append(linha) # adiciona cada linha à matriz

print(f'\nMatriz {numero_linhas} x {numero_colunas}:') # mensagem informando o formato da matriz

for i in matriz:
    print(f'| {" ".join(i)} |') # apresenta cada linha individualmente
