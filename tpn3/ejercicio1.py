eleccion="si"

try:
        while eleccion ==("si"): 
            n1=(int(input("Ingrese su Primer Numero \n >>>")))
            n2=(int(input("Ingrese su Segundo Numero \n >>>")))
            suma=n1+n2
            print("La suma de sus numeros es: " ,suma)
            eleccion=(input("Desea seguir sumando los numeros (si/no): "))
        else:
            exit()

except ValueError :
     print("Usted no ingreso un numero")

