#lista_frutas[0] = "Banana"
#lista_frutas[1] = "Maçã"
#lista_frutas[2] = "Mo"
lista_frutas = ["Banata", "Maçã", "Morango"]

print(lista_frutas[1])

lista_frutas.append("Pera")
print(lista_frutas)

qtd_frutas = len(lista_frutas)
print("Qtd de frutas", qtd_frutas)

#for indexado para PERCORRER
for i in range(qtd_frutas):
    print(lista_frutas[i])


print()


#for EACH em python
for fruta in lista_frutas:
    print(fruta)


numeros = [0, 5, 11, 4]
for numero in numeros:
    print(numero)