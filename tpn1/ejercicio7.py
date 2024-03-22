num = input("Ingrese su numero\n>>>")
def Esstep(num):
    if len(num) / float(2) != len(num) / 2:
        return False
    for i in range(0, len(num), 2):
        if not (int(num[i:i + 2][0]) + 1 == int(num[i:i + 2][1]) or int(num[i:i + 2][0]) - 1 == int(num[i:i + 2][1])):
            return False
    return True
if Esstep(num):
    print ("Es un número STEP")
else :
    print ("No es un número STEP")