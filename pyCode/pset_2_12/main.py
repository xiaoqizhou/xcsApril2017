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
                if value.upper() == 'TRUE':
                    doubleRow.append(1)
                else:
                    doubleRow.append(0)

            # store the row into our matrix
            matrix.append(doubleRow)
    return matrix
batMatrix = loadCsvData('bats.csv')
batArray = numpy.array(batMatrix)
geneIndexRange = range(5)
traitIndexRange = 5
totalItems = batArray.shape[0]
print(totalItems)
traitP = float(batArray[:, traitIndexRange].sum())/totalItems
print('Trait express P(T) = ')
print(float(traitP)/totalItems)
GP=[0]*5
GTP = [0]*5
GPTP = [0]*5
T_GP = [0]*5
for i in range(0,5):
    GP[i] = float(batArray[:, i].sum())/totalItems
    GTP[i] = float((batArray[:, i]*batArray[:, 5]).sum())/totalItems
    GPTP[i] = GP[i]*traitP
    T_GP[i] = GTP[i]/GP[i]

G5G3G4 = float((batArray[:, 2]*batArray[:, 3]*batArray[:, 4]).sum())/totalItems
G3G4 = float((batArray[:, 2]*batArray[:, 3]).sum())/totalItems
G5_G3G4 = G5G3G4/G3G4
G3G4_G5 = G5G3G4/GP[4]
TG5c = float((abs(batArray[:, 5]-1)*batArray[:, 4]).sum())/totalItems
TcG5 = float((batArray[:, 5]*abs(batArray[:, 4]-1)).sum())/totalItems
G5c = 1-GP[4]
T_G5c = TG5c/G5c
Tc_G5 = TcG5/GP[4]
print('GP List')
print(GP)
print('GTP List')
print(GTP)
print('GPTP List')
print(GPTP)
print('T_GP List')
print(T_GP)
print('G5_G3G4')
print(G5_G3G4)
print('G3G4_G5')
print(G3G4_G5)
print('T_G5c')
print(T_G5c)
print('G3*G4')
print(GP[2]*GP[3])
print('G3G4')
print(G3G4)
print('Tc_G5')
print(Tc_G5)