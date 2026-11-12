frase = 'O python é uma linguagem de programação'\
    'multiperadigma'\
    'Python foi criado por Guido Van Rossum'

i = 0

while i < len(frase):
    letra_atual = frase [i]
    quants_vezes_letra_aparece = frase.count(letra_atual)
print(frase)