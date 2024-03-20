import random
import time

def busqueda_binaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1


cantidad = int(input("Ingrese la cantidad de números aleatorios: "))
n_buscar = int(input("Ingrese el número a buscar: "))

l_aleatoria = [random.randint(1, 10000000) for _ in range(cantidad)]
l_aleatoria.sort()

print("La lista ordenada es:", l_aleatoria)


t_inicio = time.time()
resultado = busqueda_binaria(l_aleatoria, n_buscar)
t_final = time.time()



if resultado != -1:
    print(f"El número {n_buscar} se encuentra en la posición {resultado}.")
else:
    print(f"El número {n_buscar} no se encuentra en la lista.")

e_tiempo = t_final - t_inicio
print(f"El tiempo de ejecución fue de {e_tiempo} segundos.")
