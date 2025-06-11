print("\nPizzaria Bom Lar")
print("----------------")
print("1. Pedido\n2. Formas de Pagamento\n3. Reclamações\n4. Falar com Atendente\n")

opcao = int(input("Opção: "))

if(opcao == 1):
    print("----------------")
    print("1. Realizar Pedido\n2. Formas de Pagamento\n3. Cancelar Pedido\n")
    pedido = int(input("Opção: "))
    if(pedido == 1):
        print("----------------")
        print("Sabores:\n")
        print("30. Calabresa com Azeitonas\n31. Quatro Queijos\n32. Alho e Óleo com Bacon\n33. Calabresa com Mussarela\n34. Frango com Milho\n35. Frango e Catupiry com Bacon\n36. Picanha com Queijo Provolone\n37. Camarão com Catupiry\n38. Cogumelos com Queijo Brie\n39. Carne Louca\n40. Pizza de Doce de Leite com Coco\n")
        sabor = int(input("Opção: "))
        if(sabor >= 30 or sabor <= 40):
            print("----------------")
            print("Tamanhos e Valores:\n")
            print("1. P = R$35,00\n2. M = R$48,90\n3. G = R$59,90\n")
            tamanho = int(input("Opção: "))
            if(tamanho >= 1 or tamanho <= 3):
                print("----------------")
                print("Você deseja que seja entregue?:\n")
                print("1. Sim! (Valor Frete = R$10,00)\n2. Não, retirada.")
                entrega = int(input("Opção: "))            