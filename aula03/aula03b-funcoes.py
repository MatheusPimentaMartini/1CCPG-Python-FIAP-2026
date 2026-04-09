#função sem retorno sem param
def print_lyrics():
    print("i ain't gonna live forever")
    print("I just want o live while I' am alive")

print_lyrics()

#função sem retorno com param
def boas_vindas(nome):
    print(f"ola, {nome}!! Seja bem-vindo")

nome = input("digite se nome")
boas_vindas(nome)

# FUNÇÃO COM RETORNO COM PARAM.
def soma(num_a,num_b):
    soma = num_a + num_b
    return soma

print(soma (10,5))
print(type(nome))