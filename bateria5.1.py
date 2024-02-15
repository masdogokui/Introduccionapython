Temperatura = float(input("Introduce los grados Cº: ")) 
respuesta = (Temperatura * 9/5) + 32  
print("La temperatura en grados Fahrenheit es:", respuesta)  

factorial = int(input("Introduce un número para calcular su factorial: ")) 
resultado = 1
for i in range(1, factorial+1):
    resultado *= i  
print("El factorial de", factorial, "es:", resultado)
