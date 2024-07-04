import math

def searchBinary(list, key):
  lenMin = 0
  lenMax = len(list)
  while lenMin < lenMax-1:
    lenMedium = math.floor((lenMin+lenMax)/2)
    if list[lenMedium] == key:
      return list.index(list[lenMedium])
    elif list[lenMedium] < key:
      lenMin = lenMedium
    elif list[lenMedium] > key:
      lenMax = lenMedium
  return -1

def sort(list):
  for i in range(len(list)):
    for j in range(len(list)-1):
      if list[j] > list[j+1]:
        aux = list[j+1]
        list[j+1] = list[j]
        list[j] = aux
  return list