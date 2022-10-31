idade: int
somaIdade: int
contIdade: int
mediaIdadesDigitadas: float

idade = 0
somaIdade = 0
contIdade = 0
mediaIdadesDigitadas = 0.0

while idade != 0:
    idade = int(input("Digite sua idade: "))

    somaIdade += idade
    contIdade += 1

mediaIdades = somaIdade / (contIdade - 1)

print("Média das idades digitadas: ", mediaIdadesDigitadas)