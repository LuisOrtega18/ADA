import random
import time

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    m_izquierda = arr[:mid]
    m_derecha = arr[mid:]

    left_sorted = mergesort(m_izquierda)
    right_sorted = mergesort(m_derecha)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    resultado = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1

    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado

if __name__ == "__main__":
    n_aleatorios = int(input("Ingresa la cantidad de números aleatorios: "))
    n_random = [random.randint(1, 1000) for _ in range(n_aleatorios)]

    print("\nLos números aleatorios generados son:")
    print(n_random)

    i_tiempo = time.time()
    n_ordenados = mergesort(n_random)
    f_tiempo = time.time()

    print("\nLos números ordenados son:")
    print(n_ordenados)

    e_tiempo = f_tiempo - i_tiempo
    print(f"\nEl tiempo de ejecución del algoritmo fue de {e_tiempo} segundos")



