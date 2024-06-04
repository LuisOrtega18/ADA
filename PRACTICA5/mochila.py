def m_fraccionaria(items, capacidad):
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    
    valor_total = 0
    for valor, peso in items:
        if capacidad > 0:
            if peso <= capacidad:
                valor_total += valor
                capacidad -= peso
            else:
                valor_total += valor * (capacidad / peso)
                break
        else:
            break
    
    return valor_total


items1 = [(60, 10), (100, 20), (120, 30)]
capacidad1 = 50
print(m_fraccionaria(items1, capacidad1))

# Caso2: Todos los ítems caben en la mochila
items2 = [(30, 5), (40, 8), (50, 5)]
capacidad2 = 20
print(m_fraccionaria(items2, capacidad2))

# Caso3: Solo se puede tomar una fracción de un ítem
items3 = [(500, 30)]
capacidad3 = 10
print(m_fraccionaria(items3, capacidad3))

items4= [[60, 20], [100, 20], [120, 30],[140, 20]]
capacidad4 = 50
print(m_fraccionaria(items4, capacidad4))