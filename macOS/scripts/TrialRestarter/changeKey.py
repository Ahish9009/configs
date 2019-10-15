import random

with open("/Applications/Adobe InDesign CC 2018/Resources/AMT/ID/AMT/application.xml", "r") as f:

    allLines = f.readlines()

trialLine = allLines[21]
keyLength = 0
oldKey = ""

for i in trialLine:

    try:
        currentLetter = int(i)
        keyLength += 1
        oldKey += i
    except:
        pass

#keyLength = 24
#print(oldKey)

with open("/Users/ahish/Desktop/Ahish/Scripts/TrialRestarter/usedKeys", "r") as f:
    allUsedString = f.readlines()

allUsedList = []
for i in allUsedString:
    allUsedList += [int(i.rstrip("\n"))]
'''
new = random.randint(10**(keyLength-1), 10**(keyLength)-1)
print(new)
'''
new = oldKey
while (new in allUsedList ) or (new == oldKey):
    lastDigit = random.randint(0,9)
    while (lastDigit == int(oldKey[-1])):
        lastDigit = random.randint(0,9)
    secondLast = random.randint(0,9)
    while (secondLast == int(oldKey[-1])):
        secondLast = random.randint(0,9)
    
    new = list(str(new))
    new[-1] = str(lastDigit)
    new[-2] = str(secondLast)
#    print(new)
    temp = ""
    for i in new:
        temp += i
    new = int(temp)
#print(new)

while new in allUsedList:

    new = random.randint(10**(keyLength-1), 10**(keyLength)-1)

newTrialLine = "        <Data key=\"TrialSerialNumber\">"+str(new)+"</Data>\n"

allLines[21] = newTrialLine

with open("/Applications/Adobe InDesign CC 2018/Resources/AMT/ID/AMT/application.xml", "w") as f:

    for i in allLines:
        f.write(i)

with open("/Users/ahish/Desktop/Ahish/Scripts/TrialRestarter/usedKeys", "w") as f:

    for i in allUsedString:
        f.write(i)

    f.write(str(new)+"\n")

