import numpy
highA = 0
for i in range(0, 10000):
    print(i)
    voteA = 0
    for j in range(0, 64888):
        voteNow = numpy.random.rand()
        if voteNow<0.6549:
            voteA = voteA + 1
    if voteA > 32444:
        highA = highA + 1

print(highA)

