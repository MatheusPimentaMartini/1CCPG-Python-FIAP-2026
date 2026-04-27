print("While crescente")
cp = 0

while cp < 3:
    print(f"Produto {cp}")
    cp = cp + 1

print()

print("While descrescente")
i = 4

while i >= 0:
    print(f"Produto {i}")
    i -= 1

print()
print("Repetição")
# Repetição com entrada de usuario
jogar = "sim"

while jogar.lower() == "sim":
    print("Repete ou inicia o jogo")
    jogar = input("Deseja jogar novamente?")

print()
print("Modificadores de laço")
# Modificadores de laço break - continue

i = 0
while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue

    if i == 7:
        break

    print(f"Produto {i}")