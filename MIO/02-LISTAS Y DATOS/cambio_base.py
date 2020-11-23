# Slocitar numero a calcular y la base.
numero=int(input("Introduce un numero (base 10) para cabiar su base: "))
base=int(input("Introduce la base a la que queires camiar el numero anterior entre 2 y 9: "))
cadena=""

#sucesion de divisiones para ir calculando los restos y resultados
while numero>base:
    resultado=numero//base
    resto=numero % base
    numero=resultado
    cadena=str(resto)+cadena
    
      
if resultado == base:
    resto=numero%base
    resultado=numero//base
    print=(str(resultado)+str(resto)+(cadena)  )  
elif numero<base:
print=(str(numero) + (cadena) )  



        