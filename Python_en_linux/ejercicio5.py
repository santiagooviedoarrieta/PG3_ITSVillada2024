def palabra_palindromo():
  igual, auxiliar = 0, 0
  palabra = input("Ingrese la palabra que desea saber si es palindroma\n>>> ")
  for i in reversed(range(0, len(palabra))):
    if palabra[i].lower() == palabra[auxiliar].lower():
      igual += 1
      auxiliar += 1
  if len(palabra) == igual:
      print("La palabra ingresada es palindromo!")
  else:
      print("La palabra ingresada no es palindromo!")
palabra_palindromo()