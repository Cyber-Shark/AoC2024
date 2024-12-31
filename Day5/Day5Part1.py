import re

ruleList = []
pageList = []
sortedPageList = []


with open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2024\Day5\rules1.txt",'r') as rules:
    for line in rules:
        rule = line
        numbers = re.findall(r"\d+",rule)
        pageList.extend(numbers)
        ruleList.append(tuple(numbers))
    pageList= list(set(pageList))

def ruleSearch(inputRules, new, existing):
    for rule in range(len(inputRules)):
        if inputRules[rule][0] == new and inputRules[rule][1] == existing:
            return True #this means there is a rule that the new item is before the existing item
        
for i in range(len(pageList)):
    if i == 0:
        sortedPageList.append(pageList[0])
    else:
        for j in range(len(sortedPageList)):
            if ruleSearch(ruleList,pageList[i],sortedPageList[j]) == True:
                sortedPageList.insert(j-1,pageList[i])

print(pageList)
print(sortedPageList)
#for item in pageList:



#def buildOrder():