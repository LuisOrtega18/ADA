import random
import time

def particion(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = particion(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

if __name__ == "__main__":
    n_elementos = int(input("Ingresa la cantidad de números aleatorios: "))
    n_random = [random.randint(1, 1000) for _ in range(n_elementos)]

    print("\nLos números aleatorios generados son:")
    print(n_random)

    i_tiempo = time.time()
    quicksort(n_random, 0, len(n_random) - 1)
    f_tiempo = time.time()

    print("\nLos números ordenados son:")
    print(n_random)

    e_tiempo = f_tiempo - i_tiempo
    print(f"\nEl tiempo de ejecución del algoritmo fue de {e_tiempo} segundos")
