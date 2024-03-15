
class Alumno:

    def __init__(self):
        self.nombre=(input("Ingrese su nombre:"))
        self.nota=int(input("Ingrese su nota:"))
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Su nota es:" , self.nota)
    def mensaje(self):
        if self.nota>=6:
            print("usted esta aprobado")
        else:
            print("usted no esta aprobado ")

persona1=Alumno()
persona1.mensaje()