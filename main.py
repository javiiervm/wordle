import random
import os
from operator import length_hint

# Códigos de escape ANSI
RESET = "\033[0m"  # Restablecer color
BOLD = "\033[1m"  # Negrita
GREEN = "\033[92m"  # Verde
RED = "\033[91m"  # Rojo
YELLOW = "\033[93m"  # Amarillo

# Lista de palabras
diccionario = "diccionario.txt"

# FUNCIÓN PARA IMPRIMIR EL TÍTULO Y LA EXPLICACIÓN
def printMenu():
    print("JUEGO WORDLE")
    print(f"\n¿En qué consiste este juego?\n{GREEN} > Una letra verde significa que es correcta y está en el lugar correcto{RESET}"
        f"\n{YELLOW} > Una letra amarilla significa que es correcta pero está en el lugar incorrecto{RESET}"
        f"\n{RED} > Una letra roja significa que no está en la palabra{RESET}"
        f"\n ¡Recuerda que las palabras solo pueden tener {BOLD}5 letras{RESET}!\n")

# FUNCIÓN PARA GENERAR LA PALABRA ALEATORIA
def generateRandomWord(lista, word_length=5):
    with open(lista, encoding="utf-8") as f:
        words = [word.strip().lower() for word in f if len(word.strip()) == word_length]
    for i in range (0, len(words)):
        words[i] = words[i].replace("á", "a")
        words[i] = words[i].replace("é", "e")
        words[i] = words[i].replace("í", "i")
        words[i] = words[i].replace("ó", "o")
        words[i] = words[i].replace("ú", "u")
        words[i] = words[i].replace("ü", "u")
    return words, random.choice(words)

# FUNCIÓN PARA COMPROBAR QUE LA PALABRA ESTÉ EN LA LISTA
def isInList(lista, seleccion):
    for word in lista:
        if word == seleccion:
            return True
    return False

# FUNCIÓN PARA COMPROBAR LA PALABRA INTRODUCIDA POR EL JUGADOR
def wordchecker(realWord, playerWord):
    result = [RED] * len(realWord)
    realWordList = list(realWord)

    # Marcamos las letras correctas en la posición correcta (verdes)
    for i in range(len(realWord)):
        if playerWord[i] == realWord[i]:
            result[i] = GREEN
            realWordList[i] = None  # Marcamos la letra como usada

    # Verificamos letras correctas en posiciones incorrectas (amarillas)
    for i in range(len(realWord)):
        if playerWord[i] in realWordList and result[i] == RED:
            result[i] = YELLOW
            realWordList[realWordList.index(playerWord[i])] = None  # Marcamos la letra como usada

    return result

# FUNCIÓN QUE MANEJA LAS RONDAS DE CADA PALABRA
def game_round(lista, word_length=5):
    words, randomWord = generateRandomWord(lista, word_length=word_length)
    randomWord = randomWord.lower()
    attempt = 0

    while attempt < 6:
        print(f"\nRonda {attempt + 1}/6")
        playerWord = input(">> ").strip().lower()[:word_length]

        if isInList(words, playerWord.lower()):
            resultList = wordchecker(randomWord, playerWord)

            # Mostrar resultado con colores
            for i in range(word_length):
                print(f"{BOLD}{resultList[i]}{playerWord[i].upper()}{RESET}", end=" ")
            print("")

            # Si el jugador acierta, termina el juego
            if playerWord == randomWord:
                print(f"{GREEN}¡Enhorabuena! ¡Has adivinado la palabra!{RESET}\n")
                return True

            attempt = attempt + 1
        else:
            print(f"{RED}La palabra '{playerWord}' no está en el diccionario. Inténtalo de nuevo.{RESET}")

    print(f"{RED}¡Has perdido! La palabra era: {randomWord}{RESET}\n")
    return False

# PROGRAMA PRINCIPAL
words = []

printMenu()
victory = game_round(diccionario)