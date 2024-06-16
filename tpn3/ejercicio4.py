while True:
    try:
        n2 = float(input("Ingrese el segundo número \n>>>"))
        n1 = float(input("Ingrese su Primer número \n>>>"))
        resultado = n1 / n2
        print("El resultado de la división es: ", resultado)
        break
    except ValueError:
        print("Error usted ingreso un dato no numerico")
    except ZeroDivisionError:
        print("Error no se puede dividir por 0")