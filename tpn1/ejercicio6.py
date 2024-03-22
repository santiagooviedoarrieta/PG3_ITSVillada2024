def es_vocal(letra):
    return letra in "a e i o u"
cadena = input("Ingrese su palabra \n >>>")
cadena_minuscula = cadena.lower()
cantidad_vocales = 0
for letra in cadena_minuscula:
        if letra.isalpha() and not es_consonante(letra):
         cantidad_vocales += 1
       
print(f"En la cadena '{cadena}' hay {cantidad_vocales} vocales")
