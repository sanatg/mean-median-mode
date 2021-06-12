import csv

with open ('HeightWeight.csv', newline = '') as Hw : 
    reader = csv.reader(Hw)
    fileData = list(reader)

fileData.pop(0)

newList = []
for counter in range(len(fileData)) : 
    newRow = fileData[counter][1]
    newList.append(float(newRow))

noOfRows = len(newList)
total = 0
for i in newList : 
    total += i

mean = total / noOfRows 
print (mean)