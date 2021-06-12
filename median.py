import csv

with open ('HeightWeight.csv', newline = '') as Hw : 
    reader = csv.reader(Hw)
    fileData = list(reader)

fileData.pop(0)

newList = []
for counter in range(len(fileData)) : 
    newRow = fileData[counter][1]
    newList.append(newRow)

noOfRows = len(newList)
newList.sort()

if (noOfRows % 2 == 0) :
    # 2 // signs is the symbol of floor division to get the nearest whole no.
    median1 = float(newList[noOfRows // 2])
    median2 = float(newList[noOfRows // 2 - 1])

    median = (median1 + median2) / 2

else : 
    median = newList[n // 2]

print (noOfRows)
print (str(median))