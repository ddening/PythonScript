
numberCol = 20
numberRows = 10

emptyMarker = " "
filledMarker = "x"

field = [[numberCol], [numberCol] ,         [],[]]


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
 
print()

#----
field=[]
zeile =[]

#oben
for t in range(0, numberCol):
    if t is 3 or t is 15:
        zeile.append(filledMarker)
    else:
        zeile.append(emptyMarker)
field.append(zeile)
zeile = []
for u in range(0, numberCol):
    zeile.append(filledMarker)
field.append(zeile)
zeile =[]
for rows in range(0, numberRows - 5):
    zeile=[]
    for col in range (0, numberCol):
        if col is 3 or col is 15:
            zeile.append(filledMarker)
        else:
            zeile.append(emptyMarker)
    field.append(zeile)
    
field.append(field[1])

#----Ausgabe
field.append(zeile)
for i in field:
    print(i)


