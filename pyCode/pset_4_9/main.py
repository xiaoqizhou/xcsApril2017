f = open("./randomFlips2.txt","r")
flipResult = f.readlines()
flipResultStr = flipResult[0]
charList = list(flipResultStr)
print charList

matchesT = [x for x in charList if x == 'T']
nT = len(matchesT)
matchesH = [x for x in charList if x == 'H']
nH = len(matchesH)

pT = float(nT)/(nT+nH)
pH = float(nH)/(nT+nH)
print 'Number of tails: {}'.format(nT)
print 'Number of heads: {}'.format(nH)
print 'Total number: {}'.format(nT+nH)
print 'Probability of tails: {}'.format(pT)
print 'Probability of heads: {}'.format(pH)
matchesTT = 0
matchesTH = 0
matchesHH = 0
matchesHT = 0
for i in range(0, len(charList)-1):
    if (charList[i] == 'T') and (charList[i+1] == 'T'):
        matchesTT = matchesTT + 1
    elif (charList[i] == 'T') & (charList[i+1] == 'H'):
        matchesTH = matchesTH + 1
    elif (charList[i] == 'H') & (charList[i+1] == 'H'):
        matchesHH = matchesHH + 1
    else:
        matchesHT = matchesHT + 1

pTT = float(matchesTT)/(matchesTT+matchesTH )
pTH = float(matchesTH)/(matchesTT+matchesTH )
pHH = float(matchesHH)/(matchesHT+matchesHH )
pHT = float(matchesHT)/(matchesHT+matchesHH )
pTT2 = float(matchesTT)/(nT+nH)
pTH2 = float(matchesTH)/(nT+nH )
pHH2 = float(matchesHH)/(nT+nH )
pHT2 = float(matchesHT)/(nT+nH )
print 'Probability of tails| previous heads: {}'.format(pHT)
print 'Probability of tails| previous tails: {}'.format(pTT)
print 'Probability of Head| previous heads: {}'.format(pHH)
print 'Probability of Head| previous tails: {}'.format(pTH)

print 'Probability of tails,previous heads: {}'.format(pHT2)
print 'Probability of tails,previous tails: {}'.format(pTT2)
print 'Probability of Head,previous heads: {}'.format(pHH2)
print 'Probability of Head,previous tails: {}'.format(pTH2)



