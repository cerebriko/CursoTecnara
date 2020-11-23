def print_all_after_delete_first(l):
    del l[0]
    print (l)

def print_delete_first(l):
    a=l.copy()
    del a[0]
    print (a)
    
lista=[1,2,3,4,5,6]
lista2=[1,2,3,4,5,6]
print(lista)
print_all_after_delete_first(lista)
print_delete_first(lista2)
print(lista2)