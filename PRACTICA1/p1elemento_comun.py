import random
import time

def g_arreglo(tam):
    arreglo = []
    for i in range(tam):
        numero = random.randint(1,val_max)
        arreglo.append(numero)
    return arreglo

def i_arreglo(arreglo):
    texto = ", ".join(str(x) for x in arreglo)
    print(texto)


def b_numeros_iguales(arreglo1, arreglo2):
    return list(set(arreglo1) & set(arreglo2))

val_max = int(input("Ingrese el valor máximo para los números aleatorios: "))

print("-" * 50)

p_arreglo = g_arreglo(val_max)
print("El primer arreglo es:")
i_arreglo(p_arreglo)

def o_arreglo(arreglo):
    arreglo.sort()
    return arreglo

arreglo_ordenado = o_arreglo(p_arreglo)
print("El primer arreglo ordenado es:")
i_arreglo(arreglo_ordenado)

print("-" * 50)

s_arreglo = g_arreglo(val_max)
print("El segundo arreglo es:")
i_arreglo(s_arreglo)


s_arreglo_ordenado = o_arreglo(s_arreglo)
print("El segundo arreglo ordenado es:")
i_arreglo(s_arreglo_ordenado)

print("-" * 50)

n_iguales = b_numeros_iguales(p_arreglo, s_arreglo)

if len(n_iguales) > 0:
    print(f"\nLos números {n_iguales} fueron encontrados iguales.")
else:
    print("\nNo se encontraron números iguales en ambos arreglos.")


t_inicio = time.time()
arreglo = g_arreglo(val_max)
s_arreglo = g_arreglo(val_max)
arreglo_ordenado = o_arreglo(arreglo)
t_fin = time.time()
t_duracion = t_fin - t_inicio
print("-" * 50)
print(f"El tiempo de ejecución fue de {t_duracion} segundos")