import random
import time

# Función para generar un arreglo de números aleatorios
def g_arreglo(tam):
    arreglo = []
    for i in range(tam):
        numero = random.randint(1,val_max) # Genera un número aleatorio entre 1 y val_max
        arreglo.append(numero)  # Agrega el número generado al arreglo
    return arreglo

# Función para imprimir un arreglo
def i_arreglo(arreglo):
    texto = ", ".join(str(x) for x in arreglo)  # Convierte cada número del arreglo a una cadena de texto y los une con comas
    print(texto)

# Función de búsqueda secuencial en un arreglo
def b_secuencial(arreglo, elemento):
    for i, x in enumerate(arreglo): # Recorre el arreglo con índice (i) y valor (x)
        if x == elemento:
            return i  # Retorna el índice del elemento
    return -1 # Retorna -1 si el elemento no se encuentra

# Solicita al usuario el valor máximo para los números aleatorios
val_max = int(input("Ingrese el máximo valor para los números aleatorios: "))
# Solicita al usuario el número que se desea buscar en los arreglos
elemento = int(input("Ingrese el número que se busca: "))

print("-" * 50)

# Genera el primer arreglo de números aleatorios
p_arreglo = g_arreglo(val_max)
print("El primero arreglo es:")
i_arreglo(p_arreglo) # Imprime el primer arreglo

# Función para ordenar un arreglo
def o_arreglo(arreglo):
    arreglo.sort() # Ordena el arreglo en lugar
    return arreglo # Retorna el arreglo ordenado

# Ordena el primer arreglo
arreglo_ordenado = o_arreglo(p_arreglo)
print("El primer arreglo ordenado:")
i_arreglo(arreglo_ordenado) # Imprime el primer arreglo ordenado

# Busca el elemento en el primer arreglo original
indice = b_secuencial(p_arreglo, elemento)
if indice != -1:  # Si el elemento fue encontrado
    print(f"El elemento {elemento} se encontró en el arreglo")
else: # Si el elemento no fue encontrado
    print(f"El elemento {elemento} no se encontró en el arreglo")

print("-" * 50)

# Genera el segundo arreglo de números aleatorios
s_arreglo = g_arreglo(val_max)
print("El segundo arreglo es:")
i_arreglo(s_arreglo)

# Ordena el segundo arreglo (redefiniendo la función para que tome 's_arreglo')
def o_arreglo(s_arreglo):
    s_arreglo.sort() # Ordena el arreglo en lugar
    return s_arreglo

# Ordena el segundo arreglo
arreglo_ordenado = o_arreglo(s_arreglo)
print("El segundo arreglo queda ordenado:")
i_arreglo(arreglo_ordenado) # Imprime el segundo arreglo ordenado

# Busca el elemento en el segundo arreglo original
indice = b_secuencial(s_arreglo, elemento)
if indice != -1: # Si el elemento fue encontrado
    print(f"El número {elemento} se encontró en el arreglo")
else: # Si el elemento no fue encontrado
    print(f"El número {elemento} no se encontró en el arreglo")

# Mide el tiempo de ejecución de ciertas operaciones
t_inicio = time.time() # Marca el tiempo de inicio
p_arreglo = g_arreglo(val_max) # Genera un nuevo primer arreglo
s_arreglo = g_arreglo(val_max) # Genera un nuevo segundo arreglo
b_secuencial(p_arreglo, elemento) # Realiza una búsqueda secuencial en el nuevo primer arreglo
arreglo_ordenado = o_arreglo(p_arreglo) # Ordena el nuevo primer arreglo
b_secuencial(arreglo_ordenado, elemento) # Realiza una búsqueda secuencial en el primer arreglo ordenado
t_final = time.time() # Marca el tiempo de finalización
t_duracion = t_final - t_inicio # Calcula la duración total de las operaciones
print("-" * 50)
print(f"El tiempo de ejecución fue de {t_duracion} segundos")
