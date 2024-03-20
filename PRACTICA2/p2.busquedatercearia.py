import random
import time

def busqueda_ternaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        tercio = (fin - inicio) // 3
        p_medio1 = inicio + tercio
        p_medio2 = fin - tercio

        if lista[p_medio1] == elemento:
            return p_medio1
        elif lista[p_medio2] == elemento:
            return p_medio2
        elif elemento < lista[p_medio1]:
            fin = p_medio1 - 1
        elif elemento > lista[p_medio2]:
            inicio = p_medio2 + 1
        else:
            inicio = p_medio1 + 1
            fin = p_medio2 - 1

    return -1

cantidad = int(input("Ingrese la cantidad de números aleatorios: "))
n_buscar = int(input("Ingrese el número a buscar: "))


l_aleatoria = [random.randint(1, 10000000) for _ in range(cantidad)]
l_aleatoria.sort()

print("La lista ordenada es:", l_aleatoria)


i_tiempo = time.time()
resultado = busqueda_ternaria(l_aleatoria, n_buscar)
f_tiempo = time.time()



if resultado != -1:
    print(f"El número {n_buscar} se encuentra en la posición {resultado}.")
else:
    print(f"El número {n_buscar} no se encuentra en la lista.")

e_tiempo= f_tiempo - i_tiempo
print(f"El tiempo de ejecución fue de {e_tiempo} segundos.")
