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

# Libraries
import random
import time
import matplotlib.pyplot
import copy

# Globale scope
MAX_NUMBERS_IN_LIST = 5

''' ======= TODO =======
+ Sortieralgorithmen implementieren

+ Liste mit Listen zu sortierender Elemente erstellen

+ Alle Grafen in einem Plot darstellen
'''

def testListsGenerator(MAX_NUMBERS_IN_LIST):
    ''' Docstring '''

    # Definition einer leeren Liste
    myList = []
    # Fülle Liste mit zufälligen Zahlen
    myList = [random.randint(0, 99) for i in range(0, MAX_NUMBERS_IN_LIST)]

    return myList
    
def _plot():
    ''' Docstring '''

    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(1,1,1)

    # Initialliste
    bubbleLst = [testListsGenerator(i) for i in range(0, MAX_NUMBERS_IN_LIST)]
    # Kopie für InsertionSort
    insertionLst = copy.deepcopy(bubbleLst)
    # Kopie für SelectionSort
    selectionLst = copy.deepcopy(bubbleLst)

    cp1 = copy.deepcopy(bubbleLst)
    cp2 = copy.deepcopy(bubbleLst)

    # Funktion [x ; y]
    # x: Anzahl der Elemente -- y: Zeit zum sortieren

    lst = [k for k in [bubbleSort(j) for j in bubbleLst]]
    print(lst)

    ax.plot([len(testListsGenerator(i)) for i in range(0, MAX_NUMBERS_IN_LIST)], [bubbleSort(j) for j in bubbleLst],  '.', color='c', )
    #ax.plot([len(testListsGenerator(i)) for i in range(0, MAX_NUMBERS_IN_LIST)], [bubbleSort(j) for j in cp1],  '.', color='m', )
    #ax.plot([len(testListsGenerator(i)) for i in range(0, MAX_NUMBERS_IN_LIST)], [insertionSort(j) for j in insertionLst],  '.', color='r')
    #ax.plot([len(testListsGenerator(i)) for i in range(0, MAX_NUMBERS_IN_LIST)], [insertionSort(j) for j in cp2],  '.', color='b', )

    # Insertion

    ax.legend(['Bubblesort 1. Durchl.', 'Bubblesort 2. Durchl.', 'Insertionsort 1. Durchl.', 'Insertionsort 2. Durchl.'])
    ax.set_xlabel('Anzahl Elemente in Liste')
    ax.set_ylabel('Sortierzeit in s')
    matplotlib.pyplot.show()

def bubbleSort(arr):
    ''' Docstring '''
    n = len(arr)

    start = time.clock()

    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    end = time.clock()
    return end-start

def insertionSort(arr):
    """Sortiert ein Array mit InsertionSort 

    Args:
        arr: zu sortierendes Array
    """

    start = time.clock()

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

    end = time.clock()

    return end-start
    
def selectionSort():
    '''Docstring'''
    pass

def main():
    arr = [1,5,3,12,6,213,12,4,123,12,5]
    #bubbleSort(testListsGenerator(MAX_NUMBERS_IN_LIST))
    #print(r)
    # testListsGenerator(MAX_NUMBERS_IN_LIST)
    _plot()
main()