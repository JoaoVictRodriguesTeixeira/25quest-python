valorCarro: float
precoAVista: float
taxaJuros: float

valorCarro = 0
precoAVista = 0
taxaJuros = 0.03

valorCarro = float(input("Digite o valor do carro: "))

precoAVista = valorCarro  - (valorCarro * 0.20)
print("QUANTIDADE DE PARCELAS - % JUROS")    
for n in range (6, 66, 6):
    print(f" {n} - {valorCarro  +  valorCarro * taxaJuros} ")
    taxaJuros  =  taxaJuros  +  0.03