import math

x = float(input("Digite um número: "))
x1 = 2 * x
x = math.pow(x, 2)
x = x - 4
x = math.sqrt(x)
x = x / x1

print(f"{x:.2f}".replace(".", ","))