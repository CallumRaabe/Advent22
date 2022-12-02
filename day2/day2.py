def importInputFile():
    import os
    print(os.getcwd())
    with open('input.txt') as f:
        lines = f.read().split('\n')
        filteredLines = list(filter(None, lines)) # make sure we aren't getting the blank line at the end of the file
        return filteredLines

def decryptIntoPointsForMoves(input):
    moves = input.split()
    numbers = []
    for i in moves:
        match i:
            case 'A':
                numbers.append(1)
            case 'B':
                numbers.append(2)
            case 'C':
                numbers.append(3)
            case 'X':
                numbers.append(1)
            case 'Y':
                numbers.append(2)
            case 'Z':
                numbers.append(3)
    return numbers

def calculateWin(input):
    loss = 0
    draw = 3
    win = 6

    result = None

    if (input[0] == input[1]):
        result = draw
    elif ((input[0] == 1 and input[1] == 3) or (input[0] == 2 and input[1] == 1) or (input[0] == 3 and input[1] == 2)):
        result = loss
    elif ((input[1] == 1 and input[0] == 3) or (input[1] == 2 and input[0] == 1) or (input[1] == 3 and input[0] == 2)):
        result = win

    return (input[1] + result)    
            
def decrypeIntoMoveAndGameResult(input):

    loss = 0
    draw = 3
    win = 6

    points = None

    match input[0]:
        case 'A':
            points = 1
        case 'B':
            points = 2
        case 'C':
            points = 3

    result = None

    if (input[1] == 'X'): # loss
        match input[0]:
            case 'A':
                result = 3
            case 'B':
                result = 1
            case 'C':
                result = 2
        return result + loss

    elif(input[1] == 'Y'): 
        return (points + draw)

    elif (input[1] == 'Z'): # win
        match input[0]:
            case 'A':
                result = 2
            case 'B':
                result = 3
            case 'C':
                result = 1
        return result + win



file = importInputFile()

games = []

for game in file:
    games.append(decryptIntoPointsForMoves(game))

results = []

for game in games:
    results.append(calculateWin(game))

print(sum(results)) # pt 1 answer

newResults = []

for game in file:
    newResults.append(decrypeIntoMoveAndGameResult(game.split()))

print(sum(newResults)) # pt 2 answer