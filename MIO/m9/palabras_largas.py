
def palabra_lista(lista):
    longitud=""
    for i in lista:
        if len(lista[i])>len(longitud):
            longitud=lista(i)
    return longitud
def palabra_largas(fichero):
    mayor=""
    with open(fichero,"r") as f_read:
        for linea in f_read:
            palabra=linea.split(" " or ",")
            longitud=""
            for i in range(len(palabra)):
                if len(palabra[i])>len(longitud):
                    longitud=palabra[i]
            if len(longitud)>len(mayor):
                mayor=longitud
                
        print("La palabra larga es: ",mayor)
#################################################################
def num_lineas(fichero):
    with open(fichero,"r") as f_read:
        lineas=0
        for linea in f_read:
            lineas+=1
        print("El fichero tiene: ",lineas," lineas")
#################################################################
def pot_write(fichero):
    i=0
    while i!=50:
        a=2**i
        i+=1
        with open(fichero,'a') as f_write:
            f_write.write(str(a)+"\n")
########################################################
def tiempo_transcurrido(day,month,year):
    import datetime
    today=datetime.date.today()
    print(today)
    past=datetime.date(year, month,day)
    diferencia=abs(today-past)
    print("Han pasado ",diferencia.days*24, "horas")

import sys

print(sys.argv)
print(type(sys.argv))
###########################################
sys.argv = ["yo", "2020", "11", "25"]
###########################################

if len(sys.argv) == 4:
    anio = int(sys.argv[1])
    mes = int(sys.argv[2])
    dia = int(sys.argv[3])
else:
    print("ERROR: este programa necesita 3 argumentos: año, mes, dia")
    exit(1)
 
tiempo_transcurrido(dia, mes, anio)

palabra_largas("foo.txt")
num_lineas("foo.txt")
pot_write("potencias.txt")
tiempo_transcurrido(dia,mes,anio)