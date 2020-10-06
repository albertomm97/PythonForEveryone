# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("The file doesn't exists")
    
count = 0
total = 0
    
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count + 1
        pos = line.find("0")
        number = line[pos:]
        number = number.strip()
        total = total + float(number)
        
    
print("Average spam confidence:", total/count)