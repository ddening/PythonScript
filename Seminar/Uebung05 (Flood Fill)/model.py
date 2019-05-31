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

def defaultField():
    ''' Docstring'''

    # Spielfeldgröße
    numberOfColumns = 20    # Spalten
    numberOfRows = 10       # Zeilen

    emptyMarker = " "
    filledMarker = "x"

    # Erzeuge generische Liste
    field = []
    # Enthält fertige gefüllte Felder
    filledFields = []
    # Clean deep copy
    copyFields = []

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

    return field