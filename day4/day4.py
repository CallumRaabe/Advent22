def importInputFile():
    with open('input.txt') as f:
        return f.read().strip().split('\n') # read the file, split each group into an array element and strip out the final blank line

# Main function for Part 1
def checkForTotalEncapsulation(input):
    a,b = input.split(',') # split the pairs
    a1,a2 = map(int, a.split('-')) # now split the lower and upper bounds of the ranges
    b1,b2 = map(int, b.split('-'))
    if (a1 <= b1 <= b2 <= a2) or (b1 <= a1 <= a2 <= b2): # check if one range exists entirely within another
        return 1
    else:
        return 0 # make sure we don't increment if nothing matches or error out from no return    

# Main function for Part 2
def checkForAnyDuplication(input):
    a,b = input.split(',')
    a1,a2 = map(int, a.split('-'))
    b1,b2 = map(int, b.split('-'))
    if (a2 >= b1 and a1 <= b2) or (b2 >= a1 and b1 <= a2): # check if any values are shared between the ranges
        return 1
    else:
        return 0 


lines = importInputFile()

totalDuplicates = 0
anyDuplicates = 0

# let's do them both at once because we can
for line in lines:
    totalDuplicates += checkForTotalEncapsulation(line) # the amount that totally encompasses the pair
    anyDuplicates += checkForAnyDuplication(line) # the amount that has any sort of duplication

print('Part 1', totalDuplicates)
print('Part 2', anyDuplicates)
