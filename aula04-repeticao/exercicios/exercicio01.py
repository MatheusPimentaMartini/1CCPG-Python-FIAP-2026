#Faça um programa que exiba a mensagem “Olá, Mundo”.
#▪ Essa mensagem deverá ser exibida repetidamente.
#▪ Ao final de toda iteração da repetição, você deve perguntar ao usuário se ele deseja exibir a mensagem novamente.
#▪ Se sim, exiba novamente. Senão, saia do loop e exiba a mensagem “Fim”.

while True:
    print("Olá Mundo!!")
    condicao = int(input("Deseja que a mensagem exiba novamente? Digite 1, caso contrario, digite dois: "))
    if condicao != "1":
        break
print("Fim")
