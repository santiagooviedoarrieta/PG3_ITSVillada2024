lista = [8, 12, 9, 45]

try:
    elemento_buscado = int(input("Ingrese el elemento que desea buscar: "))

    try:
        indice = lista.index(elemento_buscado)
        print(f"El elemento {elemento_buscado} se encuentra en el índice {indice}.")
    except ValueError:
        print(f"El elemento {elemento_buscado} no se encuentra en la lista.")
except ValueError:
    print("Por favor, ingrese un valor numérico válido.")