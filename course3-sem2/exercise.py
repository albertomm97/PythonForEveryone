import re

def getcount(lst):
    count = 0
    for number in lst:
        count = count + int(number)
    return count

filename = input("Enter filename:")

try:
    handle = open(filename)
except:
    print("File not found!")

count = 0
for line in handle:
    numbers = re.findall("[0-9]+", line)
    count = count + getcount(numbers)

print(count)
