x= int(input("Valor da tabuada: "))
y= int(input("Valor inicial: "))
z= int(input("Valor final: "))
z=z+1

for i in range(y, z):
    print(f"{x}x{i}= {x*i}")