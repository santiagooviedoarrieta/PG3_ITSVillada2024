try:
    n1=(int(input("Ingrese su Primer Numero \n >>>")))
    n2=(int(input("Ingrese su Segundo Numero \n >>>")))
    division=n1/n2
    print("La division entre sus 2 numeros es: ", division)
except ZeroDivisionError:
    print("Error, Usted dividio entre 0")