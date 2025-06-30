'''
    Funciones:
    - código reutilizable
    - modulariza un programa en pequeños programas
    - Hay 4 tipos:
        - sin argumentos y sin retorno
        - con argumentos y sin retorno
        - sin argumentos y con retorno
        - con argumentos y con retorno
    - Los argumentos (entradas a la función) y el retorno pueden ser
      tipos y/o estructuras de datos
    - Sólo se retorna en elemento
    - Los argumentos pueden ser más de uno
'''

#A continuación se define una funcion sin argumentos y sin retorno
def primer_saludo():
    print("Hola, mundoo!")

#A continuación SE UTILIZA la función
primer_saludo()

print("-"*60)
#A continuación se define una función con argumentos y sin retorno

def saludo_general(nombre, edad):
    if edad >= 18:
        print("Hola",nombre, " eres mayor de edad")
    else:
        print("Hola",nombre, " no eres mayor de edad")

saludo_general("Óscar",37)
saludo_general("Francisco", 16)

print("-"*60)
#A continuación se define una fución sin argumentos y con retorno
from random import randint

def nombres_aleatorios():
    nombres = ["Dayan","Mario","Ana","Santiago","Óscar","Felipe"]
    return nombres[randint(0,len(nombres)-1)]

for i in range(10):
    print(nombres_aleatorios())
    if nombres_aleatorios() == "Óscar":
        print("Hola profesor")
print("-"*60)
for i in range(10):
    n = nombres_aleatorios()
    print(n)
    if n == "Óscar":
        print("Hola profesor")

#A continuación se define una función con argumentos y con retorno

def cant_pares_impares(gatito,fin):
    pares = 0
    impares = 0
    for i in range(gatito,fin+1):
        if i % 2==0:
            pares+=1
        else:
            impares +=1
    return [pares,impares]

inicio = int(input("Ingrese un número inicial: "))
final = int(input("Ingrese un número final: "))

resultado = cant_pares_impares(inicio,final)

print("La cantidad de pares es:", resultado[0])
print("La cantidad de impares es:", resultado[1])