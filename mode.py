import csv
from collections import Counter

with open ('HeightWeight.csv', newline = '') as Hw : 
    reader = csv.reader(Hw)
    fileData = list(reader)

fileData.pop(0)

newdata = []
#data is being sorted to get the height

for i in range(len(fileData)):
  n_num = fileData[i][1]
  newdata.append(float(n_num))

modedata = Counter(newdata)
json_data = {
    "50-60":0,
    "60-70":0,
    "70-80":0,
}
for height,occurence in modedata.items():
  if 50 < float(height) < 60:
    json_data["50-60"] += occurence
  
  elif 60 < float(height) < 70:
    json_data["60-70"] += occurence

  elif 70 < float(height) < 80:
    json_data["70-80"] += occurence

mode_range,mode_occurence = 0,0
for range,occurence in json_data.items():
  if occurence > mode_occurence:
    mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])],occurence
  
mode = float((mode_range[0]+mode_range[1])/2)
print(mode) 