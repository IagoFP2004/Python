#Pide tres números e imprime cuál es el mayor.
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

if numero1 >= numero2 and numero1 >= numero3:
    print(f"El número mayor es: {numero1}")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"El número mayor es: {numero2}")
else:
    print(f"El número mayor es: {numero3}")