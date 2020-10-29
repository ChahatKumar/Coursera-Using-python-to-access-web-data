# week 2 assignment : read through and parse a file -> compute the sum of all numbers present 

import re

fileName = input("Enter file name :")
dataFile = open(fileName)

sum = 0
count = 0

for line in dataFile :
  numbers = re.findall('[0-9]+', line)
  if len(numbers) > 0 :
    for num in numbers :
       count = count +1
       sum = sum + int(num) 

print(" There are total ", count," numbers , and their sum is ", sum)

