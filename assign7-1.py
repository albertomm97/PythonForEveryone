# Use words.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("The file doesn't exists")
    
for line in fh:
    line = line.strip()
    print(line.upper())