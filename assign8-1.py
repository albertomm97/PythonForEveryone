fname = input("Enter file name: ")

try:
	fh = open(fname)
except:
    print("The file doesn't exists")

lst = list()
for line in fh:
    linesplit = line.split()
    for word in linesplit:
        if word in lst:
            continue
        else:
            lst.append(word)

            
lst.sort()
print(lst)