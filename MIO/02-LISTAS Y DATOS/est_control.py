xstr= (input("Dame un número >= 0: "))
x = float(xstr)
if x < 0:
    print('Error')
    x = 0
if x < 0:
    print('Negative changed to zero')
    x = 0
else:
    if x == 0:
        print('Zero')
    elif x == 1 or x < 2.0:
        print('Single')
    elif x == 1:
        print('TEXT NEVER SHOWN')
    else:
        print('More')
print("Continuara...")