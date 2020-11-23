def potencia(base, inicio=1, fin=10):
    while inicio < fin:
        resul=base**inicio
        yield resul
        inicio=inicio+1

print(list(potencia(3,1,50)))