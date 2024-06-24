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

def bus_secuencial(arreglo, elemento):
    for i, x in enumerate(arreglo): 
        if x == elemento:
            return i 
    return -1 

val_max = int(input("Ingrese el valor máximo para los números aleatorios: "))
elemento = int(input("Ingrese el elemento a buscar: "))

arreglo = g_arreglo(val_max)
print("El arreglo original es:")
i_arreglo(arreglo) 

def o_arreglo(arreglo):
    arreglo.sort()
    return arreglo

arreglo_ordenado = o_arreglo(arreglo)
print("El arreglo ordenado es:")
i_arreglo(arreglo_ordenado)

indice = bus_secuencial(arreglo, elemento)
if indice != -1:
    print(f"El elemento {elemento} esta en el arreglo")
else: 
    print(f"El elemento {elemento} no esta en el arreglo")


t_inicio = time.time() 
t_final = time.time() 
t_duracion = t_final - t_inicio 
print(f"El tiempo de ejecución fue de {t_duracion} segundos")


