s = input("Enter a string: ")

count = {}

# Count frequency of each character
for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

# Find the first non-repeating character
found = False

for ch in s:
    if count[ch] == 1:
        print("First non-repeating character:", ch)
        found = True
        break

if not found:
    print("No non-repeating character found")
