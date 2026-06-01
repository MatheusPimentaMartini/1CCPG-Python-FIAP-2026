

while True:
    n = int(input("Digite um numero positivo:\n"))
    if n <= 0:
        print("Numero invalido, tente novamente")
    else:
        break
soma = 0
for num in range(1,n):
   soma += num 
print(f"A soma de 1 até {n} é de {soma}")