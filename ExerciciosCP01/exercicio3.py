#EX3) Faça um programa que peça dois números e imprima o maior deles, e informe caso eles sejam iguais.
numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite um numeor: "))

if numero_1 > numero_2:
    print("o numero",numero_1,"é maior que o numero", numero_2 )
elif numero_2 > numero_1:
    print("O numero",numero_2,"é maior que o", numero_1)
else:
    print("Os numeros são iguais")