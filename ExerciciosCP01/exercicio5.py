#EX5)Faça um programa que leia 2 valores inteiros (A e b).
#A seguir, o programa deve mostrar uma mensagem "São Múltiplos" ou "Não são Múltiplos", indicando se os valores lidos são múltiplos entre si

#VALORES INTEIROS
numero_1 = int(input("Digite um numero a: "))
numero_2 = int(input("Digite um numero: "))

if numero_1 % numero_2 == 0:
    print("O numero", numero_1,"é múltiplo de ",numero_2)
else:
    print("O numero escolhido não é mútiplo de ",numero_2)