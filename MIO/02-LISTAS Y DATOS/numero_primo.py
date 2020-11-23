n=int(input("Introduce un número: "))
limite=n-1
deno=2
resto=1
while deno<limite:
    resto = n % deno 
    if resto ==0:
        print (f"no es primo {n}")
        break
    deno+=1


if resto != 0:
    print(f"{n} es primo")    


