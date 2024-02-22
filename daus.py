import random

def tirada_dau():
    resultado = random.randint(1, 6)
    print("El resultado de la tirada del dado de 6 caras es:", resultado)

tirada_dau()


def dau_6():
    numero = random.randint(1, 6)
    return numero

def tiradas_dado(cantidad_dados, cantidad_tiradas):
    resultados_totales = []
    for _ in range(cantidad_tiradas):
        resultados = [dau_6() for _ in range(cantidad_dados)]
        resultados_totales.append(resultados)
    return resultados_totales

def dau_x(num_caras):
    numero = random.randint(1, num_caras)
    print(f"El resultado de la tirada del dado de {num_caras} caras es: {numero}")
    return numero

def daus_x():
    num_caras = int(input("¿De cuántas caras es cada dado?: "))
    cantidad_dados = int(input("¿Cuántos dados deseas lanzar?: "))

    resultados_totales = []
    for _ in range(cantidad_dados):
        resultado = dau_x(num_caras)
        resultados_totales.append(resultado)

    print(f"\nResultados de la tirada de los {cantidad_dados} dados de {num_caras} caras:")
    for i, resultado in enumerate(resultados_totales, start=1):
        print(f"Dado {i}: {resultado}")

    return resultados_totales

while True:
    print("\nMenu:")
    print("1. Llençar un dau de 6 cares")
    print("2. Llençar més d'un dau de 6 cares")
    print("3. Llençar un dau de cares definides per usuari")
    print("4. Llençar més d'un dau de cares definides per usuari")
    print("5. Sortir")

    opcion = input("Selecciona una opció (1/2/3/4/5): ")

    if opcion == '1':
        print("\nLlençant un dau de 6 cares:")
        print("Resultat:", dau_6())
    elif opcion == '2':
        cantidad_dados = int(input("¿Cuántos dados deseas lanzar?: "))
        cantidad_tiradas = int(input("¿Cuántas tiradas deseas realizar?: "))
        resultados = tiradas_dado(cantidad_dados, cantidad_tiradas)
        print("\nResultados de las tiradas:")
        for i, tirada in enumerate(resultados, start=1):
            print(f"Tirada {i}: {tirada}")
    elif opcion == '3':
        num_caras = int(input("¿De cuántas caras es el dado?: "))
        dau_x(num_caras)
    elif opcion == '4':
        daus_x()
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3/4/5).")

        print(f"Dado {i+1}: {resultados[i]}")

daus_x()
