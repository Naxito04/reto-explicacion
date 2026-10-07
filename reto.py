def calcular_precio(precio, cantidad=1):
    """Calcula el precio total multiplicando el precio unitario por la cantidad.

    Args:
        precio (float | int): El precio unitario del producto o artículo.
        cantidad (int, optional): El número de unidades a comprar. Por defecto es 1.

    Returns:
        float | int: El precio total resultante de la operación.
    """

    return precio * cantidad

# Dos argumentos
print(calcular_precio(10,3))

# Un argumento
print(calcular_precio(10))
