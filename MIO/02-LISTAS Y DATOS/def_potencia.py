def potencia(base, inicio=1, fin=10):
    while inicio < fin:
        resul=base**inicio
        yield resul
        inicio=inicio+1
    
for i in potencia(10,1,20):
    print(i)
##################################################################
def pot(base, inicio=1, fin=10):
    while inicio < fin:
        resul=base**inicio
        yield resul
        inicio=inicio+1

print(list(pot(3,1,20)))