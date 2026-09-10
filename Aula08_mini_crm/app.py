from model import model_lead
import control

def add_lead():
    name =input("Nome: ")
    email = input("E-mail: ")
    company = input("Empresa: ")
    step = input("Etapa de vendas: ")
        
    #validar as entradas do usuario 
    # Depois de validar... vamos modelar os dados
    print(model_lead(name,email,company,step))
      
    # Depois de modelado... vamos enviar esse dict (leads) para o leads.json
    # para salvar, vamos usar o módulo control
    control.create_lead(model_lead(name,email,company,step))


def main():
    print("\nMIni CRM de Leads")
    print("[1] Adicionar lead")
    print("[2] Listar leads")
    print("[0] Sair do programa")
    
    opt = input("Escolha uma oção: ")
    while True:
        if opt == "1":
            add_lead()
        elif opt == "2":
            print("Lista leads")
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")
            

if __name__ == "__main__":
    main()