import os

while(True):
    try:
        email= input("\nDigite seu email até o @: ")
        if(len(email)>5 and not("@" in email)):
            break
        else:
            print("\nEmail deve ser maior que cinco caracteres e não pode conter a extensão!")
    except ValueError:
        print("\nEmail informado de forma incorreta!")

print("\nDigite o número correspondente ao complemento da extensão do seu email:\n \n1. @estudantes.ifpr.edu.br\n2. @gmail.com\n3. @hotmail.com\n4. Outro")

emailCom= 0

while(True):
    try:
        emailCom= int(input("\nOpção: "))
        if(emailCom == 1 or 2 or 3 or 4):
            break
        else:
            print("\nDigite os números dados como opção!")
    except ValueError:
        print("\nDigite somente o número correspondente!")

if(emailCom == 1):
    email= f"{email}@estudantes.ifpr.edu.br"
elif(emailCom == 2):
    email= f"{email}@gmail.com"
elif(emailCom == 3):
    email= f"{email}@hotmail.com"
elif(emailCom == 4):
    while(True):
        try:
            email= input("\nDigite seu email completo: ")
            if("@" and ".com" in email and len(email) > 15):
                break
            elif("@" and ".edu" in email and len(email) > 15):
                break
            elif("@" and ".gov" in email and len(email) > 15):
                break
            else:
                print("\nO email digitado de forma incorreta!")
        except ValueError:
            print("\nInformação incorreta!")

print(f"\nEmail informado: {email}")

while(True):
    try:
        commit= input("\nDigite sua mensagem para o commit: ")
        if(len(commit) >= 10):
            break
        else:
            print("\nSua mensagem deve haver pelo menos 10 caracteres!")
    except ValueError:
        print("\nMensagem inválida!")

#configurar email
comando= f"git config user.email \"{email}\""
os.system(comando)

#identificar as novidades e incluir no commit
comando= f"git add *"
os.system(comando)

#registrar o commit com a mensagem
comando= f"git commit -m \"{commit}\""
print(f"\n{comando}")

#enviar para os servidores do github
comando= f"git push"
os.system(comando)