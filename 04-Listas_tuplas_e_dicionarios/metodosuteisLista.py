# Métodos úteis para o tipo list:

'''
Append = adiciona um item ao final da lista
insert = adiciona um item no índice escolhido
pop = remove do final ou do índice escolhido
del = apaga um índice
clear = limpa a lista
extend = estende a lista 
+ or - = concatena listas '''

lista = [10, 20, 30, 40 ]
lista.append('Lucas')
nome = lista.pop()
lista.append(1234)
del lista [-1]
lista.insert(100,5) # O 100 é a posição para o item ser adicionado 
# O 5 é o valor para ser adicionado

print(lista)
