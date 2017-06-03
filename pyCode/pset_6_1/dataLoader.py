
class dataSet(object):
    def __init__(self):
        self.filename = ""
        self.dataTable = []
        self.rowNum = 0
        self.inputNum = 0
        self.lines = []
        self.rowInputStr = []
        self.rowOutputStr = []
        self.rowInputList = []
        self.rowOutputList = []

    def loadFile(self, filename):
        self.filename = filename
        with open(filename) as f:
            self.lines = f.readlines()
            self.inputNum = int(self.lines[0])
            self.rowNum = int(self.lines[1])
            for i in range(2, self.rowNum+2):
                rowStrList = self.lines[i].split(":")

                self.rowInputStr.append(rowStrList[0] )
                self.rowOutputStr.append(rowStrList[1])
                rowInputStrList = rowStrList[0].split()
                rowOutputStrList = rowStrList[1].split()
                rowInputFloatList = []
                rowOutputFloatList = []
                for j in rowInputStrList:
                    rowInputFloatList.append(float(j))
                for j in rowOutputStrList:
                    rowOutputFloatList.append(float(j))


                self.rowInputList.append(rowInputFloatList)
                self.rowOutputList.append(rowOutputFloatList)





    def printFilename(self):
        print(self.filename)
