def validar_nota(nota):
    nota_temp = nota
    while nota_temp < 0 or nota_temp > 10:
        print("A nota deve estar entre 0 e 10")
        nota_temp = float(input("Digite novamente a nota: "))
    return nota_temp

nota1 = float(input("Digite a primeira nota: "))
nota1 = validar_nota(nota1)
'''
while nota1 < 0 or nota1 > 10:
print("A nota deve estar entre 0 e 10")
nota1 = float(input("Digite novamente a primeira nota: "))
'''
nota2 = float(input("Digite a segunda nota: "))
nota2 = validar_nota(nota2)
'''
while nota2 < 0 or nota2 > 10:
print("A nota deve estar entre 0 e 10")
nota2 = float(input("Digite novamente a segunda nota: "))
'''
media = (nota1 + nota2)/2
print(f"A média é {media:.2f}")