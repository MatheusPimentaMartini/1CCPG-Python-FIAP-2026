while True:
    numero = int(input("Digite um numero par qualquer: "))
    if numero % 2 == 0:
        break
    print("Digite um numero par.")
soma = 0
for i in range (1, numero + 1):
    soma += i
print(soma)
    
    