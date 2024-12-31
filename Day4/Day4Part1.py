import re
lineList = []
gridList = []

puzzleSide = 140
wordsFound = 0
xmasFound = 0

with open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2024\Day4\input2.txt",'r') as searchGrid:
    for line in searchGrid:
        line.strip()
        lineList = []
        for character in line:
            lineList.append(character)
        gridList.append(lineList)

def wordCheck(wordInput):
    if wordInput == 'XMAS' or wordInput == 'SAMX':
        global wordsFound
        wordsFound += 1

def xCheck(wordInput):
    if wordInput == 'MMASS' or wordInput == 'SSAMM'or wordInput == 'SMASM'or wordInput == 'MSAMS':
        global xmasFound
        xmasFound += 1

def horiz(grid):
    for row in range(puzzleSide):
        for column in range(puzzleSide-3):
            a = gridList[row][column]
            b = gridList[row][column+1]
            c = gridList[row][column+2]
            d = gridList[row][column+3]
            word = a+b+c+d
            wordCheck(word)

def vert(grid):
    for row in range(puzzleSide-3):
        for column in range(puzzleSide):
            a = gridList[row][column]
            b = gridList[row+1][column]
            c = gridList[row+2][column]
            d = gridList[row+3][column]
            word = a+b+c+d
            wordCheck(word)

def fwdDiag(grid):
    for row in range(puzzleSide-3):
        for column in range(puzzleSide-3):
            a = gridList[row][column]
            b = gridList[row+1][column+1]
            c = gridList[row+2][column+2]
            d = gridList[row+3][column+3]
            word = a+b+c+d
            wordCheck(word)

def backDiag(grid):
    for row in range(puzzleSide-3):
        for column in range(puzzleSide-3):
            a = gridList[row+3][column]
            b = gridList[row+2][column+1]
            c = gridList[row+1][column+2]
            d = gridList[row][column+3]
            word = a+b+c+d
            wordCheck(word)

def xPattern(grid):
    for row in range(puzzleSide-2):
        for column in range(puzzleSide-2):
            a = gridList[row][column]
            b = gridList[row][column+2]
            c = gridList[row+1][column+1]
            d = gridList[row+2][column]
            e = gridList[row+2][column+2]
            word = a+b+c+d+e
            xCheck(word)


horiz(gridList)
vert(gridList)
fwdDiag(gridList)
backDiag(gridList)
xPattern(gridList)


print(wordsFound)
print(xmasFound)