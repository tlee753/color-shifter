from PIL import Image
import numpy

class Shifter:
    def __init__(self, fileName, numSplits = 8, color1 = "#c0b283", color2 = "#f4f4f4"): # dark then light to match
        self.fileName = fileName
        self.numSplits = numSplits
        self.color1 = color1.replace("#", "")
        self.color2 = color2.replace("#", "")
        self.img = Image.open(fileName).convert('L')
        self.arr = numpy.array(self.img)
        self.dual = numpy.zeros((self.arr.shape[0], self.arr.shape[1], 3), dtype=numpy.uint8)
        self.splits = [(0,0,0)] * self.numSplits
        print("Shifter running...")

    def convertRGB(self):
        self.color1RGB = (int(self.color1[0:2], 16), int(self.color1[2:4], 16), int(self.color1[4:6], 16))
        # print(self.color1RGB)
        self.color2RGB = (int(self.color2[0:2], 16), int(self.color2[2:4], 16), int(self.color2[4:6], 16))
        # print(self.color2RGB)

    def createSplits(self):
        redSplits = numpy.linspace(self.color1RGB[0], self.color2RGB[0], self.numSplits)
        redSplits = [int(i) for i in redSplits]
        greSplits = numpy.linspace(self.color1RGB[1], self.color2RGB[1], self.numSplits)
        greSplits = [int(i) for i in greSplits]
        bluSplits = numpy.linspace(self.color1RGB[2], self.color2RGB[2], self.numSplits)
        bluSplits = [int(i) for i in bluSplits]
        for i in range(self.numSplits):
            self.splits[i] = (redSplits[i], greSplits[i], bluSplits[i])
        # print(self.splits)

    def dualTone(self):
        increment = int(255 / self.numSplits)
        indexes = [0] * self.numSplits
        for i in range(self.numSplits):
            indexes[i] = increment * i
        # print(indexes)

        for i in range(int(self.arr.shape[0])):
            for j in range(self.arr.shape[1]):
                self.arr[i, j] = int(self.arr[i, j] / increment) * increment # round into splits

                # edge case, might not exist
                if self.arr[i, j] == increment * self.numSplits:
                    self.arr[i, j] = increment * (self.numSplits - 1)

                self.dual[i, j, 0] = self.splits[indexes.index(self.arr[i, j])][0]
                self.dual[i, j, 1] = self.splits[indexes.index(self.arr[i, j])][1]
                self.dual[i, j, 2] = self.splits[indexes.index(self.arr[i, j])][2]

    def createImage(self):
        Image.fromarray(self.dual, 'RGB').save(self.fileName[:-4] + "-shifted.jpg")

    def run(self):
        self.convertRGB()
        self.createSplits()
        self.dualTone()
        self.createImage()

sh = Shifter("headshot.jpg")
sh.run()
