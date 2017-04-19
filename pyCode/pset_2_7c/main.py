import random
def lastNumber(n, minRandom, maxRandom):
    residual = n
    while residual > 0:
        #lastN = round(random.uniform(minRandom+0.5, maxRandom+0.5))
        lastN = random.uniform(minRandom , maxRandom )
        residual = residual - lastN
    return lastN

def game2Player(n1, n2, minRandom, maxRandom):
    lastN1 = lastNumber(n1,minRandom, maxRandom)
    lastN2 = lastNumber(n2,minRandom, maxRandom)
    if lastN1 > lastN2:
        output = 1
    elif lastN1 < lastN2:
        output = 2
    else:
        output = 0
    return output

def runGame(i):
    secondWinN = 0
    for n in range(1,i):
        gameResult = game2Player(100, 200, 0, 100)
        if gameResult == 2:
            secondWinN = secondWinN + 1

    return float(secondWinN)/i

aaa = runGame(100000)
print(aaa)