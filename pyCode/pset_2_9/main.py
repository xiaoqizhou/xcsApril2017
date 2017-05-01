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
                doubleRow.append(float(value))

            # store the row into our matrix
            matrix.append(doubleRow)
    return matrix

priorMatrix = loadCsvData('prior.csv')
pMatrix = loadCsvData('conditional.csv')

pNewConditional = []
pNewSum = 0
for i in range(0,len(priorMatrix)):
    pNewConditionalRow = []
    for j in range(0,len(priorMatrix[0])):
        pNewConditionalRow.append( priorMatrix[i][j]*pMatrix[i][j])
        pNewSum = pNewSum + priorMatrix[i][j]*pMatrix[i][j]
    pNewConditional.append(pNewConditionalRow)
pNewConditionalArray = numpy.array(pNewConditional)
pNew = pNewConditionalArray/pNewSum
print(len(priorMatrix))
print(pNewConditional)
print(pNewConditionalArray)
print(pNew)
print(pNew.sum())
pNewList = pNew.tolist()
with open('cellPhoneResult.csv', 'w') as f:
    writer = csv.writer(f)
    for row in pNewList:
        print(row)
        writer.writerow(row)
