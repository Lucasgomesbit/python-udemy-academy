# Operaodr logico and 
# Todas as condições precisam ser verdadeiras. 
# se um valor for falso, o restante das expressoes também será falso

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Saiu')
