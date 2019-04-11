def insertion_sort(arr):
    """Sortier ein Array mit InsertionSort 

    Args:
        arr: zu sortierendes Array
    """

    # Ausgabe vom Startarray
    #Test
    print("Unsortiertes Array:  ", arr)
    test = 5

    # Durchlaufe jedes Element im Array
    for i in range(1, len(arr)):
        # zu vergleichender Wert
        element = arr[i] 
        # Index f�r Elemente links vom 'element'
        index_left = i-1 
        # solange der linke Wert gr��e als unser 'element' -- tausche deren Position
        while index_left > -1 and arr[index_left] > element:
            arr[index_left + 1] = arr[index_left]
            arr[index_left] = element
            index_left -= 1

    # Ausgabe vom Array
    print("Sortiertes Array:    ", arr)

def main():
    """Main Funktion"""

    # Erstelle Array
    myarr = [2, 1, 3, 17, 22, 21, 5239, 32, -12, 0, 2312, 231, 634, 2346, 19 , 9128, -5, 7] 
    # Funktionsaufruf mit dem unsortierten Array
    insertion_sort(myarr)

    # print(insertion_sort.__doc__)

main()