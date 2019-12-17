notas = []
soma = 0
contador = 0
numero_notas = int(input('Diga o número de notas: '))
while contador < numero_notas:
	contador += 1
	notas += [float(input(f'Insira a {contador}ª nota: '))]
len_notas = len(notas) - 1
while len_notas >= 0:
	soma += notas[len_notas]
	len_notas -= 1
media = soma/contador
if media > 7:
	print('o aluno com média {:.1f} está aprovado'.format(media))
elif 7 > media >= 5.5:
	print('O aluno com média {:.1f} está de recuperação'.format(media))
else:
	print('O aluno com média {:.1f} foi reprovado'.format(media))