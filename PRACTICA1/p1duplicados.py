import random
import time

# Función para generar un arreglo de números aleatorios
def g_arreglo(tam):
    arreglo = []  # Inicializa una lista vacía para almacenar los números aleatorios
    for i in range(tam):
        numero = random.randint(1,val_max) # Genera un número aleatorio entre 1 y val_max
        arreglo.append(numero) # Agrega el número generado al arreglo
    return arreglo

# Función para imprimir un arreglo
def i_arreglo(arreglo):
    texto = ", ".join(str(x) for x in arreglo) # Convierte cada número del arreglo a una cadena de texto y los une con comas
    print(texto)

# Función de búsqueda secuencial en un arreglo
def b_secuencial(arreglo, elemento):
    for i, x in enumerate(arreglo): # Recorre el arreglo con índice (i) y valor (x)
        if x == elemento: # Si el elemento es encontrado
            return i
    return -1

# Función para buscar elementos duplicados en un arreglo
def b_duplicados(arreglo):
    e_unicos = set()  # Inicializa un conjunto para almacenar elementos únicos
    duplicados = set() # Inicializa un conjunto para almacenar elementos duplicados

    for elemento in arreglo: # Recorre cada elemento en el arreglo
        if elemento in e_unicos:  # Si el elemento ya está en el conjunto de únicos
            duplicados.add(elemento) # Agrega al conjunto de duplicados
        else:
            e_unicos.add(elemento) # Agrega al conjunto de únicos

    return list(duplicados)

# Solicita al usuario el valor máximo para los números aleatorios
val_max = int(input("Ingrese el máximo valor de números aleatorios: "))

# Genera un arreglo de números aleatorios
arreglo = g_arreglo(val_max)
print("EL arreglo original es:")
i_arreglo(arreglo) # Imprime el arreglo original

# Función para ordenar un arreglo
def o_arreglo(arreglo):
    arreglo.sort() # Ordena el arreglo en orden ascendente
    return arreglo

# Ordena el arreglo
arreglo_ordenado = o_arreglo(arreglo)
print("El arreglo ordenado es:")
i_arreglo(arreglo_ordenado)

# Busca elementos duplicados en el arreglo
duplicados = b_duplicados(arreglo)
if len(duplicados) > 0: # Si hay elementos duplicados
    print(f"\nLos números o número {duplicados} se encontraron duplicados")
else: # Si no hay elementos duplicados
    print("\nNo hubo elementos duplicados.")

# Mide el tiempo de ejecución de la generación del arreglo
t_inicio = time.time()  # Marca el tiempo de inicio
arreglo = g_arreglo(val_max)  # Genera un nuevo arreglo de números aleatorios
t_fin = time.time()  # Marca el tiempo de finalización
t_duracion = t_fin - t_inicio # Calcula la duración total de la operación
print(f"El tiempo de ejecución fue de {t_duracion} segundos") 
