#! /usr/bin/env python

# author  zhangzhaoyu
# Date    2015-01-03
# Description:
# K nearest neighbors imputation algorithm
#
#
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math as math

def createDataSet() :
    iDataSet = np.array([0, 0])
    cDataSet = np.array([
        [1, 1, 1],
        [1, 2, 1],
        [2, 1, 1],
        [-2, 1, 1],
        [-1, -1, 2.5],
        [-2, -1, 1.5],
        [2, -1, 3]
    ])
    return iDataSet, cDataSet

# iDataSet : incomplete data record
# cDataSet : complete data set
def knni_impl(iDataSet, cDataSet, k) :
    # cut the last column of the data
    cutDataSet = cDataSet[:, 0:cDataSet.shape[1] - 1]
    rowNum = cutDataSet.shape[0]
    colNum = cutDataSet.shape[1]
    #print "\ncut data set shape :"
    #print cutDataSet.shape

    diffiDataSet = np.tile(iDataSet, (rowNum, 1)) - cutDataSet
    sqDiffMat = diffiDataSet ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances ** 0.5
    #print "distance"
    #print distance
    # index of euclid distance
    sortedEuclidDist = distance.argsort()

    #print "sortedEuclidDist :"
    #print sortedEuclidDist

    resultData = imputationMissingData(distance,sortedEuclidDist, cDataSet, k)
    #print "resultData"
    #print resultData
    return resultData

# imputation missing data
# distance    : the distance of each point to the center
# sortedEuclidDist  : sorted distance index
# cDataSet :
# k : the k
def imputationMissingData(distance, sortedEuclidDist, cDataSet, k = 5) :

    tempA = 0.0
    tempB = 0.0
    for i in range(k) :
        cDataRow = cDataSet[sortedEuclidDist[i]]
        yData = cDataRow[-1]
        # compute the weight
        data_weight = 1.0 / (distance[sortedEuclidDist[i]] ** 2)
        tempA += data_weight * yData
        tempB += data_weight

    #print 'tempA %f' %(tempA)
    #print 'tempB %f' %(tempB)
    return tempA / tempB

if __name__ == '__main__' :
    iDataSet, cDataSet = createDataSet()
    colNum = cDataSet.shape[1]
    data = knni_impl(iDataSet, cDataSet)
    print "the imputation result : %f" %(data)
