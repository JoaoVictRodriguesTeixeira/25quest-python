idade: int
peso: float

mediaFaixas1a10: float
mediaFaixas11a20: float
mediaFaixas21a30: float
mediaFaixas31ParaCima: float

somaPesosFaixas1a10: float
somaPesosFaixas11a20: float
somaPesosFaixas21a30: float
somaPesosFaixas31ParaCima: float

qtdPesosFaixas1a10: float
qtdPesosFaixas11a20: float
qtdPesosFaixas21a30: float
qtdPesosFaixas31ParaCima: float

mediaPesosFaixas1a10  =  0
mediaPesosFaixas11a20  =  0
mediaPesosFaixas21a30  =  0
mediaPesosFaixas31ParaCima  =  0

somaPesosFaixas1a10  =  0
somaPesosFaixas11a20  =  0
somaPesosFaixas21a30  =  0
somaPesosFaixas31Acima  =  0

qtdPesosFaixas1a10 = 0
qtdPesosFaixas11a20 = 0
qtdPesosFaixas21a30 = 0
qtdPesosFaixas31ParaCima = 0

for n in range (1, 16):
    idade = int(input("Informe sua idade: "))
    peso = float(input("Informe seu peso: "))

    if idade >= 1 and idade <= 10:
        somaPesosFaixas1a10  +=  peso
        qtdPesosFaixas1a10  +=  1

    if idade  >=  11 and idade  <=  20 :
        somaPesosFaixas11a20 += peso
        qtdPesosFaixas11a20 += 1

    if idade >= 21 and idade <= 30:
        somaPesosFaixas21a30  +=  peso
        qtdPesosFaixas21a30  +=  1

    if idade >= 31:
        somaPesosFaixas31ParaCima + peso
        qtdPesosFaixas31ParaCima += 1

if qtdPesosFaixas1a10 > 0:
    mediaPesosFaixa1a10 = somaPesosFaixas1a10 / qtdPesosFaixas1a10
    print("Mídia faixa 1 a 10 anos: ", mediaPesosFaixa1a10)
else :
    print("Não havia idade na faixa etária entre 1 a 10 anos")

if qtdPesosFaixas11a20 > 0:
    mediaPesosFaixa11a20 = somaPesosFaixas11a20 / qtdPesosFaixas11a20
    print("Mídia faixa 11 a 20 anos:", mediaPesosFaixa11a20)
else :
    print("Não havia idade na faixa etária entre 11 a 20 anos")

if qtdPesosFaixas21a30 > 0:
    mediaPesosFaixa21a30 = somaPesosFaixas21a30 / qtdPesosFaixas21a30
    print("Mídia faixa 21 a 30 anos: " , mediaPesosFaixa21a30)
else :
    print("Não havia idade na faixa etária entre 21 a 30 anos")

if qtdPesosFaixas31ParaCima > 0:
    mediaPesosFaixa31Acima = somaPesosFaixas31Acima / qtdPesosFaixas31ParaCima
    print("Mídia faixa 31 anos acima: ", mediaPesosFaixa31Acima)
else:
    print("Não houve idade na faixa acima de 31 anos")