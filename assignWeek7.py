largest = None
smallest = None
number = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
        
    try:
        number = int(num)
    except:
        print("Invalid input")
        continue
        
    if smallest is None:
            smallest = number
            
    if largest is None:
            largest = number
        
    if number < smallest: 
          smallest = number
            
    if number > largest:
          largest = number
        
        
print("Maximum is", largest)
print("Minimum is", smallest)