#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salario por mês



salario_atual = float(input("digite seu salario mensal em R$: "))

#reajustes

reajuste_1 = 1.20
reajuste_2 = 1.15
reajuste_3 = 1.10
reajuste_4 = 1.05

def calcular_reajuste(salario_atual, reajuste_1, reajuste_2, reajuste_3, reajuste_4):
    if salario_atual <= 280:
        salario_reajustado = float(salario_atual * reajuste_1)
    elif salario_atual > 280 and salario_atual <= 700:
        salario_reajustado = float(salario_atual * reajuste_2)
    elif salario_atual > 700 and salario_atual <= 1500:
        salario_reajustado = float(salario_atual * reajuste_3)
    else:
        salario_reajustado = float(salario_atual * reajuste_4)
    return salario_reajustado

salario_novo = calcular_reajuste(salario_atual, reajuste_1, reajuste_2, reajuste_3, reajuste_4)
print("Seu salario atual era de:", salario_atual, "porem com os novos rajustes seu salario é:", salario_novo) 
valor_do_aumento = salario_novo - salario_atual
print("O valor do aumento foi de: ",valor_do_aumento)

def calcular_o_percentual_de_aumento(reajuste_1, reajuste_2, reajuste_3, reajuste_4):
    if salario_atual <= 280:
        percentual_de_aumento = float(reajuste_1)
    elif salario_atual > 280 and salario_atual <=  700:
        percentual_de_aumento = float(reajuste_2)
    elif salario_atual > 700 and salario_atual <= 1500:
        percentual_de_aumento = float(reajuste_3)
    else:
        percentual_de_aumento = float(reajuste_4)
    return percentual_de_aumento

percentual_de_aumento = calcular_o_percentual_de_aumento(reajuste_1, reajuste_2, reajuste_3, reajuste_4)
print("O percentual de aumento foi de",percentual_de_aumento)