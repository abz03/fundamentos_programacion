'''
Programa para carrito de compras
- Tienen que haber productos
- Tienen que haber usuarios
- Tiene que haber un carrito de compra que asocie los productos y sus cantidades, que quiere comprar un usuario
- Tiene que existir un código de descuento
    - Tiene solo letras mayúsculas, 6 caracteres y por lo menos 1 número
    - ej. 2BNM8YT
'''

codigo_descuento = {
    "2BNM8YT": 0.1,
    "UGLYKID47": 0.15,
}

productos = {
    "italiano": 2990,
    "dinamico": 3450,
    "chacarero": 3740,
    "papas_fritas": 1890
}

carritos = {
    "racsodia": {
        "productos": {
            "italiano": 3,
            "papas_fritas": 2
        },
        "total_compra": 0,
        "codigo_descuento": ""
    },
    "jorgeb": {
        "productos": {
            "italiano": 3,
            "papas_fritas": 2
        },
        "codigo_descuento": ""
    }
}

# Función que agregue productos al carrito
def agregar_producto(usuario, producto, cantidad):
    if producto in productos and usuario in carritos:
        if producto in carritos[usuario]["productos"]:
            carritos[usuario]["productos"][producto] += cantidad
        else:
            carritos[usuario]["productos"][producto] = cantidad

print(carritos)

agregar_producto("jorgeb", "dinamico", 2)
print(carritos)
agregar_producto("jorgeb", "dinamico", 1)
print(carritos)


# Función que elimine productos al carrito
def eliminar_producto(usuario, producto, cantidad):
    if producto in productos and usuario in carritos:
        if producto in carritos[usuario]["productos"]:
            carritos[usuario]["productos"][producto] -= cantidad
        else:
            print("El producto no está en su carrito")
    else:
        print("Ingrese datos validos")

eliminar_producto("jorgeb", "dinamico", 1)
print(carritos)

def calcular_boleta(usuario):                       # verificar que user tiene carrito
    if usuario in carritos:
        carrito_productos = carritos[usuario]["productos"]
        
        if len(carrito_productos) == 0:                       # verifica que el carrito no tiene productos y termina el programa con un mensaje
            print("El carrito no tiene productos")
            return

        subtotal = 0
        print("****** BOLETA ******")
        
        for nombre_producto in carrito_productos:          # Recorremos cada producto en el carrito ya que es un diccionario
            cantidad = carrito_productos[nombre_producto]  # Cuantos compra
            precio_unitario = productos[nombre_producto]   # Precio por producto, tomandolo del otro diccionario
            total_producto = cantidad * precio_unitario    # Precio total de ese producto, multiplica valor unitaro por precio_unitaro
            subtotal += total_producto                     # Sumamos al subtotal en cada vuelta
            
            print(f"{nombre_producto}: {cantidad} x {precio_unitario} = {total_producto}") # Detalle del producto
        total_detalle = 0.19 * subtotal
        print(f"SubTotal (sin IVA): {subtotal}")
        print(f"Total de su compra(con IVA): {total_detalle}")
    else:
        print("El usuario no tiene carrito creado") #Mensaje para cuando el usuario no tiene carrito creado:

# Ejemplo de uso:
calcular_boleta("jorgeb")
calcular_boleta("racsodia")