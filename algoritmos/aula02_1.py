import math

x = float(input("Digite valor de x: "))
y = float(input("Digite valor de y: "))

cima = x + math.pow(y, 3)
baixo = math.log10(x)
resultado = math.sqrt(cima/baixo)
resultadoFormatado = f"{resultado:.2f}".replace(".", ",")

print(f"Resultado da equação: {resultadoFormatado}.")