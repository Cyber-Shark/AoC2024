import re

listLeft = []
listRight = []
listDiff = []
simScore = 0

with open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2024\Day1\input.txt",'r') as rawLists:
    for line in rawLists:
        lineList = re.split("\s", line)
        listLeft.append(lineList[0])
        listRight.append(lineList[3])

listLeft.sort()
listRight.sort()

for i in range(len(listLeft)):
    listLeft[i] = int(listLeft[i])

for i in range(len(listRight)):
    listRight[i] = int(listRight[i])

for i in range(len(listLeft)):
    listDiff.append(abs(listLeft[i] - listRight[i]))
print("List Difference Sum")
print(sum(listDiff))

for i in range(len(listRight)):
    matchCount = listRight.count(listLeft[i])
    scoreItem = listLeft[i]*matchCount
    simScore = simScore + scoreItem             
print("Simiarity Score")
print(simScore)