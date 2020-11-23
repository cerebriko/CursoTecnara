#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio / demo "recorrer diccionarios" del Módulo 4

dicc1 = {
    "Naranjas": (25, "Paco"),
    "Manzanas": (0,"Maria"),
    "Fresas": (240,"Juan"),
    "Kiwis": (15.33333,"Juan"),
    "Plátanos": (5.5,"Juan"),
}

dicc2 = {
    "Naranjas": (10.5,"Paco"),
    "Manzanas": (55,"Maria"),
    "Fresas": (0.0,"Juan"),
    "Kiwis": (50,"Paco"),
    "Plátanos": (5.5,"Maria"),
}

fruits = dicc2
frutas = dicc1
suma=0
for fruta1, valor in frutas.items():  # si no indico nada, es como keys()
    suma=valor[0]
    for fruta, valor1 in frutas.items():
        if valor[1]==valor1[1]:
            suma=suma+valor1[0]
    for fruta, valor2 in fruits.items():
        if valor[1]==valor2[1]:
            suma=suma+valor2[0]
        
    print(valor[1],"ha traido ",suma," kilos")
    suma=0
# for fruta1 in frutas.keys():  # si no indico nada, es como keys()
#     for fruta2 in range(len(fruits)):
#         if frutas[fruta1][1] == fruits[fruta1][1]:
#             print("El proveedor", fruits[fruta1][1], "ha traido", frutas[fruta1][0] + fruits[fruta1][0], "kg de",fruta1)
#             break
#         else:
#             print("El proveedor", frutas[fruta1][1], "ha traido", frutas[fruta1][0] , "kg de",fruta1)
#             print("El proveedor", fruits[fruta1][1], "ha traido", fruits[fruta1][0] , "kg de",fruta1)
#             break


















# for fruta in frutas.keys():  # si no indico nada, es como keys()
#     # MODIFICAR para que cumpla lo que se pide:
#     if frutas[fruta][0] > 0:
#         print("La cantidad de:", fruta, "es", frutas[fruta][0])




# for fruta in fruits.keys():  # si no indico nada, es como keys()
#     # MODIFICAR para que cumpla lo que se pide:
#     if (type (fruits[fruta][0]) == int or (type (fruits[fruta][0]) == float :
#         print("La cantidad de:", fruta, "es", fruits[fruta][0])

# print()




# # Alternativa: recorrer los items (tuplas clave-valor)

# for fruta, cantidad in frutas.items():
#     # MODIFICAR para que cumpla lo que se pide:
#     if cantidad > 0:
#         print("La cantidad de:", fruta, "es", cantidad)

# print()


# # Alternativa 2, no recomendable para este caso: sacar los elementos con popitem()
# # No es recomendable simplemente por eficiencia, tenemos que hacer primero una copia
# # porque no sabemos si luego haría falta la lista original de nuevo (probable...)

# copia_frutas = dict(frutas)  # copia
# # copia_frutas = frutas.copy()  # alternativa (mejor) para copia
# while len(copia_frutas) > 0:
#     fruta, cantidad = copia_frutas.popitem()
#     # MODIFICAR para que cumpla lo que se pide:
#     if cantidad > 0:
#         print("La cantidad de:", fruta, "es", cantidad)
