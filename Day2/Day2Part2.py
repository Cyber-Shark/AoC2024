import re 
report = []
fwdReport = []
revReport = []
safeCount = 0
lineNum = 0

orderSafe = False
diffSafe = False

def orderCheck(reportCheck):
    fwdReport = reportCheck.copy()
    revReport = reportCheck.copy()
    fwdReport.sort()
    revReport.sort()
    revReport.reverse()
    global orderSafe

    if reportCheck == fwdReport or reportCheck == revReport:
        orderSafe = True
    else:
        orderSafe = False

def diffCheck(reportCheck):
    global diffSafe
    for i in range(len(reportCheck)-1):
        first = reportCheck[i]
        second = reportCheck[i+1]

        if first == second or abs(first-second)>3:
            diffSafe = False
            break
        else:
            diffSafe = True


with open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2024\Day2\input.txt",'r') as allReports:
    for line in allReports:

        report = re.split(r'\s', line)
        report.pop()
        for i in range(len(report)):
            report[i] = int(report[i])

        orderSafe = False
        diffSafe = False
        initial = True
        orderCheck(report)
        diffCheck(report)

        if orderSafe == True and diffSafe == True:
            safeCount += 1
        else:
            for element in range(len(report)):
                reportTemp = report.copy()
                reportTemp.pop(element)
                
                orderCheck(reportTemp)
                diffCheck(reportTemp)
                if orderSafe == True and diffSafe == True:
                    safeCount += 1
                    print("SAVED!!!", safeCount)
                    break

            
    print("Final: ",safeCount)