import math

num: int; contPrimo: int; quantPrimo: int

num = 0
contPrimo = 0
quantPrimo = 0

for n in range(0, 10):
    num = int(input("Informe seu número: "))

    for n in range(2, int(math.sqrt(num)+1)):
        if num % n == 0:
            contPrimo += 1

    if contPrimo == 0:
        quantPrimo += 1

    contPrimo = 0

print(f"Quantidade de números primos apresentados: {quantPrimo}")