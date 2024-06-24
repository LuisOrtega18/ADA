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
    texto = ", ".join(str(x) for x in arreglo)  # Convierte cada número del arreglo a una cadena de texto y los une con comas
    print(texto)

# Función de búsqueda secuencial en un arreglo
def bus_secuencial(arreglo, elemento):
    for i, x in enumerate(arreglo): # Recorre el arreglo con índice (i) y valor (x)
        if x == elemento:
            return i # Retorna el índice del elemento
    return -1 # Retorna -1 si el elemento no se encuentra

# Solicita al usuario el valor máximo para los números aleatorios
val_max = int(input("Ingrese el valor máximo para los números aleatorios: "))
# Solicita al usuario el número que se desea buscar en los arreglos
elemento = int(input("Ingrese el elemento a buscar: "))

# Genera un arreglo de números aleatorios
arreglo = g_arreglo(val_max)
print("El arreglo original es:")
i_arreglo(arreglo)  # Imprime el arreglo

# Función para ordenar un arreglo
def o_arreglo(arreglo):
    arreglo.sort() # Ordena el arreglo en orden ascendente
    return arreglo

# Función para ordenar un arreglo
arreglo_ordenado = o_arreglo(arreglo)
print("El arreglo ordenado es:")
i_arreglo(arreglo_ordenado) #imprime el arreglo ordenado

# Busca el elemento en el arreglo original
indice = bus_secuencial(arreglo, elemento)
if indice != -1: # Si el elemento fue encontrado
    print(f"El elemento {elemento} esta en el arreglo")
else: # Si el elemento no fue encontrado
    print(f"El elemento {elemento} no esta en el arreglo")


t_inicio = time.time()  # Marca el tiempo de inicio
arreglo = g_arreglo(val_max) # Genera un nuevo arreglo
t_final = time.time() # Marca el tiempo de finalización
t_duracion = t_final - t_inicio # Calcula la duración total de las operaciones
print(f"El tiempo de ejecución fue de {t_duracion} segundos")


