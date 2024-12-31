import re

multList = []

with open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2024\Day3\input.txt",'r') as corrupted:
    text = corrupted.read()
    pattern = r"mul\(\d+,\d+\)"
    numberPattern = r"\d+"

    matches =re.findall(pattern,text)
    for line in matches:
        numbers = re.findall(numberPattern,line)
        first = int(numbers[0])
        second = int(numbers[1])

        multList.append(first*second)

print(sum(multList))

