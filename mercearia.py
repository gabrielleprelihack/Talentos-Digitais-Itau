carrinho = []
item = []
verificacao = 'S'
total = 0
controle = 0
print('='*50)
print('{:^50}'.format('Mercearia do Matheus'))
print('='*50)
while controle == 0:
    print('''Escolha uma opção:
[1] Adicionar um item ao carrinho
[2] Finalizar a compra''')
    escolha = str(input('Escolha: '))
    if escolha not in '12':
        escolha = str(input('Resposta inválida. Insira uma opção existente: '))
    elif escolha in '1':
        while verificacao == 'S':
            nome_produto = str(input('Nome do produto: '))
            preco_produto = str(input('Preço do produto: R$ '))
            quantidade_produto = str(input('Quantidade a ser comprada: '))
            item = [nome_produto, preco_produto, quantidade_produto]
            carrinho += [item]
            verificacao = str(input('Gostaria de adicionar outro ? [S/N]: '))[0].strip().upper()
    elif escolha in '2':
        print('='*50)
        len_carrinho = len(carrinho) - 1
        while len_carrinho != -1:
            print(f'''Nome do produto: {carrinho[len_carrinho][0]} 
Preço: {carrinho[len_carrinho][1]} 
Quantidade: {carrinho[len_carrinho][2]}''')
            print('-'*50)
            total += float(carrinho[len_carrinho][2]) * float(carrinho[len_carrinho][1])
            len_carrinho -= 1
        print('Preço total da compra: R${:.2f}'.format(total))
        controle = 1