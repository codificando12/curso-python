line = 'X-DSPAM-Confidence:0.8475'
line_lower = line.lower()
line_find = line_lower.find(':')
numbers = line_lower[line_find + 1:]
floating = float(numbers)
print(floating)