
numberCol = 20
numberRows = 10

emptyMarker = " "
filledMarker = "x"

field = []
zeile = []

print("Ausgabe über print():")
for oben in range(0, numberCol):
    if oben is 3 or oben is 15:
        print(filledMarker, end ="")
    else:
        print(emptyMarker, end = "")
print()
print(filledMarker * numberCol)

for rows in range(0, numberRows - 4):
    for col in range (0, numberCol):
        if col is 3 or col is 15:
            print(filledMarker, end ="")
        else:
            print(emptyMarker, end = "")
        if col is numberCol-1:
            print()
   
# Unten
print(filledMarker * numberCol)

for oben in range(0, numberCol):
    if oben is 3 or oben is 15:
        print(filledMarker, end ="")
    else:
        print(emptyMarker, end = "")
 
print("\n----")

print("Ausgabe über field[]: ")

# 1. Zeile
for t in range(0, numberCol):
    if t is 3 or t is 15:
        zeile.append(filledMarker)
    else:
        zeile.append(emptyMarker)
field.append(zeile)

# 2.Zeile
zeile = []
for u in range(0, numberCol):
    zeile.append(filledMarker)
field.append(zeile)

# Inhalt
zeile =[]
for rows in range(0, numberRows - 4):
    zeile=[]
    for col in range (0, numberCol):
        if col is 3 or col is 15:
            zeile.append(filledMarker)
        else:
            zeile.append(emptyMarker)
    field.append(zeile)
    
# Letzten Zeilen gleich wie oben
# vorletzte Zeile
zeile=[]
for u in range(0, numberCol):
    zeile.append(filledMarker)
field.append(zeile)

# letzte Zeile
zeile = []
for t in range(0, numberCol):
    if t is 3 or t is 15:
        zeile.append(filledMarker)
    else:
        zeile.append(emptyMarker)
field.append(zeile)

#----Ausgabe
for i in field:
    print(i)

print("----")

def printField(field, numRows, numCols):
    eString=""

    for row in range(0, numRows):
        for col in range(0, numCols):
            eString = eString + field[row][col]
        eString = eString + '\n'

    return eString

print("Ausgabe über Funktion printField(): ")
print(printField(field, numberRows, numberCol))

print("----")

print("Test, ob field[] sich ändern lässt:")
field[5][10] = "e"
print(printField(field, numberRows, numberCol))