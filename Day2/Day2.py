import re 
intList = []
fwdList = []
revList = []
safeCount = 0
import time

with open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2024\Day2\input.txt",'r') as reports:
    for line in reports:
        lineList = re.split(r'\s', line)
        lineList.pop()
        for i in range(len(lineList)):
            lineList[i] = int(lineList[i])

        fwdList = lineList.copy()
        revList = lineList.copy()
        fwdList.sort()
        revList.sort()
        revList.reverse()

        if lineList == fwdList or lineList == revList:
            for i in range(len(lineList)-1):
                if abs(lineList[i] - lineList[i+1])>=1 and abs(lineList[i] - lineList[i+1])<=3:
                    if i == len(lineList)-2:
                        safeCount += 1
                else:
                    break
    print((safeCount))