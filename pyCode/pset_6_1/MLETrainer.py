class MLETrainer(object):
    def __init__(self):
        p = []
        xNum = 0
        yNum = 0
    def loadDataSet(self, inputData):
        self.p = [[[0,0],[0,0]]]*inputData.inputNum
        for i in range(0,len(inputData.rowInputList)):
            for j in range(0,len(inputData.rowInputList[i])):
                for k in range(0, len(inputData.rowOutputList[i])):
                    self.p[j][int(inputData.rowInputList[i][j])][int(inputData.rowOutputList[i][k])] += 1


