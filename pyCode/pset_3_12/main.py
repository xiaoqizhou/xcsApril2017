import csv
import numpy
def loadCsvData(fileName):
    matrix = []
    # open a file
    with open(fileName) as f: #will automatically close the file after the section
        reader = csv.reader(f)

        # loop over each row in the file
        for row in reader:

            # cast each value to a float
            doubleRow = []
            for value in row:
                try:
                    doubleRow.append(float(value))
                except:
                    pass


            # store the row into our matrix
            if doubleRow != []:
                matrix.append(doubleRow)
    return matrix

pullMatrix = loadCsvData('polls.csv')

pullArray = numpy.array(pullMatrix)

aArray = pullArray[:,1]
bArray = pullArray[:,2]

aSum = numpy.sum(aArray)
bSum = numpy.sum(bArray)
totalSum = aSum+bSum
pA = aSum/totalSum
pB = bSum/totalSum

print(aSum)
print(bSum)
print(totalSum)
print(pA)
print(pB)

print(pullArray)