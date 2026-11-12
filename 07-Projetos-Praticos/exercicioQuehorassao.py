'''Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

print('Que horas são...')

horas = float(input('Informe a hora: '))


if horas >= 0.00 and horas <= 11.59:
    print('Bom dia...')
elif horas >= 12.00 and horas <= 17.59:
    print('Boa tarde...')
elif horas >= 18.00 and horas <= 23.59:
    print('Boa noite...')
else:
    print('Nenhuma hora foi digitada')
    