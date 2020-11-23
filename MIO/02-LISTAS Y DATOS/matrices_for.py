#mostrar matrices en pantalla (cada sublista dentro de una lista genera una fila en la matriz)
m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[7,8],[4,5],[1,2]]
#m3=[[7,9],[1,2],[89,56]]
# print("La matriz 1 es: ")
# for i in m1:
#     print(i)
# print("La matriz 2 es: ")
# for i in m2:
#     print(i)
# print("La matriz 3 es: ")
# for i in m3:
#     print(i)
#Comprobar filas y columnas
# if len(m1)==len(m2[1]):
#     print("Las matrices son compatibles para multiplicar")
# else:
#      print("Las matrices NO son compatibles para multiplicar")   

#hacer la multiplicación

a=len(m1[0])
b=len(m2)
b2=len(m2[0])


m3 = []
for i in range(a):
    x = []
    for j in range(b2):
        x.append(0)
    m3.append(x)

r=0
i=0
k=0 #cambio en m2
j=0 #cambio en m1

while k<b2:
    while i<a:
        x=m1[j][i]
        y=m2[i][k]
        r=r+(x*y)
        i=i+1
    m3[0][k]=r
    r=0
    i=0
    k+=1
print(m3)

        
    
       
     
#mostrar el resultado