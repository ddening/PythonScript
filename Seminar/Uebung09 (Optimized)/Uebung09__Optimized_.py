# Seminar Uebung 09 (Testa02 - Optimized)                         
#  _____________________________________
#                                       
#          /               ,            
#  ----__-/----__----__--------__----__-
#    /   /   /___) /   ) /   /   ) /   )
#  _(___/___(___ _/___/_/___/___/_(___/_
#                                    /  
#                                (_ /   
# Quellen:
#

import sys
import colorama
import copy
import time

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

def printMap(map):
    for line in map:
        for j in line:
            if j[0] is -1:
                print("x", end= ' ')
            elif j[0] is 0:
                print(RED + 'F' + RESET, end= ' ')
            else:
                print(colorama.Fore.GREEN + "e" + RESET, end= ' ')
        print()

def printSimple(map):
    for r in map:
        for c in r:
            print(c[0], end = ' ')
        print()
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

# NOTES:
# -1 Knoten auf Karte noch nicht besucht
#  0 besuche diesen Weg nicht
def buildEmptyMap(arr):
    ''' Erzeugt <leere> Karte. <-1> symbolisiert dabei ein leeres bzw. nicht besuchtes Feld'''
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            arr[i][j] = [-1, ()]

    return arr

def isDeadEnd():
    pass

def _findEscape(arr, rowNumber, colNumber, routeMap, route = ()):
    '''Hilfsfunktion liefert alle moeglichen Pfade die Loesung sind'''

    # Ausserhalb des Feldes
    if rowNumber < 0 or rowNumber >= len(arr) - 1 or colNumber < 0 or colNumber >= len(arr[rowNumber]) - 1:
        return ()

    route += ((rowNumber, colNumber), )
   
    # Blockierter Knoten -> Stop
    if routeMap[rowNumber][colNumber][0] is 0:
        return ()

    # Knoten wurde bereits min. einmal ueber anderen Pfad erreicht
    if routeMap[rowNumber][colNumber][0] is not -1:

        # Falls derzeitige Route zum aktuellen Knoten laenger ist als anderer Pfad -> Stop
        if len(route) >= routeMap[rowNumber][colNumber][0]:
            # Vergleiche Pfad aus Karte mit aktuellen Pfad und blockiere Tupel/Knoten die nicht gleich sind
            # Loesche Teilpfad bzw. blockieren mit 0

            diff = tuple(set(route).difference(routeMap[rowNumber][colNumber][1]))
            for coord in diff:
                routeMap[coord[0]][coord[1]][0] = 0
            
            return ()
        
    # Ist aktuelle Zelle Ausgang? -> Ja: Speicher Pfad ab und return
    if isEscape(rowNumber, colNumber, arr):
        return route

    steps = ((0,1), (0, -1), (1, 0), (-1, 0))
    myRoutes = []

    for s in steps:
        newRow = rowNumber + s[0]
        newCol = colNumber + s[1]

        if isFree(newRow, newCol, arr) and not nodeVisited(newRow, newCol, route):
            routeMap[rowNumber][colNumber][0] = len(route)  # Setze neuen kuerzesten Weg in Karte
            routeMap[rowNumber][colNumber][1] = route       # Speichere dazugehoerigen Pfad ab

            # printSimple(routeMap)

            _route = copy.deepcopy(route)
            _tempRoute = _findEscape(arr, newRow, newCol, routeMap, _route)

            # Vermeide leere Liste
            if len(_tempRoute) > 0:
                myRoutes.append(_tempRoute) 
        else:
            # print("DeadEnd Row Col: ", rowNumber, colNumber)
            routeMap[newRow][newCol][0] = 0

    # Falls keine Bewegung moeglich
    if len(myRoutes) == 0:
        return ()

    # Bestimme Minimum
    sPath = min(myRoutes, key = len)

    return sPath

def findEscape(arr, rowNumber, colNumber, emptyMap, route = ()):
    '''Liefert kuerzesten Pfad als Loesung'''
    # Kuerzeste Loesung
    paths = _findEscape(arr, rowNumber, colNumber, emptyMap)
    print("Länge des Pfades: ", len(paths))

    return paths
    
def fillField(arr, path):
    ''' Visuelle Darstellung des Loesungspfades'''
    for coord in path:
        arr[coord[0]][coord[1]] = RED + 'e' + RESET
    return arr

def main():
    '''Main Fkt'''

    colorama.init()

    # Globale Variablen
    global filledMarker
    global escapeSymbol

    # Definition der Variablen
    emptyMarker = ''
    filledMarker = 'x'
    escapeSymbol = 'E'

    # Erstelle Feld
    arr = convertFileToField("field3.txt", emptyMarker, filledMarker)
    # Erstelle leere Karte
    emptyMap = buildEmptyMap(copy.deepcopy(arr))

    start = time.perf_counter()
    _t = findEscape(arr, 1, 1, emptyMap)
    end = time.perf_counter()
    
    print("Berechnungszeit in [s]: ", end - start)
    print("Kürzeste Route: ",_t)

    # Pfaddarstellung im Feld
    fillField(arr, _t)
    printField(arr)

    print("Karte mit blockierten Elementen: \n")
    printMap(emptyMap)

if __name__ == "__main__":
    main()