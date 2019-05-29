# Seminar Uebung 05 (Flood Fill)                         
#  _____________________________________
#                                       
#          /               ,            
#  ----__-/----__----__--------__----__-
#    /   /   /___) /   ) /   /   ) /   )
#  _(___/___(___ _/___/_/___/___/_(___/_
#                                    /  
#                                (_ /   

import os
import time
import colorama

 # GLOBALE DEFINITION 
RED = '\033[31m'    # mode 31 = red forground
RESET = '\033[0m'   # mode 0  = reset

# ++++++ INFO ++++++
MAX_TIME = 0.1      # Verlangsame die Ausgabe im cmd Fenster
VISUAL = 0          # Zur visuellen Darstellung aller Einzelschritte auf <1> setzen (lange Ausführzeit)
COLOR = 1           # Füllung der Felder gefärbt. Setze <0> um Ausführzeit gegebenenfalls zu verkürzen

def printField(field):
    ''' Docstring'''

    for i in range(0, len(field)):
        _string = ""
        for j in range(0, len(field[i])):
            _string = _string + field[i][j]
        print(_string)

def fillFlood(field, x, y, emptyMarker, filledMarker):
    ''' Docstring'''

    if x < 0 or y < 0 or x > len(field) - 1 or y > len(field[x]) - 1 :
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
    fillFlood(field, x+1, y, emptyMarker, filledMarker)
    fillFlood(field, x-1, y, emptyMarker, filledMarker)
    fillFlood(field, x, y+1, emptyMarker, filledMarker)
    fillFlood(field, x, y-1, emptyMarker, filledMarker)

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

    while line:
        # Erzeuge leeres Spielfeld
        field.append([emptyMarker] * (searchMaxLine(filename) - 1)) # * (len(line)-1)
        line = f.readline()

    f.close() 

    # Fülle Feld
    f = open(filename, "r")
    line = f.readline()
    
    counter = 0
    while line:
        for j in range (0, len(line) - 1):
            field[counter][j] = line[j]
        line = f.readline()
        counter = counter + 1

    return field

def main():
    ''' Docstring'''

    # +++ INIT +++
    colorama.init()
    
    # Spielfeldgröße
    numberOfColumns = 20    # Spalten
    numberOfRows = 10       # Zeilen

    emptyMarker = " "
    filledMarker = "x"

    # Erzeuge generische Liste
    field = []
    # Enthält fertige gefüllte Felder
    filledFields = []

     # Erzeuge Spielfeld
    for i in range(0, numberOfRows):
        field.append([emptyMarker] * numberOfColumns)

    # Erzeuge Umrandung
    for i in range(0, numberOfRows):
        field[i][3] = filledMarker
        field[i][15] = filledMarker
    # Erzeuge Umrandung
    for i in range(0, numberOfColumns):
        field[1][i] = filledMarker
        field[8][i] = filledMarker

    
    # Fülle Feld mit Startpunkten (x = 5, y = 5)
    _field = fillFlood(field, 5, 5, emptyMarker, filledMarker)
    filledFields.append(_field)

    # Erzeuge Spielfeld aus field.txt Datei
    field = convertFileToField("field.txt", emptyMarker, filledMarker)
    _field = fillFlood(field, 14, 39, emptyMarker, "e")
    filledFields.append(_field)

    # Erzeuge Spielfeld aus field2.txt Datei
    field = convertFileToField("field2.txt", emptyMarker, filledMarker)
    _field= fillFlood(field, 7, 3, emptyMarker, "e")
    filledFields.append(_field)

    # Erzeuge Spielfeld aus field3.txt Datei
    field = convertFileToField("field3.txt", emptyMarker, filledMarker)
    _field = fillFlood(field, 15, 20, emptyMarker, "e")
    filledFields.append(_field)

     # Erzeuge Spielfeld aus monalisatxt Datei
    field = convertFileToField("monalisa.txt", emptyMarker, filledMarker)
    _field = fillFlood(field, 41, 65, emptyMarker, "e")
    filledFields.append(_field)
     
     # Erzeuge Spielfeld aus monalisatxt Datei
    field = convertFileToField("laby1.txt", emptyMarker, filledMarker)
    _field = fillFlood(field, 7, 22, emptyMarker, "e")
    filledFields.append(_field)

    if not VISUAL:
        # Gebe alle fertigen Felder aus
        for i in filledFields:
            print("\n\n\n")
            printField(i)
main()