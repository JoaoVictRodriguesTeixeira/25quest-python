import math

num: int
somaPares: int
somaPrimos: int
contPrimo: int

contPrimo = 0
somaPares = 0
somaPrimos = 0
for n in range(1, 10):
    num = int(input("Digite um número: "))
    if num / 2 == 0:
        somaPares += num

for n in range(1, int(math.sqrt(num)+1)):
    if num / 2 == 0:
        contPrimo += 1

    if contPrimo == 0:
        somaPrimos += num
    
print(f"Soma dos números pares: {somaPares}")
print(f"Soma dos números primos: {somaPrimos}")