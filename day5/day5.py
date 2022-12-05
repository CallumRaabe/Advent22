import copy

def importInputFile():
    with open('input.txt') as f:
        return f.read().strip().split('\n') # read the file, split each group into an array element and strip out the final blank line

# I have no clue how to parse that so let's just hardcode it
stacks = [
    ['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'],
    ['N', 'B', 'L'],
    ['J', 'C', 'H', 'T', 'L', 'V'],
    ['S', 'P', 'J', 'W'],
    ['Z', 'S', 'C', 'F', 'T', 'L', 'R'],
    ['W', 'D', 'G', 'B', 'H', 'N', 'Z'],
    ['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'],
    ['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'],
    ['R', 'P', 'M', 'L', 'H'],
]

file = importInputFile()

part1 = copy.deepcopy(stacks) # python sucks and doesn't create actual copies without an import...

del file[0:10] # remove the lines we've hardcoded and no longer care about

for line in file:
    arr = line.split() # split the string
    del arr[::2] # remove the descriptor words
    a,b,c = arr # pass the numbers to variables
    a = int(a)
    b = int(b) - 1
    c = int(c) - 1
    for _ in range(a):
        part1[c].append(part1[b].pop(-1))

result = ''
result = result.join(z[-1] for z in part1)
print('Part 1', result)

for line in file:
    arr = line.split()
    del arr[::2]
    a,b,c = arr
    a = int(a)
    b = int(b) - 1
    c = int(c) - 1
    stacks[c].extend(stacks[b][-a:])
    del stacks[b][-a:]

result2 = ''
result2 = result2.join(z[-1] for z in stacks)
print('Part 2', result2)