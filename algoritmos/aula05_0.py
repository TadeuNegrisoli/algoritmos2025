menu = print("""Pizzaria Bom Lar

1. Pedido
2. Formas de Pagamento
3. Reclamações
4. Falar com Atendente
""")

opcao = int(input("Digite o número correspondente: "))

if(opcao == 1):
    print("""
1. Realizar Pedido
2. Consultar Pedido
3. Cancelar Pedido
4. Voltar
""")
    opcao_pedido = int(input("Digite o número correspondente: "))
    if(opcao_pedido == 1):
        print("""
Sabores:
              
30. Calabresa com Azeitonas
31. Quatro Queijos
32. Alho e Óleo com Bacon
33. Calabresa com Mussarela
34. Frango com Milho
35. Frango e Catupiry com Bacon
36. Picanha com Queijo Provolone
37. Camarão com Catupiry
38. Cogumelos com Queijo Brie
39. Carne Louca
40. Pizza de Doce de Leite com Coco
""")
        sabor = int(input("Opção: "))
        if(sabor < 30 or sabor > 40):
            print()
    elif(opcao_pedido == 2):
        print("\nSeu pedido está:")
    elif(opcao_pedido == 3):
        cancelamento= input("\nDigite o motivo do cancelamento:")
        print("\nMotivo registrado! Pedido cancelado.")
elif(opcao == 2):
    print("""
1. Pix
2. Cartão de Crédito
3. Cartão de Débito
4. Dinheiro
5. Voltar
""")
elif(opcao == 3):
    print("\nReclamações")
    report = input("\nFaça sua reclamação: ")
    print("Reclamação registrada!")
elif(opcao == 4):
    print("\nFalar com Atendente")
else:
    print("\nOpção Inválida!")