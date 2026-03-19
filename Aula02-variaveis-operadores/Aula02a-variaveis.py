print("olá mundo")

print("7+4")
print("7" + "4") #concatenando strings

#Comentário de 1 linha
'''
comentários de 
mútlipas
 linhas'''

#variavis
nome = "Matheus" #str
idade = 18 #int
peso = 89 # float

print(nome , idade, peso)

print("oiii \n", nome, idade, peso)
print(f'olá,{nome}!!')

#imput -- simulação de um formulario no cmd
nome = input("digite o seu nome")
print(nome)
idade = int(input("digite sua idade"))
peso = input("digite seu peso")
print(idade + 1)

ano_nascimento = 2007
ano_atual = 2026
idade_atual = ano_atual -  ano_nascimento
print(f"sua idade é:{idade_atual}")