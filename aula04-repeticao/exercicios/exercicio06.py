#Faça um programa capaz de exibir todos os valores pares entre 2 e um valor fornecido pelo usuário.

num_1 = int(input("Digite um numero: "))

for n in range(num_1):
    if n % 2 == 0:
        print(n)
    