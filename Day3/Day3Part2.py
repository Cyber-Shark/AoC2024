import re

multList = []
finalSplit = []
mulMatches = []

with open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2024\Day3\input.txt",'r') as corrupted:
    text = "TRUE" + corrupted.read()
    doPattern = r"do\(\)"
    dontPattern = r"don't\(\)"
    mulPattern = r"mul\(\d+,\d+\)"
    numberPattern = r"\d+"

    
    modText1 = re.sub(doPattern,'do()TRUE',text)
    modText2 = re.sub(dontPattern,'don\'t()FALSE',modText1)
    doSplit = re.split(doPattern,modText2)

    for line in doSplit:
        dontSplit = re.split(dontPattern,line)
        finalSplit.extend(dontSplit)

    for item in finalSplit:
        if item.startswith("TRUE"):
            lineMatches = re.findall(mulPattern,item)
            mulMatches.extend(lineMatches)

    for item in mulMatches:
        numbers = re.findall(numberPattern,item)
        first = int(numbers[0])
        second = int(numbers[1])

        multList.append(first*second)

print(sum(multList))

