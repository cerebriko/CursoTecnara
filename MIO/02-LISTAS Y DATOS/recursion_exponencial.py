def exponencial(base,n):
    if n < 0 :
        return None
    elif n==0:
        return 1
    else:
        a= base * exponencial(base, n-1)
        return a


x=exponencial(2,3)
y = print(x)
print(y)


# #####################################################################
def exponencial(base,n):
    a = 1
    while n > 0 :
        n = n -1
        a= base * a
    return a


x=exponencial(2,3)
print(x)


# ###################################################################
def exponencial(base,n):
    while n > 0 :
        a=base * exponencial(base, n-1)
        return a


x=exponencial(2,3)
print(x)