def importInputFile():
    with open('input.txt') as f:
        return f.read().split('\n\n')

def calculateElfTotal(array):
    list = filter(None, array.split())
    numbers = [eval(i) for i in list]
    return sum(numbers)

def findHighestCalorieCount(array):
    print(max(array))
    
def findHighestThreeCounts(array):
    topThree = (sorted(array, reverse=True)[:3])
    print(sum(topThree))


file = importInputFile()

elfTotals = []

for elf in file:
    elfTotals.append(calculateElfTotal(elf))

findHighestCalorieCount(elfTotals)
findHighestThreeCounts(elfTotals)