#Ex7)Faça um programa que receba o ano de nascimento da pessoa e retorne
#Se o voto é obrigatorio este ano
#Se o voto é opcional este ano
#Se o voto é proibido este ano

ano_do_nascimento = int(input("Qual seu ano de nascimento: "))
if ano_do_nascimento >= 1900 and ano_do_nascimento <= 2026:
    str("valido")
else:
    print("Data invalida!")

idade = 2026 - ano_do_nascimento
if idade >=16 and idade <=18 // idade >70:
    print("voto não obrigatorio")
elif idade >18 and idade <70:
    print("Voto obrigatorio!")
if idade <16:
    print("Não pode votar" )