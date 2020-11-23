# Obtener la lista de palabras y separarlas
# l=("Dame una lista lista de palabras palabras separadas con espacio ")
l=input("Dame una frase con varias palabras repetidas:")
palabra=""
coincide=""
s=""
for letra in l:
    # print("LETRA:", letra)
    if letra!=" ":
        palabra+=letra
        # print("PALABRA:", palabra)
    if letra ==" ":
        # print (palabra)
        # print (s)
        # print("S:", s)
        if not s.find(palabra) == -1:
            print("SOLUCION:", palabra)
            # coincide+=(palabra+" ")
        s+=palabra
        palabra=""

# print("SOLUCION:", coincide)
