endpoints = ["/login", "/produtos", "/pedidos"]

status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

# FUNÇÃO QUE VERIFICA SE UM STATUS CODE HTTP É SUCESSO
# 200-299 = SUCESSO
def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# Função que detecta 2 erros seguidos nos códigos HTTP de um ENDPOINT
# [200, 200, 401, 200, 500] --> /login   >> False
# [201, 500, 502, 201, 500] --> /pedidos >> True
def erros_seguidos(codigos_http):
    for i in range(len(codigos_http) - 1):
        codigo_atual = codigos_http[i]
        prox_codigo = codigos_http[i + 1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

def analisar_endpoint(codigos_http):
    qtd_sucessos = 0

    for codigo in codigos_http:
        if eh_sucesso(codigo):
            qtd_sucessos += 1

    qtd_requisicoes = len(codigos_http)
    qtd_erros = qtd_requisicoes - qtd_sucessos

    percentual_sucesso = (qtd_sucessos / qtd_requisicoes) * 100

    tem_erros_seguidos = erros_seguidos(codigos_http)

    if tem_erros_seguidos:
        classificacao = "Crítico"
    elif percentual_sucesso >= 80:
        classificacao = "Estável"
    else:
        classificacao = "Instável"

    return (qtd_sucessos, qtd_erros, percentual_sucesso, classificacao)

# Percorrendo toda a matriz

maior_qtd_erros = -1
endpoints_maior_erro = []

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    codigos_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(codigos_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Códigos HTTP: {codigos_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% de sucesso: {percentual:.1f}%")
    print(f"Classificação: {classificacao}")
    print("-" * 30)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoints_maior_erro = [nome_endpoint]
    elif erros == maior_qtd_erros:
        endpoints_maior_erro.append(nome_endpoint)

print(f"Endpoint(s) com mais erros: {', '.join(endpoints_maior_erro)} ({maior_qtd_erros})")