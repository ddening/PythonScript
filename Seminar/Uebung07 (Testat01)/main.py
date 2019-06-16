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
# https://www.inf-schule.de/grenzen/komplexitaet/sortieren/sortieralgorithmen/selectionsort
# https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format
# https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html#example-google

# Libraries
import random
import matplotlib.pyplot
import copy
import bubble
import insertion
import selection

# Globale scope
MAX_NUMBERS_IN_LIST = 100 + 1

def testListsGenerator(MAX_NUMBERS_IN_LIST):
    '''Erzeugt Liste mit Listen, welche zufaellige Zahlen beinhalten

    Args:
        MAX_NUMBERS_IN_LIST (const): Maximale Anzahl an Nummern in der letzen Liste

    Return:
        lst: Liste bestehend aus anderen Listen mit zufaelligen Zahlen gefuellt
    '''

    # Definition einer leeren Liste
    myList = []

    # Fülle Liste mit zufälligen Zahlen zwischen 0 und x
    myList = [random.randint(0, 99) for i in range(0, MAX_NUMBERS_IN_LIST)]

    return myList
    
def plot():
    '''Plottet die Laufzeiten der Sortierverfahren in einem Diagramm '''

    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(1,1,1)

    # Initialliste
    bubbleLst = [testListsGenerator(i) for i in range(0, MAX_NUMBERS_IN_LIST)]
    # Kopie für InsertionSort
    insertionLst = copy.deepcopy(bubbleLst)
    # Kopie für SelectionSort
    selectionLst = copy.deepcopy(bubbleLst)

    # Funktion [x ; y]
    # x: Anzahl der Elemente -- y: Zeit zum sortieren

    ax.plot([i for i in range(0, MAX_NUMBERS_IN_LIST)], [bubble.bubbleSort(j) for j in bubbleLst],  '.', color='c', )
    ax.plot([i for i in range(0, MAX_NUMBERS_IN_LIST)], [insertion.insertionSort(j) for j in insertionLst],  '.', color='m')
    ax.plot([i for i in range(0, MAX_NUMBERS_IN_LIST)], [selection.selectionSort(j) for j in selectionLst],  '.', color='r', )

    # Legende
    ax.legend(['BubbleSort', 'InsertionSort', 'SelectionSort'])
    ax.set_xlabel('Anzahl Elemente in Liste')
    ax.set_ylabel('Sortierzeit in s')
    matplotlib.pyplot.show()

def main():
    '''Main Funktion '''
    plot()

main()