enino=5500
ejoven=7000
eadulto=9000
totalnino=0
totaljoven=0
totaladulto=0
sw=1
try:
    while sw==1:
        resp=int(input("Ingrese tipo de entrada: \n1.- Niño (1 a 13 años)\n2.- Jóven (14 a 21 años)\n3.- Adulto (Mayor a 22)\nDigite: "))
        if resp==1:
            total=enino
            cantent=int(input(f"El precio de su entrada es de ${enino} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total*=cantent
            totalnino+=cantent
            print(f"======BOLETA======\nCategoría: Niño\nCantidad de entradas: {cantent}\nTotal a pagar: ${total} pesos")
            total1=total
            print("Gracias por su compra, disfrute la función.")
        elif resp==2:
            total=ejoven
            cantent=int(input(f"El precio de su entrada es de ${ejoven} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total*=cantent
            totaljoven+=cantent
            print(f"======BOLETA======\nCategoría: Jóven\nCantidad de entradas: {cantent}\nTotal a pagar: ${total} pesos")
            total2=total
            print("Gracias por su compra, disfrute la función.")
        elif resp==3:
            total=eadulto
            cantent=int(input(f"El precio de su entrada es de ${eadulto} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total*=cantent
            totaladulto+=cantent
            print(f"======BOLETA======\nCategoría: Adulto\nCantidad de entradas: {cantent}\nTotal a pagar: ${total} pesos")
            total3=total
            print("Gracias por su compra, disfrute la función.")
        sw=int(input("Desea realizar otra compra?\n1.- Si\n2.- No\nDigite: "))
    totalent=(totalnino+totaljoven+totaladulto)
    print(f"La cantidad de entradas de categoría \"Niño\" vendidas es: {totalnino} ({((totalnino*100)//totalent)}% de las entradas totales.)")
    print(f"La cantidad de entradas de categoría \"Jóven\" vendidas es: {totaljoven} ({((totaljoven*100)//totalent)}% de las entradas totales.)")
    print(f"La cantidad de entradas de categoría \"Adulto\" vendidas es: {totaladulto} ({((totaladulto*100)//totalent)}% de las entradas totales.)")
    print(f"Total de ganancias del día: ${total1+total2+total3} pesos")
except:
    print("Digite opcion valida")