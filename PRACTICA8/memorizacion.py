def memorizacion(n):
    memo = [-1] * (n + 1)  # Lista para almacenar los resultados ya calculados

    def ways(step):
        if step == 0:
            return 1
        if step < 0:
            return 0
        
        if memo[step] != -1:
            return memo[step]  # Devolver el resultado ya calculado si está disponible
        
        # Calcular y memorizar el resultado
        memo[step] = ways(step - 1) + ways(step - 2) + ways(step - 3)
        return memo[step]

    return ways(n)

# Pidiendo el número de peldaños al usuario
try:
    n = int(input("Ingresa el número de peldaños de la escalera: "))
    if n < 0:
        print("Por favor, ingresa un número entero no negativo.")
    else:
        print(f"El número de maneras de subir una escalera de {n} peldaños es {memorizacion(n)}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
