pesos = input("¿Cuántos pesos argentinos tienes?: ")
pesos = float(pesos)
valor_dolar = 200
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")
