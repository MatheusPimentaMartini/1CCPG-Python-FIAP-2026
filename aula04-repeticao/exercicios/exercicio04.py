# Faça um programa que receba 5 valores digitados pelo usuário e, ao final, informe qual é a soma deles.
i = 5
soma = 0
while i > 0:
    n = int(input("Digite um numero: "))
    i -= 1
    soma += n

print(f"Os cinco números somados dão {soma}")