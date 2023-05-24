# EJEMPLO DE USO DE REPOSITORIO

print("DATOS PERSONALES")
print("====================================")
vnom=input("Ingrese su nombre:  ")
while True:
    try:
        vedad=int(input("Ingrese su edad:  "))
        break
    except:
        print("Valor no corresponde")

print("====================================")
print(f"Su nombre es: {vnom}")
print(f"Su edad es: {vedad}")
print("Programa finalizado.................")