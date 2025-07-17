numero1 = 0
numero2 = 1

# Imprime los números de la secuencia de Fibonacci hasta el número 100.
for i in range(100):
    print(numero1)
    siguiente_numero = numero1 + numero2
    numero1 = numero2
    numero2 = siguiente_numero

    if numero1 > 100:
        break

