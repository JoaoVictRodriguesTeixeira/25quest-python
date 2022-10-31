import os

idade: int
opin: int
otimo: int
bom: int
regular: int
mediaOtimo: float
somaOtimo: float
qntRegular: float
porcentagemBom: float

idade = 0
opin = 0
otimo = 0
bom = 0
regular = 0
mediaOtimo = 0
somaOtimo = 0

for n in range(1,3):
    idade = int(input("Digite sua idade: "))
    opin = int(input("| Ótimo — 3 | Bom — 2 | Regular — 1 | Classifique sua opinião: "))

    os.system ("cls")
    somaOtimo += idade

    if opin == 3 :
        otimo += 1
        somaOtimo += idade
    if opin == 1:
        regular += 1
    if opin == 2:
        bom += 1

mediaOtimo = somaOtimo / otimo
porcentagemBom = bom / 15 * 100

print("Média de pessoas que responderam ótimo: ", mediaOtimo)
print("Quantidade de pessoas que responderam regular: ", regular)
print("Porcentagem de pessoas que responderam bom, entre todos os analisados: ", porcentagemBom)