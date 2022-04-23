
def run():
    kilos = int(input("¿Cuál es tu peso en KG?: "))
    altura = input("Cuánto mides en metros (ejemplo: 1.20): ")
    altura = float(altura)
    imc = kilos / (altura**2)
    imc = round(imc, 2)
    print("Tu indice de masa corporal de: " + str(imc))

if __name__ == "__main__":
    run()