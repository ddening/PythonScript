
def loadMaze( mazeFile):
    file = open(mazeFile,"r")
    field = [list(row) for row in file.read().splitlines()]
    file.close()

    return field

def showMaze(maze):
    for row in range(len(maze)):
        print(*maze[row])
        #print(maze)

def isEscape(x,y):
    if field[x][y] == "E":
        return True
    else:
        return False
def isFree(x,y):
    if field[x][y] != "x":
        return True
    else:
        return False

def findEscape(x,y, route):

    if isEscape(x,y):
        return [(x,y)]
    else:
        localRoutes = []
        route.append((x,y))

        if isFree(x+1,y) and (x+1,y) not in route:
            localRoutes.append(findEscape(x+1,y,route))
        if isFree(x,y+1) and (x,y+1) not in route:
            localRoutes.append(findEscape(x,y+1,route))
        if isFree(x-1,y) and (x-1,y) not in route:
            localRoutes.append(findEscape(x-1,y,route))
        if isFree(x,y-1) and (x,y-1) not in route:
            localRoutes.append(findEscape(x,y-1,route))

    if len(localRoutes)>0:
        i=0
        while True:
            if localRoutes[i] == []:
                del localRoutes[i]
                i = i-1
            i = i+1
            if i >= len(localRoutes):
                break

        if len(localRoutes)>0:
            min = 0
            for i in range(0,len(localRoutes)):
                if(len(localRoutes[i])< len(localRoutes[min])):
                    min = i

            localRoutes[min].append((x,y))
            return localRoutes[min]
        else:
            return []

    else:
        return []


field = loadMaze("field2.txt")
showMaze(field)
escapeRoute = findEscape(1,1,[])

for i in escapeRoute:
    field[i[0]][i[1]] = "o"

showMaze(field)
print(escapeRoute)