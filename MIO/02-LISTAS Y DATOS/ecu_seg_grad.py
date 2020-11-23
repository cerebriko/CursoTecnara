a = float(input("Introduce el valor a: ")) 
b = float (input("Introduce el valor b: "))
c = float (input("Introduce el valor c: "))
raiz=(b**2)-(4*a*c)

if raiz < 0:
    print("el resultado no es un numero NO real")

else:
    xpos = ((-b+ (raiz**0.5))/(2*a))
    xneg = ((-b-(raiz**0.5))/(2*a))
    print(f"el primer resultado es: {xpos}")
    print(f"el segundo resultado es: {xneg}")