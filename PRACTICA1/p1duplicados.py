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

def b_duplicados(arreglo):
    e_unicos = set() 
    duplicados = set() 
    for elemento in arreglo:
        if elemento in e_unicos:  
            duplicados.add(elemento) 
        else:
            e_unicos.add(elemento) 

    return list(duplicados)

val_max = int(input("Ingrese el máximo valor de números aleatorios: "))


arreglo = g_arreglo(val_max)
print("EL arreglo original es:")
i_arreglo(arreglo) 

def o_arreglo(arreglo):
    arreglo.sort() 
    return arreglo


arreglo_ordenado = o_arreglo(arreglo)
print("El arreglo ordenado es:")
i_arreglo(arreglo_ordenado)

duplicados = b_duplicados(arreglo)
if len(duplicados) > 0: 
    print(f"\nLos números o número {duplicados} se encontraron duplicados")
else: 
    print("\nNo hubo elementos duplicados.")

t_inicio = time.time() 
t_fin = time.time() 
t_duracion = t_fin - t_inicio
print(f"El tiempo de ejecución fue de {t_duracion} segundos") 
