nomes = ['Matheus', 'Guylherme', 'Aline', 'André', 'João']
nomes.sort(reverse=True)
aluno = 0
len_nomes = len(nomes) - 1
letra_u = input('Insira a letra inicial desejada: ')
while len_nomes != -1:
    if nomes[len_nomes][0] == letra_u:
        print(nomes[len_nomes])
        len_nomes -= 1
        aluno += 1
    else:
        len_nomes -= 1
if aluno == 0:
    print('Não há alunos com essa letra inicial')