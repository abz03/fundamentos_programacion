def verificar_numeros(lista):
    '''
    Verifica que todos los elementos de la lista sean números reales.
    Intenta convertirlos a float. Si falla, retorna False.
    '''
    try:
        for i in range(len(lista)):             # Recorre la lista usando índices
            lista[i] = float(lista[i])          # Convierte cada elemento a número decimal
        return True                             # Si todos se convierten bien, retorna True
    except ValueError:                          # Si alguna conversión falla, cae aquí
        print("Valor incorrecto ingresado, por favor ingresa números")
        return False                            # Retorna False si hay un error


def sumar_numeros(lista):
    '''
    Suma todos los números reales de una lista.
    '''
    suma = 0                                    # Inicializa la variable suma
    for numero in lista:                        # Recorre cada número en la lista
        suma += float(numero)                   # Convierte a float y lo suma
    return suma                                 # Retorna el resultado final


def multiplicar_numeros(lista):
    '''
    Multiplica todos los números reales de una lista.
    '''
    resultado = 1                               # Inicializa con 1 (elemento neutro de la multiplicación)
    for numero in lista:                        # Recorre cada número en la lista
        resultado *= float(numero)              # Convierte a float y multiplica
    return resultado                            # Retorna el producto final


def dividir_numeros(lista):
    '''
    Divide en orden los números de una lista.
    Retorna el resultado o un mensaje si hay división por cero.
    '''
    try:
        resultado = float(lista[0])                     # Tomamos el primer número
        for i in range(1, len(lista)):                  # Recorremos desde el segundo hasta el final
            numero = float(lista[i])                    # Convertimos cada número a float
            resultado /= numero                         # Dividimos el resultado actual entre ese número
        return resultado                                # Retornamos el resultado final
    except ZeroDivisionError:                           # Si alguno de los números es 0
        return "No se puede dividir por cero."          # Retornamos un mensaje de error


def calcular_factorial(numero):
    '''
    Calcula el factorial de un número entero.
    '''
    factorial = 1                               # Inicializa el resultado del factorial
    for i in range(1, numero + 1):              # Desde 1 hasta el número
        factorial *= i                          # Multiplica el acumulador por i
    return factorial                            # Retorna el resultado final


# ---- PROGRAMA PRINCIPAL ----

print("Bienvenido a la calculadora")  # Mensaje de bienvenida

while True:                                  # Bucle principal del programa
    print("\n¿Qué desea calcular hoy?")
    print('''
1) Suma de números
2) Multiplicar números
3) Calcular factorial
4) Dividir números
5) Salir
    ''')

    try:
        opcion = int(input("Seleccione una opción (1-5): "))  # Pide la opción al usuario
    except ValueError:
        print("Por favor, ingrese un número del 1 al 5.")   # Si no es número, error
        continue                                              # Vuelve al inicio del while

    if opcion == 5:
        print("Gracias por venir, nos vemos")                 # Si elige salir
        break                                                 # Sale del bucle

    elif opcion in [1, 2, 4]:                                 # Si la opción es suma, mult o división
        entrada = input("Ingrese los números separados por espacio: ")  # Pide números
        numeros = entrada.split()                            # Divide los números en una lista

        if verificar_numeros(numeros):                       # Verifica que todos sean válidos
            if opcion == 1:
                print("La suma es:", sumar_numeros(numeros))  # Llama a suma
            elif opcion == 2:
                print("La multiplicación es:", multiplicar_numeros(numeros))  # Multiplicación
            elif opcion == 4:
                print("El resultado de la división es:", dividir_numeros(numeros))  # División
        else:
            print("Error: Debe ingresar solo números reales.")  # Si hay error en verificación

    elif opcion == 3:                                         # Si la opción es factorial
        try:
            numero = int(input("Ingrese un número entero positivo para el factorial: "))  # Pide número
            if numero < 0:
                print("El número debe ser positivo.")        # No se puede factorial negativo
            else:
                print(f"El factorial de {numero} es: {calcular_factorial(numero)}")  # Muestra resultado
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")  # Si no es número válido

    else:
        print("Opción no válida. Intente nuevamente.")       # Si elige opción fuera del rango
