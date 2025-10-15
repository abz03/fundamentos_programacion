
carrito_compras = {}
precio_hamburguesa = 5800
precio_papas_fritas = 3000
precio_tocomple = 2500
precio_bebida = 1200
total_compra = 0

total_bebida = 0
total_papas = 0
total_hamburguesa = 0

def comprar_hamburguesa():
    global total_compra
    global total_hamburguesa
    global carrito_compras
    total_compra = total_compra + precio_hamburguesa
    total_hamburguesa = total_hamburguesa + 1
    carrito_compras['total_compra'] = total_compra
    carrito_compras['total_hamburguesa'] = total_hamburguesa

def comprar_papas():
    global total_compra
    global total_papas
    global carrito_compras
    total_compra = total_compra + precio_papas_fritas
    total_papas = total_papas + 1
    carrito_compras['total_compra'] = total_compra
    carrito_compras['total_papas'] = total_papas

def comprar_bebida():
    global total_compra
    global total_bebida
    global carrito_compras
    total_compra = total_compra + precio_bebida
    total_bebida = total_bebida + 1
    carrito_compras['total_compra'] = total_compra
    carrito_compras['total_bebida'] = total_bebida

def mostrar_carrito():
    global carrito_compras
    sumador = 0
    print("")
    print("Productos en el carrito:")
    for total in carrito_compras:
        sumador+=1
        print(f"{sumador}.- {total}.")

def terminar_compra():
    pass
    # como no pude ver el total de la compra pos no lo hice

def menu():
    while True:
        print("")
        print("Bienvenidos a una tienda de comida rapida, por favor seleccione lo que desea comprar:")
        print(f"1.- Hamburguesa: $ {precio_hamburguesa}")
        print(f"2.- Papas fritas: $ {precio_papas_fritas}")
        print(f"3.- Bebida: $ {precio_bebida}")
        print("4.- Mostrar carrito compras.")
        print("5.- Terminar la compra.")
        print("6.- Salir sin comprar.")
        print("")
    
        opcion = input("Seleccione una opción: ")
    
        if opcion == '1':
            comprar_hamburguesa()
        elif opcion == '2':
          comprar_papas()
        elif opcion == '3':
            comprar_bebida()
        elif opcion == '4':
            mostrar_carrito()
        elif opcion == '5':
            terminar_compra()
        elif opcion == '6':
            while True:
                print("Desea salir y sin terminar la compra?:")
                print("1.- Si")
                print("2.- No")
                if opcion == '1':
                    break
                elif opcion == '2':
                    menu()
                else:
                    print("Debe ingresar una opción válida, 1 o 2")       
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

menu()