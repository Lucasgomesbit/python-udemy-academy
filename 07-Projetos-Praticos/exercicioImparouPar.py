"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numeros_inteiros = int(input('Digite um número: '))

par_ou_impar = numeros_inteiros % 2 == 0

if par_ou_impar == 0:
    print('Número digitado é par')
elif par_ou_impar > 0:
    print('Número digitado é impar')
else:
    print('Número informado não é inteiro')
