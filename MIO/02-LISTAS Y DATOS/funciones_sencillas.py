def area_circulo(x):
    a=3.14159265*(x**2)
    return a
    

r=int(input("introduce el valor del radio: "))
x=area_circulo(r)
print(f"el area del circulo es: {x}")

###################################################
def maslarga(l):
    lalarga=""
    for palabra in l:
        if len(palabra)>len(lalarga):
            lalarga=palabra
    return lalarga

lista=["hola", "jorge", "ujdsfuhsediufhasidfhaoeihfod", "ashyd","khdsfuahs"]

print(maslarga(lista))


#############################################

def num_letras(x):
    result=0
    for i in x:
        r=len(i)
        result=result+r
    return result

l=["hola", "mundo"]
        
x = num_letras(l)
print(x)