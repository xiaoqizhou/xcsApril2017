import dataLoader as dl
import MLETrainer as mt
import LaplaceTrainer as lt
import logRegTrainer as lr

dataSet_1 = dl.dataSet()
dataSet_1.loadFile("heart-train.txt")
dataSet_2 = dl.dataSet()
dataSet_2.loadFile("heart-test.txt")

trainer_MLE = mt.MLETrainer()
trainer_MLE.loadTrainDataSet(dataSet_1)
trainer_MLE.loadTestDataSet(dataSet_2)
trainer_MLE.printPY(1)
for i in range(0, dataSet_2.inputNum):
    trainer_MLE.printPx_y(i, 1, 1)
for i in range(0, dataSet_2.inputNum):
    trainer_MLE.printPx_y(i, 1, 0)
trainer_MLE.printAccuracy()
trainer_Laplace= lt.LaplaceTrainer()
trainer_Laplace.loadTrainDataSet(dataSet_1)
trainer_Laplace.loadTestDataSet(dataSet_2)
trainer_Laplace.printPY(1)
for i in range(0, dataSet_2.inputNum):
    trainer_Laplace.printPx_y(i, 1, 1)
for i in range(0, dataSet_2.inputNum):
    trainer_Laplace.printPx_y(i, 1, 0)
trainer_Laplace.printAccuracy()
t_diff = trainer_MLE.ty - trainer_Laplace.ty

for i in range(0, dataSet_2.inputNum):
    print("%d & %.3f & %.3f & %.3f & %.3f \\\\"%(i, trainer_MLE.px_y[i][1][0],trainer_MLE.px_y[i][1][1],trainer_Laplace.px_y[i][1][0],trainer_Laplace.px_y[i][1][1]))
trainer_MLE.printR()

for i in range(0, dataSet_2.inputNum):
    print("%d & %.3f"%(i, trainer_MLE.r[i]))


trainer_logReg = lr.logRegTrainer()
trainer_logReg.loadTrainDataSet(dataSet_1)
trainer_logReg.loadTestDataSet(dataSet_2)
trainer_logReg.printAccuracy()

trainer_logReg.printTheta()
trainer_logReg.printLL(dataSet_2)
print("Finished.")
