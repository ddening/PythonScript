# Seminar Uebung 05 (Flood Fill)                         
#  _____________________________________
#                                       
#          /               ,            
#  ----__-/----__----__--------__----__-
#    /   /   /___) /   ) /   /   ) /   )
#  _(___/___(___ _/___/_/___/___/_(___/_
#                                    /  
#                                (_ /   
# Quellen:
# https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python

import time
import os
import colorama
import random

# GLOBALE DEFINITION 
RED = '\033[31m'        # mode 31 = red forground
RESET = '\033[0m'       # mode 0  = reset

# ==== INFO ====
MAX_TIME = 0.01         # Verlangsame die Ausgabe im cmd Fenster
VISUAL = 1              # Zur visuellen Darstellung aller Einzelschritte auf <1> setzen (lange Ausfuehrzeit)
COLOR = 1            # Fuellung der Felder gefaerbt. Setze <0> um Ausfuehrzeit gegebenenfalls zu verkuerzen

def printField(field):
    ''' Docstring'''

    for i in range(0, len(field)):
        _string = ""
        for j in range(0, len(field[i])):
            _string = _string + field[i][j]
        print(_string)


def doublePrint(field, _field):
    _string0 = ""
    _string1 = ""
    _string = ""

    for i in range(0, len(field)):
        _string0 = ""
        _string1 = ""
        for j in range(0, len(field[i])):
            _string0 = _string0 + field[i][j]
            _string1 = _string1 + _field[i][j]
        _string = _string0 + "   " + _string1
        print(_string)


def fillFlood(field, startPoint, emptyMarker, filledMarker):
    ''' Docstring'''

    x = startPoint[0]
    y = startPoint[1]

    if x < 0 or y < 0 or x >= len(field) or y >= len(field[x]) :
        return

    if field[x][y] != emptyMarker:
        return
  
    if COLOR:
        field[x][y] = RED + filledMarker + RESET
    else:
        field[x][y] = filledMarker

    if VISUAL:
        time.sleep(MAX_TIME)
        os.system('cls')
        printField(field)

    # Rekursive Aufrufe fuer alle 4 Positionen
    fillFlood(field, (x+1, y), emptyMarker, filledMarker)
    fillFlood(field, (x, y-1), emptyMarker, filledMarker)
    fillFlood(field, (x-1, y), emptyMarker, filledMarker)
    fillFlood(field, (x, y+1), emptyMarker, filledMarker)
    

    return field

def searchMaxLine(filename):
    ''' Docstring'''

    _max = []

    f = open(filename, "r")
    line = f.readline()

    while line:
        # Erzeuge leeres Spielfeld
        _max.append(len(line))
        line = f.readline()

    f.close() 

    return max(_max)
    
def convertFileToField(filename, emptyMarker, filledMarker):
    ''' Docstring'''

    field = []

    f = open(filename, "r")
    line = f.readline()

    _maxLine = searchMaxLine(filename)

    while line:
        # Erzeuge leeres Spielfeld
        field.append([emptyMarker] * (_maxLine - 1))
        line = f.readline()

    f.close() 

    # F�lle Feld
    f = open(filename, "r")
    line = f.readline()
    
    counter = 0
    while line:
        for j in range (0, len(line) - 1):
            field[counter][j] = line[j]
        line = f.readline()
        counter = counter + 1

    return field

def randomStartPoint(field):
    ''' Docstring'''

    check = -1

    while check is -1 :
        x = random.randint(0, len(field) - 1)
        y = random.randint(0, len(field[x]) - 1)

        if field[x][y] == " ":
            check = 0
 
    return (x, y)
