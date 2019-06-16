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
# https://www.geeksforgeeks.org/bubble-sort/
# https://en.wikipedia.org/wiki/Bubble_sort

import time

def bubbleSort(arr):
    '''Sortiert eine uebergebene Liste mit dem BubbleSort Algorithmus

    Args:
        arr (lst): Unsortierte Liste mit Datensaetzen

    Returns:
        time (float): Benoetigte Zeit um Liste zu sortieren
    
    '''

    _start = time.clock()

    n = len(arr)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    _end = time.clock()
    _time = _end - _start

    return _time