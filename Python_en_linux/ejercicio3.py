def rectangulo():
    ancho = int(input("Anchura del rectángulo\n>>> "))
    alto = int(input("Altura del rectángulo\n>>> "))
    caracter = input("Ingrese el caracter a utilizar\n>>>")
    for i in range(alto):
        for j in range(ancho):
            print(f' {caracter} ' , end ="" )
        print()
rectangulo()
