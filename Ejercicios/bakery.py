# Una panadería vende barras de pan a 3.49$ cada una. El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace 
# por no ser fresca y el coste final total.


def run():
   sold = int(input("How many yesterday breads did you sell today?: "))
   bread = round(3.49 * sold, 2)
   discount = bread * 0.6
   total = bread - discount
   print("The bread price is: $" + str(bread))
   print("The 60% discount is: $" + str(round(discount, 2)))
   print("The total to pay is: $" + str(round(total, 2)))


if __name__ == "__main__":
    run() 