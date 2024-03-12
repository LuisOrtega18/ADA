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

def b_secuencial(arreglo, elemento):
    for i, x in enumerate(arreglo):
        if x == elemento:
            return i
    return -1

val_max = int(input("Ingrese el máximo valor para los números aleatorios: "))
elemento = int(input("Ingrese el número que se busca: "))

print("-" * 50)

p_arreglo = g_arreglo(val_max)
print("El primero arreglo es:")
i_arreglo(p_arreglo)

def o_arreglo(arreglo):
    arreglo.sort()
    return arreglo

arreglo_ordenado = o_arreglo(p_arreglo)
print("El primer arreglo ordenado:")
i_arreglo(arreglo_ordenado)

indice = b_secuencial(p_arreglo, elemento)
if indice != -1:
    print(f"El elemento {elemento} se encontró en el arreglo")
else:
    print(f"El elemento {elemento} no se encontró en el arreglo")

print("-" * 50)

s_arreglo = g_arreglo(val_max)
print("El segundo arreglo es:")
i_arreglo(s_arreglo)

def o_arreglo(s_arreglo):
    s_arreglo.sort()
    return s_arreglo

arreglo_ordenado = o_arreglo(s_arreglo)
print("El segundo arreglo queda ordenado:")
i_arreglo(arreglo_ordenado)

indice = b_secuencial(s_arreglo, elemento)
if indice != -1:
    print(f"El número {elemento} se encontró en el arreglo")
else:
    print(f"El número {elemento} no se encontró en el arreglo")


t_inicio = time.time()
p_arreglo = g_arreglo(val_max)
s_arreglo = g_arreglo(val_max)
b_secuencial(p_arreglo, elemento)
arreglo_ordenado = o_arreglo(p_arreglo)
b_secuencial(arreglo_ordenado, elemento)
t_final = time.time()
t_duracion = t_final - t_inicio
print("-" * 50)
print(f"El tiempo de ejecución fue de {t_duracion} segundos")