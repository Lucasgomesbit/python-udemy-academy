# Nivel intermediario 

'''
- Introdução às funções (def) em python
- Funções são trechos de código usados para replicar determinada ação ao longo do seu código
- Elas podem receber valores por parâmetros (argumentos) e retornar uma valor específico
'''
# exemplo:

'''def saudacao(nome):
    # SAUDACAO = FUNÇÃO
    # NOME = PARAMETRO

def saudacao (nome = 'sem nome'):
    # = atribuir um valor para quando não for passado nenhuhm valor.
'''
    
def saudacao(nome):
    print(f'Olá {nome}!')
    
saudacao('Lucas')
# O que será imprimido todas as vezes que for chamado a funcao

saudacao('Gomes')
# Pode ser chamado quantas vezes quiser em varios valores diferentes

saudacao('Ana Banana')