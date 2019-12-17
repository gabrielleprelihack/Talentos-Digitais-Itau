saldo = 500
tentativa = 1
senha_correta = 123456
valor_saque = 0
numero_conta = str(input('Insira o número da conta: '))
senha = int(input('Insira a sua senha: '))
if senha == senha_correta:
    valor_saque = int(input('Insira o valor do saque: '))
else:
    print('Senha incorreta.')
    while senha != senha_correta and tentativa <= 3:
        senha = int(input('Tente novamente: '))
        tentativa += 1
        if senha == senha_correta:
            valor_saque = int(input('Insira o valor do saque: R$'))
        elif tentativa == 3:
            print('Excedeu o número de tentativas. Senha bloqueada')
            exit()
if valor_saque <= saldo:
    senha = int(input('Confirme a sua senha: '))
    if senha == senha_correta:
        print('Saque aprovado! Aguarde a contagem das notas')
    else:
        print('Senha incorreta.')
        while senha != senha_correta and tentativa <= 3:
            senha = int(input('Tente novamente: '))
            tentativa += 1
else:
    while valor_saque > saldo:
        outro_valor = str(input('Saldo indisponível. Deseja sacar outro valor? [S/N]: '))[0].upper()
        if outro_valor in 'S':
            valor_saque = int(input('Insira o valor do saque: R$'))
            if valor_saque <= saldo:
                senha = int(input('Confirme a sua senha: '))
                if senha == senha_correta:
                    print('Saque aprovado! Aguarde a contagem das notas')
                else:
                    print('Senha incorreta.')
                    while senha != senha_correta and tentativa <= 3:
                        senha = int(input('Tente novamente: '))
                        tentativa += 1
        else:
            exit()