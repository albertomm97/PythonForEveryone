hrs = input("Hours:")
h = float(hrs)
rate = input("Rate:")
r = float(rate)

standardhours = 40
gross = 0

if h > 40:
    extrahours = h - standardhours
    gross = standardhours * r + (extrahours * (r * 1.5))
else:
    gross = h * r

print("Pay:", gross)