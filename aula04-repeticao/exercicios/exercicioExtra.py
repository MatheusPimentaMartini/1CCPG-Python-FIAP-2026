n = int(input("Digite um numero inteiro:\n"))
while n<=0:
    print("numero invalido!")
    n = int(input("Digite um numero inteiro:\n"))


for num in range(11):   
    print(f"a tabuada do numero {n} é {n} X {num} = {n*num}")