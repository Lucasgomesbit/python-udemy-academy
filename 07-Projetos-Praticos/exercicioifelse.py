'''''''''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
'''''''''

nome = str(input('Infome seu nome: '))
letras = len(nome)

if letras <= 4:
    print('Seu nome é curto.')
elif letras >= 5 and letras <= 6:
    print('Seu nome é normal.')
elif letras > 6:
    print('Seu nome é muito grande.')
else:
    print('Digite apenas letras')
