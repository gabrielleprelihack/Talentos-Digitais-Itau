numeros = [1, 15, 999, 78, 962]
resposta = input('Gostaria de imprimir em ordem crescente ou decrescente? [C/D]')[0].upper()
if resposta == 'C':
    numeros.sort()
    print(numeros)
elif resposta == 'D':
    numeros.sort(reverse=True)