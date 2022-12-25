#! /usr/bin/python3

import sys
from os import listdir
import numpy as np
import operator

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        sortedClassCount = sorted(classCount.items(), key= operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def imgToVector(filename):
    returnVect = np.zeros((1, 1024))
    with open(filename) as fp:
        for i in range(32):
            lineStr = fp.readline()
            for j in range(32):
                returnVect[0, 32 * i + j] = int(lineStr[j])
        return returnVect
    
def hwClassifier(trainingDigits, testDigits):
    labels = []
    trainingFileList = listdir(trainingDigits)
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))
    
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        labels.append(classNumStr)
        trainingMat[i, :] = imgToVector(trainingDigits + '/' + fileNameStr)
    
    #trainingMat, labels
    testFileList = listdir(testDigits)
    n = len(testFileList)
    for k in range(1, 21):
        errorCnt = 0; cnt = 0
        for i in range(n):
            classNumStr = int(testFileList[i].split('_')[0])
            testData = imgToVector(testDigits + '/' + testFileList[i])
            classifierResult = classify0(testData, trainingMat, labels, k)
            cnt += 1
            if classNumStr != classifierResult:
                errorCnt += 1
        print(int(errorCnt / cnt * 100))

trainingDigits = sys.argv[1]    #trainingDigits
testDigits = sys.argv[2]        #testDigits
hwClassifier(trainingDigits, testDigits)
