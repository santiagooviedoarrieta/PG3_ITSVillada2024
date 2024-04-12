try:
    with open("texto_almacenado.txt", "w") as archivo:
        archivo.write(123)

except TypeError:
    print("Error, usted no ingreso texto")
