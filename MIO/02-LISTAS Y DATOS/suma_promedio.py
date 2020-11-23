x=0
y=-1
s=0
cont=True

while cont == True:
    x = input("Introduce numeros y usa el 0 para indicar que no añades mas numeros:")
    a = float(x)
    cont=bool(a)
    s = s + a
    y=y+1

cont=False
print(f"la suma de los números añadidos es {s}")
prom = s / y
print(f"el promedio de los números añadidos es {prom}")