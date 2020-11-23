#definir variables
x=1
n=0
ex=0
#sume es el acumulador de ex
sume=0
#factorial es el denominador en cada momento del bucle
factorial=1

while n<10:
    factorial=n*factorial
    #esta condicion contempla que el denominador(factorial) inicial tiene que ser 1 
    #Gracias por la info Pachi
    if factorial == 0:
        factorial = 1
    ex=(x/factorial)
    sume=ex+sume
    n=n+1
    print(sume)


print(f"el numero e es igual a:{sume}")




