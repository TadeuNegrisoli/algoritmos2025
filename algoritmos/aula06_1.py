import random

x = 0
a = 0

while(a!=10):
    a = random.randint(1, 10)
    if(a % 2):
        pass
    else:
        print(a)
        x = x + 1
    
print(f"Foi gerado {x} vezes.")