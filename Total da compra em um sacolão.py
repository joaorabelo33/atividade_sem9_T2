
morango= float(input())
maca = float(input())

preco_morango_1 = morango * 2.20
preco_morango_2 = morango * 2.50

preco_maca_1 = maca * 1.5
preco_maca_2 = maca * 1.8

if morango > 5:
    valor_morango = preco_morango_1
else:
    valor_morango= preco_morango_2

if maca > 5:
    valor_maca = preco_maca_1
else:
    valor_maca = preco_maca_2

resultado = valor_maca  + valor_morango

if resultado > 25 or (maca + morango) > 8:
    resultado_final= resultado - (resultado * 0.1)
    print(f'{resultado_final:.2f}')
else:
    print(f'{resultado:.2f}')