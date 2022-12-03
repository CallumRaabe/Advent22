def importInputFile():
    with open('input.txt') as f:
        return f.read().split('\n\n')

def calculateElfTotal(string):
    list = filter(None, string.split())
    numbers = [eval(i) for i in list]
    result = sum(numbers)
    return result

def findHighestCalorieCount(array):
    print(max(array))
    
def findHighestThreeCounts(array):
    topThree = (sorted(array, reverse=True)[:3])
    print(sum(topThree))


arr = importInputFile()

elfTotals = []

for elf in arr:
    elfTotals.append(calculateElfTotal(elf))

findHighestCalorieCount(elfTotals)
findHighestThreeCounts(elfTotals)