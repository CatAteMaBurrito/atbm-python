import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlipList = []
    for i in range(100):
        flip = random.randint(0, 1)
        if (flip == 0):
            coinFlipList.append('H')
        else:
            coinFlipList.append('T')
    # Code that checks if there is a streak of 6 heads or tails in a row.
    headsInARow = 0
    tailsInARow = 0
    for element in coinFlipList:
        if (headsInARow == 6 or tailsInARow == 6):
            numberOfStreaks += 1
            headsInARow = 0
            tailsInARow = 0
        if (element == 'H'):
            headsInARow += 1
            tailsInARow = 0
        if (element == 'T'):
            tailsInARow += 1
            headsInARow = 0
print('Chance of streak: %s%%' % (numberOfStreaks / 100))