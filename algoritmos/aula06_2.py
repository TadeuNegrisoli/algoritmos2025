menu = """1. Contratar Plano
2. Suporte Técnico
3. Financeiro
4. Cancelamento
5. Sair"""

user = None

while(user != 5):
    print(menu, "\n")
    user = int(input("Opção: "))
    if(user == 1):
        print("\nRedirecionando para o setor de planos...\n")
    elif(user == 2):
        print("\nRedirecionando para o setor de suporte técnico...\n")
    elif(user == 3):
        print("\nRedirecionando para o setor financeiro...\n")
    elif(user == 4):
        print("\nRedirecionando para o setor de cancelamento...\n")
    elif(user == 5):
        print("\nSaindo do setor de atendimento...")
    else:
        print("\nOpção inválida! Tente novamente...\n")