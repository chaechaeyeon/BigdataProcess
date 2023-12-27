import numpy as np
import sys

from os import listdir
import operator


def createDataSet(dir):
    trainList = listdir(dir)
    length = len(trainList)

    matrix = np.zeros((length, 1024))
    labels = []

    for i in range(length):
        filenames= trainList[i]

        ans= int(filenames.split('_')[0]) 
        labels.append(ans)
        matrix[i, :] = getVector(dir + '/' + filenames)
    return matrix, labels 


def classify0(inX, dataSet, labels, k):

    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet

    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances**0.5

    sortedDistIndicies = distances.argsort()
    classCnt = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCnt[voteIlabel] = classCnt.get(voteIlabel,0) + 1

    sortedClassCount = sorted(classCnt.items(),key= operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]


def getVector(file):
    vector = np.zeros((1, 1024))
    with open(file) as fp:
        for i in range(32):
            line =fp.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line[j])
        return vector        


if __name__ == "__main__":
    trainingDir = "trainingDigits"
    testDir = "testDigits"

    testFileList = listdir(testDir)
    length = len(testFileList)

    matrix, labels = createDataSet(trainingDir)

    for k in range(1, 21):
        count = 0 
        errorCnt = 0
        for i in range(length):
            answer = int(testFileList[i].split('_')[0])
        
            testData = getVector(testDir + '/' + testFileList[i])

            result = classify0(testData, matrix, labels, k)

            count += 1
            if answer != result:
                errorCnt += 1
    
        print(int(errorCnt / count * 100))