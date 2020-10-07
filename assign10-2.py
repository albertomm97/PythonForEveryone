name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = dict()
lst = list()
pos = None
hour = None

for line in handle:
    if not line.startswith("From "): continue
    line = line.rstrip()
    pos = line.find(":")
    hour = line[pos-2:pos]
    hours[hour] = hours.get(hour, 0) + 1

for key,val in hours.items():
    lst.append((key, val))

lst = sorted(lst)

for key, val in lst:
    print(key, val)