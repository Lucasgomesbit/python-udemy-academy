print('Lista de compras')

import os 

lista = []
while True:
    print('Selecione uma opção ')
    opcao = input(' [i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system ('cls')
        produto = input ('Produto: ')
        lista.append(produto)
    elif opcao == 'a':
        indice_str = input (
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista [indice]
        except ValueError:
            print('Digite um número inteiro')
        except IndexError:
            print('Indice não existe na lista ')
        except Exception:
            print('Erro desconecido')
    elif opcao == 'l':
        os.system ('cls')
        if  len (lista) == 0:
            print('Nada para listar')
        for i, produto in enumerate (lista):
            print(i, lista)        

