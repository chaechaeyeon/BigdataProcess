#!/usr/bin/python3


import sys
import numpy as np

import os
import operator

def createDataSet(dir):
    
    t_fileList = os.listdir(dir)
    m = len(t_fileList)
    matrix =np.zeros((m,1024))
    labels=[]
    for i in range(m):
        files= t_fileList[i]
        featVex = int(files.split('_')[0])
        labels.append(featVex)
        matrix[i, :] = getVector(dir + '/' + files)
    return matrix, labels

def classify0(inX, dataSet, labels, k):
    
    dataSize=dataSet.shape[0]
    diffMat = np.title(inX,(dataSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistIndices=distances.argsort()
    classCount={}
    for i in range(k):
        voteLabel=labels[sortedDistIndices[i]]
        classCount[voteLabel]=classCount.get(voteLabel,0)+1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
def authNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals#범위
    normDataSet=np.zeros(np.shape(dataSet))
    m = dataSet.Shape[0]
    normDataSet=dataSet-np.title(minVals,(m,1))
    normDataSet = normDataSet/np.tile(ranges,(m,1))
    return normDataSet,ranges,minVals

def getVector(name):
	vec = np.zeros((1,1024))
	with open(name) as fp:
		for i in range(32):
			line = fp.readline()
			for j in range(32):
				vec[0,32 * i + j] = int(line[j])
		return vec
      
trainingFileName = sys.argv[1]
testFileName = sys.argv[2]

matrix,labels = createDataSet(trainingFileName)
fileList = os.listdir(testFileName)
length = len(fileList)

for k in range(1, 21):
	error = 0
	cnt = 0

	for i in range(length):
		ans = int(list[i].split('_')[0])
		testData = getVector(testFileName + '/' + fileList[i])
		classifiedResult = classify0(testData, matrix, labels, k)
		cnt += 1

		if ans != classifiedResult:
			error += 1
	print(int(error / cnt * 100)) 