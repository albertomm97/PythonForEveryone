text = "X-DSPAM-Confidence:    0.8475";

pos = text.find("0")
number = float(text[pos:])
print(number)