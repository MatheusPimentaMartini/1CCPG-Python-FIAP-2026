# Faça um programa que receba um número n
#▪ Exiba a tabuada deste número do 0 ao 25.
#▪ Utilize laços de repetição.

num=int(input("Tabuada do numero "))

for n in range (26):
    print(f"{num} x {n} = {num*n}")