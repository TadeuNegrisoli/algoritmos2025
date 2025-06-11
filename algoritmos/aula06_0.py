import random

x = 0
a = 0

while(a!=7):
    a = random.randint(1, 10)
    x = x + 1
    print(a)
    
print(f"Foi gerado {x} vezes.")