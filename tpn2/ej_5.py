class persona:
    def __init__(self):
            self.nombre=""
            self.edad= 0

    def cargar_datos(self):
        self.nombre = (input('Ingrese su nombre\n>>>'))
        self.edad=int(input('Ingrese su edad\n>>>'))
   


class empleado(persona):
    def __init__(self):
        super().__init__()
        self.sueldo = 0

    def cargar_datos(self):
        super().cargar_datos()

        self.sueldo = float(input("Ingrese el sueldo \n>>>"))

    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print("Usted debe pagar impuestos")
        else:
            print("Usted no debe pagar impuestos, su sueldo no es mayor a 3000")
persona_fin=persona()
empleado_fin=empleado()
empleado_fin.cargar_datos()
empleado_fin.pagar_impuestos()