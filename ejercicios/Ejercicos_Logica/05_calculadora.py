#Funcion para sumar
def suma(numero1, numero2):
    return numero1 + numero2
#Funcion para restar
def resta(numero1,numero2):
    return numero1 - numero2
#funcion para dividir
def division(numero1,numero2):
    if(numero2 != 0):
        return numero1 / numero2
    else:
        print("No se pueden dividir numeros por 0")
#funcion para multiplicar
def multiplicacion(numero1,numero2):
    return numero1 * numero2

#Funcion para detener la ejecucion del programa
def detenerEjecucion(respuesta):
    if(respuesta == "si"):
        return True
    elif(respuesta == "no"):
        return False
    else:
        return None

while True:
    #Entrada de datos al programa 
    numero1 = int(input("Introduce el primer numero: "))
    numero2 = int(input("Introduce el segundo numero: "))
    operador = input("Introduce la operacion que deseas realizar (+,-,*,/)")#Se indica el tipo de operacion que se quiere realizar

    #Segun la eleccion del operador ejecutara una u otra funcion
    match operador:
        case "+":
            print(suma(numero1, numero2))
        case "-":
            print(resta(numero1, numero2))
        case "*":
            print(multiplicacion(numero1, numero2))
        case "/":
            print(division(numero1, numero2))
        case _:#En caso de no coincidir con ninguna de las opciones anteriores muestra un mensaje
            print("Operador no reconocido. Por favor, utiliza +, -, * o /.")

    salir_del_programa = input("Desea salir del programa?(si/no): ").lower()#variable donde se manejara el flujo del bucle, se usa lower para que no importe si se escribe en mayusculas o minusculas
    #Si la respuesta a salir es si entonces se finaliza la ejecucion en caso de que sea que no el blucle continua
    #Si la respuesta no es "si" o "no" entonces te pide que vuelvas a responder 
    #Si la funcion detenerEjecucion devuelve True, el programa se detiene; si devuelve False, el bucle continúa.
    #En caso de devolver None, se solicita una respuesta válida.
    while True:
        decision = detenerEjecucion(salir_del_programa)
        if decision is True:
            exit()  # Termina el programa si la respuesta es "si"
        elif decision is False:
            break
        else:
            salir_del_programa = input("Respuesta no válida. Escribe 'si' o 'no': ")

