def holerite(salario, taxa_inss=0.09, vale_transporte=0.03, plano_saude=347):
    inss = salario * taxa_inss
    taxa_vt = salario * vale_transporte
    taxa_ps = plano_saude * 0.15
    salario_liquido = salario - inss - taxa_ps - taxa_vt
    print(f'''Salário integral: {salario}
INSS: {inss}
Vale transporte: {taxa_vt}
Plano de Saúde: {taxa_ps}
Salário Líquido: {salario_liquido}''')


def inss(salario_bruto, porcentagem=9):
    return salario_bruto * (porcentagem / 100)


def vale_transporte(salario_bruto, porcentagem=3):
    return salario_bruto * (porcentagem / 100)


def plano_saude(valor=347, porcentagem=15):
    return valor * (porcentagem/100)


def salario_liquido(salario_bruto):
    return salario_bruto - plano_saude(salario_bruto) - vale_transporte(salario_bruto) - plano_saude()


salario = float(input('Digá-me seu salário: R$'))
desconto_inss = inss(salario)
desconto_vt = vale_transporte(salario)
desconto_ps = plano_saude()
print(desconto_inss, desconto_vt, desconto_ps, salario_liquido(salario))