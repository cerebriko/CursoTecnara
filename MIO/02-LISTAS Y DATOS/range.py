inicio=int(input("Introduce el valor inicial:"))
fin=int(input("Introduce el valor final:"))
salto=int(input("Introduce el valor de salto:"))
lista=[]

while inicio<fin:
    lista.append(inicio)
    inicio=inicio+salto

print(lista)

    