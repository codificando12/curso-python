def run():
    cap = int(input("¿Cuánto quieres invertir hoy?: "))
    interes = int(input("¿Qué tasa de interes deseas? "))
    years = int(input("¿Cuánto años quieres invertir? "))
    print("Invirtiendo " + str(cap) + " a una tasa del " + str(interes) + " anual " + "en " + str(years) + " año(s) vas a tener un total de " + str(round(cap 
          * (interes / 100 + 1) ** years, 2)))


if __name__ == "__main__":
    run()