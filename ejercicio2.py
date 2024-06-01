lista = [1, 20, 15, 10]
try:
    print(lista[10])
except IndexError:
    print("El índice no existe")