def dibujar_rectangulo(ancho, alto, caracter):
    for i in range(alto):
        print(caracter * ancho)
        #prueba de cambio
def dibujar_triangulo(base, caracter):
    for i in range(1, base + 1):
        print(caracter * i)

def main():
    try:
        opcion = int(input("Seleccione una opción:\n1. Dibujar Rectángulo\n2. Dibujar Triángulo\n"))

        if opcion == 1:
            ancho = int(input("Ingrese el ancho del rectángulo: "))
            alto = int(input("Ingrese el alto del rectángulo: "))
            caracter = input("Ingrese el carácter para el dibujo: ")
            dibujar_rectangulo(ancho, alto, caracter)
        elif opcion == 2:
            base = int(input("Ingrese la base del triángulo: "))
            caracter = input("Ingrese el carácter para el dibujo: ")
            dibujar_triangulo(base, caracter)
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
