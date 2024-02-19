while True:
    print("Bienvenido a la calculadora.")
    print("0. Salir")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Selecciona una opción (0-4): ")

    if opcion == "0":
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    elif opcion == "1":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print("La suma es:", num1 + num2)
    elif opcion == "2":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print("La resta es:", num1 - num2)
    elif opcion == "3":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print("La multiplicación es:", num1 * num2)
    elif opcion == "4":
        num1 = float(input("Ingresa el dividendo: "))
        num2 = float(input("Ingresa el divisor: "))
        if num2 != 0:
            print("La división es:", num1 / num2)
        else:
            print("Error: No se puede dividir entre 0.")
    else:
        print("Opción no válida. Por favor, selecciona una opción del 0 al 4.")
