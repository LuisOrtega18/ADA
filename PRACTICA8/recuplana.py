def recursion_plana(n):
    if n == 0:
        return 1  # Base case: una manera de estar en el inicio sin moverse
    if n < 0:
        return 0  # No hay maneras de llegar a un peldaño negativo
    
    return recursion_plana(n - 1) + recursion_plana(n - 2) + recursion_plana(n - 3)

# Pidiendo el número de peldaños al usuario
try:
    n = int(input("Ingresa el número de peldaños de la escalera: "))
    if n < 0:
        print("Por favor, ingresa un número entero no negativo.")
    else:
        print(f"El número de maneras de subir una escalera de {n} peldaños es {recursion_plana(n)}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
