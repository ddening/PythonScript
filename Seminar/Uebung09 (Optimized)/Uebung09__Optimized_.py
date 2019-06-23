# Seminar Uebung 08 (Testa02)                         
#  _____________________________________
#                                       
#          /               ,            
#  ----__-/----__----__--------__----__-
#    /   /   /___) /   ) /   /   ) /   )
#  _(___/___(___ _/___/_/___/___/_(___/_
#                                    /  
#                                (_ /   
# Quellen:

import sys
import colorama
import copy

# GLOBALE DEFINITION 
RED = '\033[31m'        # mode 31 = red forground
RESET = '\033[0m'       # mode 0  = reset

def printField(field):
    ''' Gibt das Spielfeld in der Konsole aus
        
    Args: 
        field (lst): Enthaelt das gesamte Spielfeld
    Returns:
        None
    '''

    for i in range(0, len(field)):
        _string = ""
        for j in range(0, len(field[i])):
            _string = _string + field[i][j]
        print(_string)
    print()

def _searchMaxLine(filename):
    ''' Hilfsfunktion fuer convertFileToField, welche die Laengste Zeile eines Bildes/Feldes ermittelt
        
        Args:
            filename (string): Name der Datei in der sich das Feld befindet
        Returns:
            max (int): Laenge der laengsten Zeile
    '''

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
    ''' Erstellt ein Feld als Liste aus einer .txt Datei, welche das Feld beinhaltet
        
        Args:
            filename (string): Dateiname
            emptyMarker (string): Zeichen mit dem <nichts> gefuellt wird
            filledMarker (string): Zeichen mit dem das Feld in der Liste aufgebaut wird
        Returns:
            field (lst): Fertiges Spielfeld als Liste, welche ebenfalls Listen enthaelt (2D-Array)
    '''

    field = []

    f = open(filename, "r")
    line = f.readline()

    _maxLine = _searchMaxLine(filename)

    while line:
        # Erzeuge leeres Spielfeld
        field.append([emptyMarker] * (_maxLine - 1))
        line = f.readline()

    f.close() 

    # Fuelle Feld
    f = open(filename, "r")
    line = f.readline()
    
    counter = 0
    while line:
        for j in range (0, len(line) - 1):
            field[counter][j] = line[j]
        line = f.readline()
        counter = counter + 1

    return field

def isFree(rowNumber, colNumber, arr):
    ''' Ueberprueft Feldposition auf Gueltigkeit
        
        Args:
            rowNumber (int): Zeile 
            colNumber (int): Spalte
            arr (lst): Spielfeld
        Returns:
            bool: True falls Feld leer -- sonst False
    '''
    if arr[rowNumber][colNumber] is not filledMarker:
        return True
    else:
        return False

def isEscape(rowNumber, colNumber, arr):
    ''' Ueberprueft ob Feldposition Ausgang ist
        
        Args:
            rowNumber (int): Zeile 
            colNumber (int): Spalte
            arr (lst): Spielfeld
        Returns:
            bool: True falls Feld Ausgang -- sonst False
    '''
    if arr[rowNumber][colNumber] is escapeSymbol:
        return True
    else:
        return False

def nodeVisited(rowNumber, colNumber, route):
    '''Docstring'''
    if (rowNumber, colNumber) in route:
        return True
    else:
        return False  

def isDeadEnd(rowNumber, colNumber, _arr):
    # Wenn alle Felder umherum belegt -> True
    if (isFree(rowNumber + 1, colNumber, _arr) and isFree(rowNumber - 1, colNumber, _arr) and isFree(rowNumber, colNumber + 1, _arr) and isFree(rowNumber, colNumber - 1, _arr)):
        return False

def findEscape(arr, rowNumber, colNumber, route = (), visited = [], sol = []):
    '''Docstring'''

    # Ausserhalb des Feldes
    if rowNumber < 0 or rowNumber >= len(arr) or colNumber < 0 or colNumber >= len(arr[rowNumber]):
        return

    # Definition
    stack = []
    escapeRoutes = []

    if isEscape(rowNumber, colNumber, arr):
        sol.append(route)
        return route

    if nodeVisited(rowNumber, colNumber, visited):
        return

    if not isFree(rowNumber, colNumber, arr):
        return

    # Fuege Pfadpunkt zu Route hinzu
    route += ((rowNumber, colNumber), )
    # stack.append((rowNumber, colNumber))
    visited.append((rowNumber, colNumber))

    findEscape(arr, rowNumber + 1, colNumber, route, visited, sol)
    findEscape(arr, rowNumber - 1, colNumber, route, visited, sol)
    findEscape(arr, rowNumber, colNumber + 1, route, visited, sol)
    findEscape(arr, rowNumber, colNumber - 1, route, visited, sol)

    return sol

    
def fillField(arr, path):
    ''' Visuelle Darstellung des Loesungspfades'''
    for coord in path:
        arr[coord[0]][coord[1]] = RED + 'e' + RESET

def main():
    '''Main Fkt'''

    # Globale Variablen
    global filledMarker
    global escapeSymbol

    # Init
    colorama.init()
    sys.setrecursionlimit(10000)

    # Definition der Variablen
    emptyMarker = ''
    filledMarker = 'x'
    escapeSymbol = 'E'

    # Erstelle Feld + Ausgabe
    arr = convertFileToField("field2.txt", emptyMarker, filledMarker)
    _arr = copy.deepcopy(arr)
    #printField(arr)

    b = findEscape(arr, 1, 1)
    print(b)

if __name__ == "__main__":
    main()