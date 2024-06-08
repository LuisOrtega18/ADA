def simple(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1 # Si no existe índice mágico
