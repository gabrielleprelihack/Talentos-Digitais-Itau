from random import randint
from math import ceil
minimo = 1
maximo = 100
numero = randint(1, 100)
print('Pense em um número entre 1 e 100 e eu tentarei adivinhá-lo')
print('''[S] = Sim
[M] = Maior
[m] = Menor''')
print('='*60)
resposta = input(f'{numero}? [S/M/m]: ')[0].strip()
if resposta == 'S':
    print('Adivinhei')
else:
    while resposta != 'S':
        if resposta == 'M':
            minimo = numero
            numero = ceil((maximo + minimo)/2)
            resposta = input(f'{numero}? [S/M/m]: ')[0].strip()
        elif resposta == 'm':
            maximo = numero
            numero = ceil((maximo + minimo)/2)
            resposta = input(f'{numero}? [S/M/m]: ')[0].strip()
    print('Adivinhei! Uhuu!')