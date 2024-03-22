
class Triangulo:
    def __init__(self):
        self.lado1=(input("Ingrese el primer lado \n>>>"))
        self.lado2=(input("Ingrese el segundo lado \n>>>"))
        self.lado3=(input("Ingrese el tercer lado \n>>>"))
    
    def imprimir_v_mayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(f'el lado mayor es el lado 1: {self.lado1}')
        else:
            if self.lado2 > self.lado1 and self.lado2 > self.lado3:
                print(f'el lado mayor es el lado 2: {self.lado2}')
            else:
                if self.lado3 > self.lado2 and self.lado3 > self.lado1:
                    print(f'el lado mayor es el lado 3: {self.lado3}')
                else:
                    print("No tienes un lado mayor")
    def equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print('Sus 3 lados miden lo mismo, tu triangulo es equilatero')
        else:
            print("Tu triangulo no es equilatero, sus lados son diferentes")
triangulo_fin=Triangulo()
triangulo_fin.imprimir_v_mayor()
triangulo_fin.equilatero()