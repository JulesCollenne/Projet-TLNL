import numpy as np


class FeatModel:
    def __init__(self, featModFilename, dicos):
        self.featArray = self.readFeatModelFile(featModFilename)
        self.inputVectorSize = self.computeInputSize(dicos)

    def readFeatModelFile(self, featModFilename):
        try:
            featModFile = open(featModFilename, encoding='utf-8')
        except IOError:
            print(featModFilename, " : ce fichier n'existe pas")
            exit(1)
        featArray = []
        for ligne in featModFile:
            splitted = ligne.split()
            if len(splitted) == 4:
                (featType, container, position, wordFeature) = splitted
                # print("type =", featType, "container = ", container, "position = ", position, "wordFeature = ", wordFeature)
                if featType == 'W':
                    if container != "B" and container != "S":
                        print("error while reading featMod file : ", featModFilename, "container :", container,
                              "undefined")
                        exit(1)
                    if not wordFeature in {'POS', 'LEMMA', 'FORM'}:
                        print("error while reading featMod file : ", featModFilename, "wordFeature :", wordFeature,
                              "undefined")
                        exit(1)
                    featArray.append((featType, container, int(position), wordFeature))
            if len(splitted) == 6:
                (featType, feature, container1, position1, container2, position2) = splitted
                if featType == 'C':
                    if feature not in {'DIST', 'NLDEP', 'NRDEP', 'LLDEP', 'LRDEP', 'SH'}:
                        print("error while reading featMod file : ", featModFilename, "feature :", feature, "undefined")
                        exit(1)
                    if container1 != "B" and container1 != "S":
                        print("error while reading featMod file : ", featModFilename, "container :", container,
                              "undefined")
                        exit(1)
                    if container2 != "B" and container2 != "S":
                        print("error while reading featMod file : ", featModFilename, "container :", container,
                              "undefined")
                        exit(1)
                    featArray.append((featType, feature, container1, int(position1), container2, int(position2)))
        featModFile.close()
        return featArray

    def computeInputSize(self, dicos):
        inputVectorSize = 0
        for featTuple in self.getFeatArray():
            feat = featTuple[3]
            if dicos.getDico(feat) is not None:
                inputVectorSize += dicos.getDico(feat).getSize()
        return inputVectorSize

    def getInputSize(self):
        return self.inputVectorSize

    def getNbFeat(self):
        return len(self.featArray)

    def getFeatArray(self):
        return self.featArray

    def getFeatType(self, featIndex):
        return self.featArray[featIndex][0]

    def getFeatContainer(self, featIndex):
        return self.featArray[featIndex][1]

    def getFeatPosition(self, featIndex):
        return self.featArray[featIndex][2]

    def getFeatLabel(self, featIndex):
        return self.featArray[featIndex][3]

    def buildInputVector(self, featVec, dicos):
        inputVector = np.zeros(self.inputVectorSize, dtype="int32")
        origin = 0
        for i in range(self.getNbFeat()):
            label = self.getFeatLabel(i)
            if dicos.getDico(label) is not None:
                size = dicos.getDico(label).getSize()
                position = dicos.getCode(label, featVec[i])
                # print('featureName = ', featureName, 'value =', featVec[i], 'size =', size, 'position =', position,
                # 'origin =', origin)
                inputVector[origin + position] = 1
                origin += size
        return inputVector
