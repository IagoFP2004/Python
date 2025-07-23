import random #Importamos la libreria para generar numeros aleatorios

decisiones = [] #Lista donde almacenaremos las decisiones 

#Funcion que detiene la ejecucion de la aplicacion
def detenerEjecucion(respuesta):
    if(respuesta == "si"):
        return True
    elif(respuesta == "no"):
        return False
    else:
        return None
    
#Funcion que toma la decision
def elegirDecision(decisiones):
   decision = random.choice(decisiones)#Elige de manera aleatoria un elemento de la lista
   print(f"\n👉 La decisión seleccionada es: {decision}")#Muestra el resultado
   exit()#Finaliza la ejecucion del programa

print("¡BIENVENIDO A LA RULETA DE LAS DECISIONES!") #Mensaje que se mirara segun se ejecute la aplicacion

while True: #Bucle principal
    #Se pedira al usuario que introduzca una decision y la añadira a la lista de decisiones
    #Nos preguntara si queremos seguir añadiendo decisiones, se usa lower para que no importe si se escribe en mayusculas o minusculas
    decision = input("Introduce una decision:")
    decisiones.append(decision)
    salir = input("Deseas añadir otra decision?: (si/no)").lower()

    while True: #Bucle que gestiona el flujo del programa
        #Si decimos que si queremos seguir añadiendo decisiones se repite el bloque de codigo anterior
        #Si decimos que no se ejecutara la funcion que toma una decision y finalizara el programa
        #Si la respuesta es diferente de "si" o "no" nos pedira que volvamos a responder
        decision = detenerEjecucion(salir)
        if decision is True:
           break
        elif decision is False:
            elegirDecision(decisiones)
        else:
            salir = input("Respuesta no válida. Escribe 'si' o 'no': ").lower()

