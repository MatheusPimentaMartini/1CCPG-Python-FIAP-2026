# Faça um programa que receba a quantidade de produtos que o usuário deseja
# A seguir, seu programa deve exibir a mensagem “Produto” a quantidade de vezes que o usuário solicitou.
# Utilize o laço for

qtd_produtos = int(input("Digite a quantidade de produtos: "))

for i in range(qtd_produtos):
    print(f"Produtos {i+1}")