#EX6) Escreva um algoritmo que recebe dois números e um caractere (representando uma das operações matemáticas(+,-,*,/)
numero_1 = float(input("Ditigi um numero: "))
numero_2 = float(input("Ditigi um numero: "))
caractere = str(input("Ditige qual operação matematica deseja realizar(+,-,*,/): "))
soma = float(numero_1 + numero_2)
subtracao = float(numero_1 - numero_2)
multiplicacao = float(numero_1 * numero_2)
divisao = float(numero_1 / numero_2)

if caractere == '*':
    print("o resultado da sua conta foi: ",multiplicacao )
elif caractere == '/':
    print("o resultado da sua conta foi: ",divisao )
elif caractere == '+':
    print("o resultado da sua conta foi: ", soma )
elif caractere == '-':
    print("o resultado da sua conta foi: ", subtracao )
else:
    print("Erro, caracter n identificado")