numeros=input("Introduce números: ")
ln=[]

for e in numeros.split():
    ln.append(float(e))
lon= len(ln)
print("la suma es: ", sum(ln))
print("la media es: ",sum(ln)/lon)
print("el numero minimo es: ",min(ln))
print("el numero maximo es: ",max(ln))

lo=ln
lo.sort()
print (lo)
if lon % 2 == 1:
     print("Mediana: ", lo[lon//2])
else:
    temp=(lo[lon//2-1]+ lo[lon//2])/2
    print("Mediana: ", temp)