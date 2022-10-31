sexo: str
resposta: str
totalNao: int
totalSim: int
mulheresSim: int
homensNao: int
homensSim: int
homensTotal: int
percenHomens: float

sexo = ""
resposta = ""
totalSim = 0
mulheresSim = 0
totalNao = 0
perHomens = 0
homensNao = 0
homensSim = 0
homensTotal = 0

for n in range(1, 11):
    sexo = input("Digite seu sexo (F - FEMININO | M - MASCULINO): ")
    resposta = input("Qual sua resposta? (S — SIM | N — NÃO)")

    if resposta == "S":
        totalSim += 1
        if sexo == "F":
            mulheresSim += 1
        else:
            homensSim += 1

    if resposta == "N":
        totalNao += 1
        if sexo == "M":
            homensNao += 1

homensTotal = homensNao + homensSim
percenHomens = homensNao / homensTotal * 100

print("O número de pessoas que responderam sim: ", totalSim)
print("O número de pessoas que responderam não: ", totalNao)
print("O número de mulheres que responderam sim: ", mulheresSim)
print("A percentagem de homens que responderam não, entre homens: ", perHomens)