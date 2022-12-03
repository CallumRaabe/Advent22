def importInputFile():
    with open('input.txt') as f:
        return f.read().strip().split('\n')

def getDuplicateValue(input): 
    if(input.islower()):
        return ord(input) - ord('a') + 1
    elif(input.isupper()):
        return ord(input) - ord('A') + 27 # capitals are before lowercase in unicode

lines = importInputFile()

# Part 1
result = 0
for line in lines:
    indexMod = len(line) // 2 # modifier for the array index
    dupe, = set(line[:indexMod]) & set(line[indexMod:]) # get the shared letter
    result += getDuplicateValue(dupe) # calculate value from unicode value
print('Part 1', result)

# Part 2
result2 = 0
for line in range(0, len(lines), 3):
    line1, line2, line3 = lines[line:line+3] # get the three lines in the group
    dupes, = set(line1) & set(line2) & set(line3) # find the shared letter
    result2 += getDuplicateValue(dupes) # calculate value from unicode value
print('Part 2', result2)
