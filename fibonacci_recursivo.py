# função recursiva que retorna o valor da sequência de fibonacci em uma determinada posição
def fibonacci(num): # "num" representa a posição do valor na sequência de fibonacci
    if num <= 0: # se o número for menor ou igual a 0
        return 0 # retorne 0
    elif num == 1: # se o número for igual a 1
        return 1 # retorne 1
    else: # se o número for maior que 1
        return fibonacci(num - 1) + fibonacci(num - 2) # retorne a soma dos dois elementos anteriores

qnt = int(input('Quantos valores deseja ver? ')) # Define quantos elementos da sequência de fibonacci serão exibidos

print('Sequência de Fibonacci:', end=' ')

for i in range(qnt): # itera de 0 até a quantidade escolhida
    print(fibonacci(i), end=' ') # apresenta os valores da sequência de fibonacci
