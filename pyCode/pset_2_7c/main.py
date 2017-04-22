import random

randomHist = [0 for x in range(100)]
lastN1Hist = [0 for x in range(100)]
lastN2Hist = [0 for x in range(100)]
def lastNumber(n, minRandom, maxRandom, startNum):
    global randomHist
    totalN = startNum
    while totalN < n:
        lastN = random.randint(1,100)
        randomHist[int(lastN)-1] = randomHist[int(lastN)-1]+ 1
        #lastN = round(random.uniform(minRandom+0.5, maxRandom+0.5))
        #lastN = random.uniform(minRandom , maxRandom )

        totalN = totalN + lastN
    return [lastN,totalN]

def game2Player(n1, n2, minRandom, maxRandom):
    lastR1 = lastNumber(n1,minRandom, maxRandom,0)
    lastR2 = lastNumber(n2,minRandom, maxRandom,lastR1[1])
    lastN1 = lastR1[0]
    lastN2 = lastR2[0]
    lastN1Hist[int(lastN1) - 1] = lastN1Hist[int(lastN1) - 1] + 1
    lastN2Hist[int(lastN2) - 1] = lastN2Hist[int(lastN2) - 1] + 1
    if lastN1 > lastN2:
        output = 1
    elif lastN1 < lastN2:
        output = 2
    else:
        output = 0
    return output

def runGame(i):
    secondWinN = 0
    for n in range(0,i):
        gameResult = game2Player(100, 200, 0, 100)
        if gameResult == 2:
            secondWinN = secondWinN + 1

    return float(secondWinN)/i

aaa = runGame(1000000)
print(aaa)
print(randomHist)
print(lastN1Hist)
print(lastN2Hist)
print(sum(randomHist))