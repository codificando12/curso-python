def run():
    cap = input("¿Cuánto quieres invertir hoy?: ")
    interes = input("¿Qué tasa de interes deseas? ")
    
    # years = input("¿Cuánto años quieres invertir? ")
    print("Invirtiendo " + str(cap) + " a una tasa del " + str(interes) + " anual " + " en " 
    + " vas a tener un total de " + str(int(cap) * (int(interes)/ 100) + cap))


if __name__ == "__main__":
    run()