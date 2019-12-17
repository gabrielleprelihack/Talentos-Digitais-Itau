caractere = str(input('Caractere para fazer a escadinha: '))
numero_degraus = int(input('Número de degraus da escada: ')) + 1
for c in range(1, numero_degraus):
    print(caractere * c)
    c += 1