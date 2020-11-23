#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def read_flashcard_file(filename, enc="utf-8"):
    """Devuelve un diccionario clave-valor en el que las claves son las preguntas, y
    los valores las respuestas, tal como se han leído de un fichero .csv"""

    question_dict = {}
    with open('filename', 'r') as file_read:
        for line in file_read:  # NOTA: mejor que file_read.readlines():
            print(line.split())

    # COMPLETAR... !
    return question_dict


# Nombre del fichero que se usará
# flashcard_filename = "examples/flashcards_capitales_latin-1.csv"  # alternativa!
flashcard_filename = "M3/m9/flashcards_capitales.csv"  # default value

# Leer el fichero en cuestión
print("Flash card file to use:", flashcard_filename)
question_dict = read_flashcard_file(flashcard_filename)
questions = list(question_dict.keys())