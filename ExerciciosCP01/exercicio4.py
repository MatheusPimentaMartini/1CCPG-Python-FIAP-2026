#EX4)Faça um programa para a leitura de quatro notas parciais de um aluno. O programa deve calcular a média alcançada pelo aluno e apresentar:

nota_primeiro_bimestre = float(input("Digite a nota do Primeiro bimestre: "))
nota_segundo_bimestre = float(input("Digite a nota do Segundo bimestre: "))
nota_Terceiro_bimestre = float(input("Digite a nota do Terceiro bimestre: "))
nota_Quarto_bimestre = float(input("Digite a nota do Quarto bimestre: "))

#Caculo de média
media = (nota_primeiro_bimestre + nota_segundo_bimestre + nota_Terceiro_bimestre + nota_Quarto_bimestre)/ 4
if media >= 6:
    print("Aprovado!")
elif media >= 4 and 6:
    print("Recuperação!")
else:
    print("Reprovado!")