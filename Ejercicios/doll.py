# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo 
# y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos 
# y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule 
# el peso total del paquete que será enviado.


def run():
    quantity_clowns = int(input("How many clowns did you sell last order?: "))
    quantity_dolls = int(input("How many dolls did you sell last order?: "))
    clowns = 112
    dolls = 75
    print("The last order package will weight " + str(((quantity_clowns * clowns) + (quantity_dolls * dolls)) / 1000) + " kilograms")


if __name__ == "__main__":
    run()