#LOGICA E (and)

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if login:
    print("Entrar no programa")

#LOGICA OU (or)
logica_ou = False or False or True
print(logica_ou)

# Negacao
negacao = not False
print(negacao)

if not login:
    print("Loga certo ai...")

