# Cauculadora de IMC
# Início do recebimento de dados
altura = float(input('Insira a sua altura em metro: '))
peso = float(input('Insira o seu peso, em kilograma: '))
# Fim do recebimento de dados
# Inicio do tratamento de dados
imc = peso/(altura**2)
# Fim do tratamento de dados
# Inicio das saídas para o usuário
if imc < 18.5:
    print(f'Seu IMC é de {imc}, você está abaixo do peso.')
elif 24.9 > imc > 18.5:
    print(f'Seu IMC é de {imc}, você está em seu peso ideal')
elif 30 > imc > 24.9:
    print(f'Seu IMC é de {imc}, você está em sobrepeso')
else:
    print(f'Seu IMC é de {imc}, você está em obesidade')
# Fim das saídas para o usuário
# Fim do programa