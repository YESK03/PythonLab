text = input("Enter a string:")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1
        
        
print("Character Frequency")

for ch, count in frequency.items():
    print(ch, ":",count)