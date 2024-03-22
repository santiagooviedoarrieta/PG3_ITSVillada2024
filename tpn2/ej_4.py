class Operaciones:
    def __init__(self) :
        self.prim_num=(int(input("Ingresa tu primer número \n>>>")))
        self.seg_num=(int(input("Ingresa tu primer número \n>>>")))
    def suma(self):
        suma=self.prim_num+self.seg_num
        print(f'la suma de tus 2 numeros es: {suma}')
    def resta(self):
        resta=self.prim_num-self.seg_num
        print(f'la resta de tus 2 numeros es: {resta}')
    def multiplicacion(self):
        multiplicacion=self.prim_num*self.seg_num
        print(f'la multiplicacion de tus 2 numeros es: {multiplicacion}')
    def division(self):
        division=self.prim_num/self.seg_num
        print(f'la division de tus 2 numeros es: {division}')

operaciones_fin=Operaciones()
operaciones_fin.suma()
operaciones_fin.resta()
operaciones_fin.multiplicacion()
operaciones_fin.division()