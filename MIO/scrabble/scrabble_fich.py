#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def leer_fichero_palabras(filename):
    """Devuelve una LISTA de cadenas con las palabras que contiene el fichero indicado.
    Todas están en MINÚSCULAS"""
    wordlist = []
    try:
        with open (filename, 'r') as file_read:
            for item in file_read:
                item=item.strip('\n')
                wordlist.append(item)

        # ... COMPLETAR!

    except:
        print("Error leyendo fichero:", filename)
        wordlist = []  # por si acaso, no devolver nada

    return wordlist

print(leer_fichero_palabras("sowpods.txt"))