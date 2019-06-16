# Seminar Uebung 07 (Testa01)                         
#  _____________________________________
#                                       
#          /               ,            
#  ----__-/----__----__--------__----__-
#    /   /   /___) /   ) /   /   ) /   )
#  _(___/___(___ _/___/_/___/___/_(___/_
#                                    /  
#                                (_ /   
# Quellen:
# https://www.inf-schule.de/grenzen/komplexitaet/sortieren/sortieralgorithmen/selectionsort

import time

def selectionSort(arr):
    '''Sortiert eine uebergebene Liste mit mit dem SelectionSort Algorithmus

    Args:
        arr (lst): Unsortierte Liste mit Datensaetzen

    Returns:
        time (float): Benoetigte Zeit um Liste zu sortieren
    
    '''
    
    _start = time.clock()

    # Startposition für Suche nach dem Minimum -- S = [ leer ] -- U = [ alle Elemente aus arr]
    currentIdx = 0
    # Laenge der Liste
    lstLength = len(arr)

    while currentIdx < lstLength:
        newMinIdx = currentIdx 
        # Suche kleinstes Element in Liste
        for i in range(currentIdx, lstLength):    
            if arr[i] < arr[newMinIdx]:
                # Neuer Index mit Minimum
                newMinIdx = i
        # Tausche Elemente
        arr[currentIdx], arr[newMinIdx] = arr[newMinIdx], arr[currentIdx]

        currentIdx = currentIdx + 1

    _end = time.clock()
    _time = _end - _start

    return _time