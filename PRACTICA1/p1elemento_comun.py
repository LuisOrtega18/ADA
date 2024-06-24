import random
import time

# Función para generar un arreglo de números aleatorios
def g_arreglo(tam):
    arreglo = []
    for i in range(tam):
        numero = random.randint(1,val_max) # Genera un número aleatorio entre 1 y val_max
        arreglo.append(numero) # Agrega el número generado al arreglo
    return arreglo

# Función para imprimir un arreglo
def i_arreglo(arreglo):
    texto = ", ".join(str(x) for x in arreglo) # Convierte cada número del arreglo a una cadena de texto y los une con comas
    print(texto)

# Función para encontrar números iguales en dos arreglos
def b_numeros_iguales(arreglo1, arreglo2):
    return list(set(arreglo1) & set(arreglo2)) # Convierte ambos arreglos a conjuntos y retorna la intersección convertida a lista

# Solicita al usuario el valor máximo para los números aleatorios
val_max = int(input("Ingrese el valor máximo para los números aleatorios: "))

print("-" * 50)

# Genera el primer arreglo de números aleatorios
p_arreglo = g_arreglo(val_max)
print("El primer arreglo es:")
i_arreglo(p_arreglo)

# Función para ordenar un arreglo
def o_arreglo(arreglo):
    arreglo.sort()  # Ordena el arreglo en orden ascendente
    return arreglo

# Ordena el primer arreglo
arreglo_ordenado = o_arreglo(p_arreglo)
print("El primer arreglo ordenado es:")
i_arreglo(arreglo_ordenado)

print("-" * 50)

# Genera el segundo arreglo de números aleatorios
s_arreglo = g_arreglo(val_max)
print("El segundo arreglo es:")
i_arreglo(s_arreglo)

# Ordena el segundo arreglo
s_arreglo_ordenado = o_arreglo(s_arreglo)
print("El segundo arreglo ordenado es:")
i_arreglo(s_arreglo_ordenado)

print("-" * 50)

# Encuentra los números iguales en ambos arreglos
n_iguales = b_numeros_iguales(p_arreglo, s_arreglo)

# Imprime los números iguales si se encontraron
if len(n_iguales) > 0:
    print(f"\nLos números {n_iguales} fueron encontrados iguales.")
else:
    print("\nNo se encontraron números iguales en ambos arreglos.")

# Mide el tiempo de ejecución de ciertas operaciones
t_inicio = time.time() # Marca el tiempo de inicio
arreglo = g_arreglo(val_max) # Genera un nuevo primer arreglo
s_arreglo = g_arreglo(val_max) # Genera un nuevo segundo arreglo
arreglo_ordenado = o_arreglo(arreglo) # Ordena el nuevo primer arreglo
t_fin = time.time() # Marca el tiempo de finalización
t_duracion = t_fin - t_inicio # Calcula la duración total de las operaciones
print("-" * 50)
print(f"El tiempo de ejecución fue de {t_duracion} segundos")
