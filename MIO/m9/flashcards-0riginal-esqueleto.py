#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def read_flashcard_file(filename, enc="utf-8"):
    """Devuelve un diccionario clave-valor en el que las claves son las preguntas, y
    los valores las respuestas, tal como se han leído de un fichero .csv"""

    question_dict = {}
    with open( filename , 'r') as file_read:
        for line in file_read:  # NOTA: mejor que file_read.readlines():
            line = line.replace("\n", "")
            a=(line.split(","))
            question_dict[a[0]]=a[1]

    # COMPLETAR... !
    return question_dict


# Nombre del fichero que se usará
flashcard_filename = "M3/m9/flashcards_capitales_latin-1.csv"  # alternativa!
#flashcard_filename = "M3/m9/flashcards_capitales.csv"  # default value


# Leer el fichero en cuestión
print("Flash card file to use:", flashcard_filename)
question_dict = read_flashcard_file(flashcard_filename)
questions = list(question_dict.keys())


# Escribir las instrucciones de juego
print("Welcome to the flashcard quizzer.")
print("At any time, type 'quit' to quit.")
print()


while True:
    question = random.choice(questions)
    print("Question: " + question)

    answer = question_dict[question]

    user_input = input("Your guess: ")
    if user_input == "quit":
        print("Thanks for playing! Goodbye.")
        break
    elif user_input == answer:
        print("Correct!!! 🏆")
    else:
        print("Sorry, the answer was: " + answer)
