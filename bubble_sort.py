lista = [17, 4, 23, 8, 19, 12]

print('Lista desorganizada:', lista)

c = 1 # flag que inicia o looping while

while c != 0: # enquanto c for diferente de 0
    c = 0 # se nenhum valor for invertido, o laço será finalizado
    for i in range(1, len(lista)): # verifica cada elemento da lista a partir do segundo
        if lista[i] < lista[i - 1]: # se o valor da frente for menor que o valor de trás
            lista[i], lista[i - 1] = lista[i - 1], lista[i] # inverte os valores
            c = 1 # se algum valor tiver sido invertido, o laço reinicia

print('Lista organizada:', lista)
