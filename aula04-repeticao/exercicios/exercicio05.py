#Faça um programa que receba 5 valores digitados pelo usuário e, ao final, informe qual é o maior
#deles.

i = 5
maior = 0
while i > 0:
    n = int(input("Digite um numero: "))
    i -= 1
    if n > maior:
        maior = n
print(f"o maior número é {maior}")