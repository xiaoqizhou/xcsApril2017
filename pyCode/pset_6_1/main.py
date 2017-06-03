import dataLoader as dl
import MLETrainer as mt

dataSet_1 = dl.dataSet()
dataSet_1.loadFile("simple-train.txt")

trainer_MLE = mt.MLETrainer()
trainer_MLE.loadDataSet(dataSet_1)


dataSet_1.printFilename()
