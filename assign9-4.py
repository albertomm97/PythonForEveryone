name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

words = list()
mails = dict()
for line in handle:
    if not line.startswith("From "): continue
    line = line.rstrip()
    words = line.split()
    mails[words[1]] = mails.get(words[1], 0) + 1

largest = 0
author = None

for key in mails:
    if mails[key] > largest:
        largest = mails[key]
        author = key
        
print(author, largest)