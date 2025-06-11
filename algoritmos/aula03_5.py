import random

x = int(input("Digite o valor minímo a ser gerado: "))
y = int(input("Digite o valor maxímo a ser gerado: "))

a = random.randint(x, y)
b = a - 1
c = a + 1

print(f"Valor gerado: {a}")
print(f"Valor antecessor do gerado: {b}")
print(f"Valor sucessor do gerado: {c}")