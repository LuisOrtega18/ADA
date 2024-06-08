def distintos(arr):
    def search(arr, izquierda, derecha):
        if izquierda > derecha:
            return -1
        mitad = (izquierda + derecha) // 2
        val_medio = arr[mitad]
        if mitad == val_medio:
            return mitad
        # Buscar en el lado izquierdo
        izq_index = search(arr, izquierda, min(mitad - 1, val_medio))
        if izq_index != -1:
            return izq_index
        # Buscar en el lado derecho
        return search(arr, max(mitad + 1, val_medio), derecha)

    return search(arr, 0, len(arr) - 1)

