def busqueda_binaria(arr):
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        if arr[mitad] == mitad:
            return mitad
        elif arr[mitad] < mitad:
            izquierda = mitad + 1
        else:
            derecha = mitad - 1
    return -1  # Si no existe índice mágico



