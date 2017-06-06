# Logistic Regression Trainer
import numpy
class logRegTrainer(object):
    def __init__(self):
        # Define step length and iteration numbers
        self.eta = 0.0025
        self.iteration = 10000
    def sigmoid(self, x):
        return 1/(1 + numpy.exp(-x))

    def loadTrainDataSet(self, inputData):
        self.theta = numpy.zeros((inputData.inputNum+1))
        self.devLL = numpy.zeros((inputData.inputNum+1))
        for i in range (0, self.iteration):
            self.devLL = numpy.zeros((inputData.inputNum + 1))
            if i%100 == 0:
                print("Iteration #%d"%(i))

            for k in range (0, inputData.rowNum):
                # Calculate devLL
                x_now =numpy.append(numpy.array([1]), inputData.rowInputList[k])
                self.devLL += (inputData.rowOutputList[k] - self.sigmoid(numpy.sum(x_now*self.theta)))*x_now
            # Move one step
            self.theta += self.eta*self.devLL



    def loadTestDataSet(self, testData):
        self.py = numpy.zeros(testData.rowNum)
        self.ty = numpy.zeros(testData.rowNum)
        self.correct = 0
        self.correctRate = float(0)
        for i in range(0, len(testData.rowInputList)):
            x_now = numpy.append(numpy.array([1]), testData.rowInputList[i])
            # Calculate P(Y = 1|X) based on current row of data
            self.py[i] = self.sigmoid(numpy.sum(x_now* self.theta))

            if self.py[i] > 0.5:
                    self.ty[i] = 1
            else:
                    self.ty[i] = 0
            if self.ty[i] == testData.rowOutputList[i][0]:
                    self.correct += 1

        self.correctRate = self.correct / float(testData.rowNum)


    def printAccuracy(self):
        print("Logistic: Accuracy = %f"%(self.correctRate))

    def printTheta(self):
        index = 0
        for i in (self.theta):
            print("Logistic Regression: theta[%d] = %f"%(index, i))
            index += 1

    def printLL(self, inputData):
        self.LL = 0
        self.LL0 = 0
        for k in range(0, inputData.rowNum):
            x_now = numpy.append(numpy.array([1]), inputData.rowInputList[k])
            y = inputData.rowOutputList[k][0]
            s = self.sigmoid(numpy.sum(x_now * self.theta))
            s0 = self.sigmoid(0)
            self.LL += (y*numpy.log(s))+(1-y)*numpy.log(1-s)
            self.LL0 += (y * numpy.log(s0)) + (1 - y) * numpy.log(1 - s0)
        print("LL = %f"%(self.LL))
        print("LL0 = %f" % (self.LL0))




