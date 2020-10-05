def computepay(h, r):
    standardhours = 40
    gross = 0
    
    if h > 40:
        extrahours = h - standardhours
        gross = standardhours * r + (extrahours * (r * 1.5))
    else:
        gross = h * r
    return gross

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Rate:")
r = float(rate)

p = computepay(h,r)
print("Pay",p)