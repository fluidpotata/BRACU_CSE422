import heapq


def dataInput(file):
    with open(file) as inp:
        readData = []
        data = inp.readline().split()
        while data:
            readData.append(data)
            data = inp.readline().split()
    return readData


def fixingData(readData):
    heuristicValues = {}
    realDistances = {}

    for i in readData:
        heuristicValues[i[0]] = int(i[1])
        realDistances[i[0]] = {}
        for j in range(2,len(i),2):
            realDistances[i[0]][i[j]] = int(i[j+1])
    return heuristicValues, realDistances


def aStarSearch(heuristicValues,realDistances, start,end):
    path = []
    pqueue = []
    pqueue.append((heuristicValues[start]+0, 0,  start))
    found = False
    while pqueue:
        currNode = heapq.heappop(pqueue)
        # print(currNode)
        if len(path)<1 or currNode[2] in realDistances[path[-1]].keys():
            path.append(currNode[2])
            if currNode[2]==end:
                found = True
                print("Path: ", " -> ".join(path))
                print(f"Total Distance: {currNode[1]} km")
                break

            for i in realDistances[currNode[2]].keys():
                heapq.heappush(pqueue,(heuristicValues[i]+currNode[1]+realDistances[currNode[2]][i], currNode[1]+realDistances[currNode[2]][i], i))
    if not found:
        print("No path found!")



readData = dataInput("22101221_Md Ibrahim Alif_CSE422_09_Lab_Assignment01_InputFile_Summer2024.txt")
heuristicValues, realDistances = fixingData(readData)
# aStarSearch(heuristicValues, realDistances, "Arad", "Bucharest")
print(realDistances)