import random

def dau_6():
    numero = random.randint(1 , 6)
    print(numero)
dau_6()






import random

def dau_6():
    numero = random.randint(1, 6)
    return numero

def tiradas_dado(cantidad_dados, cantidad_tiradas):
    resultados_totales = []
    for _ in range(cantidad_tiradas):
        resultados = [dau_6() for _ in range(cantidad_dados)]
        resultados_totales.append(resultados)
    return resultados_totales

cantidad_dados = int(input("¿Cuántos dados deseas lanzar?: "))
cantidad_tiradas = int(input("¿Cuántas tiradas deseas realizar?: "))

resultado = tiradas_dado(cantidad_dados, cantidad_tiradas)
print("\nResultados de las tiradas:")
for i, tirada in enumerate(resultado, start=1):
    print(f"Tirada {i}: {tirada}")





import random

def dau_x(num_caras):
    numero = random.randint(1, num_caras)
    print(f"El resultado de la tirada del dado de {num_caras} caras es: {numero}")


num_caras = int(input("¿De cuántas caras es el dado?: "))

dau_x(num_caras)






import random

def dau_x(num_caras):
    numero = random.randint(1, num_caras)
    return numero

def daus_x():
    num_caras = int(input("¿De cuántas caras es cada dado?: "))
    cantidad_dados = int(input("¿Cuántos dados deseas lanzar?: "))

    resultados = []
    for i in range(cantidad_dados):
        resultado = dau_x(num_caras)
        resultados.append(resultado)

    print(f"\nResultados de la tirada de los {cantidad_dados} dados de {num_caras} caras:")
    for i in range(cantidad_dados):
        print(f"Dado {i+1}: {resultados[i]}")

daus_x()
