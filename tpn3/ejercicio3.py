months_year = (
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
try:
    nmes = int(input("Ingrese el número de mes \n>>>"))
    nom_mes = months_year[nmes - 1]
    print("El mes correspondiente es: ", nom_mes)
except ValueError:
    print("Error usted ingreso un dato no numerico")
except IndexError:
    print("Error, usted ingreso un numero fuera del rango de 1 a 12")