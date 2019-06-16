# Seminar Uebung 07 (Testa01)                         
#  _____________________________________
#                                       
#          /               ,            
#  ----__-/----__----__--------__----__-
#    /   /   /___) /   ) /   /   ) /   )
#  _(___/___(___ _/___/_/___/___/_(___/_
#                                    /  
#                                (_ /   

import time

def insertionSort(arr):
    '''Sortiert eine uebergebene Liste mit dem InsertionSort Algorithmus

    Args:
        arr (lst): Unsortierte Liste mit Datensaetzen

    Returns:
        time (float): Benoetigte Zeit um Liste zu sortieren
    
    '''

    _start = time.clock()

    # Durchlaufe jedes Element im Array
    for i in range(1, len(arr)):
        # zu vergleichender Wert
        element = arr[i] 
        # Index fuer Elemente links vom 'element'
        index_left = i-1 
        # solange der linke Wert groeßer als unser 'element' -- tausche deren Position
        while index_left > -1 and arr[index_left] > element:
            arr[index_left + 1] = arr[index_left]
            arr[index_left] = element
            index_left -= 1

    _end = time.clock()
    _time = _end - _start

    return _time