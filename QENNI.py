#! /usr/bin/python

# author  zhangzhaoyu
# Date    2015-01-03
# Description:
# WQENNI is depended on QENNI(quadrant encapsidated nearest based imputation)
#
#
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

def createDataSet() : 
    iDataSet = array([0, 0])
    cDataSet = array([
        [1, 1, 1],
        [1, 2, 1],
        [2, 1, 1],
        [-2, 1, 1],
        [-1, -1, 2.5],
        [-2, -1, 1.5],
        [2, -1, 3]
    ])
    return iDataSet, cDataSet

# compute the quadrant of the target index
def quadrantOfIndex(target, center) :
    colNum = len(center)
    charArr = 0
    for i in range(colNum) :
        if (target[i] - center[i]) >= 0 :
            charArr += 1 * (2 ** (colNum - i -1))
        else :
            charArr += 0 * (2 ** (colNum -i -1))
    return charArr
    

# iDataSet : incomplete data record
# cDataSet : complete data set
def qenni_impl(iDataSet, cDataSet) :
    # cut the last column of the data
    cutDataSet = cDataSet[:, 0:cDataSet.shape[1] - 1]
    
    rowNum = cutDataSet.shape[0]
    colNum = cutDataSet.shape[1]
    diffiDataSet = tile(iDataSet, (rowNum, 1)) - cutDataSet
    sqDiffMat = diffiDataSet ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances ** 0.5
    # index of euclid distance
    sortedEuclidDist = distance.argsort()

    p_choose = array([-1 for i in range(2 ** colNum)])
    for k in range(rowNum) :
        cRowData = cutDataSet[k, :]
        quadrantIndex = quadrantOfIndex(cRowData, iDataSet)

        if (p_choose[quadrantIndex] != -1 and p_choose[quadrantIndex] != k ) :
            min_dist = distance[p_choose[quadrantIndex]]
            k_dist = distance[k]
            if k_dist < min_dist :
                p_choose[quadrantIndex] = k
        else :
            p_choose[quadrantIndex] = k

    numOfEachQ = countNumOfEachQuadrant(p_choose, distance, cutDataSet, iDataSet)
    dist_weight = compute_dist_wight(p_choose, distance, colNum)
    resultData = imputationMissingData(p_choose, numOfEachQ, dist_weight, cDataSet)
    return resultData, p_choose, dist_weight, numOfEachQ

# imputation missing data
def imputationMissingData(p_choose, numOfEachQ, dist_weight, cDataSet, coefficient = 0.5) :
    sumOfIndex = numOfEachQ.sum()
    sizeOfQ = len(dist_weight)

    tempA = 0.0
    tempB = 0.0
    for i in range(sizeOfQ) :
        cDataRow = cDataSet[p_choose[i]]
        # the decision attribute
        yData = cDataRow[-1]
        tempA += ((1.0 - coefficient) * dist_weight[i] + coefficient * numOfEachQ[i] / sumOfIndex) * yData
        tempB += ((1.0 - coefficient) * dist_weight[i] + coefficient * numOfEachQ[i] / sumOfIndex)
    #print 'tempA %f' %(tempA)
    #print 'tempB %f' %(tempB)
    return tempA / tempB

# compute the distance wight
def compute_dist_wight(p_choose, distance, colNum) :
    dist_weight = array([0.0 for i in range(2 ** colNum)])

    for j in range(2 ** colNum) :
        if p_choose[j] != -1 :
            dist_weight[j] = 1.0 / (distance[p_choose[j]]) ** 2
    return dist_weight

# cout number of every quadrant
def countNumOfEachQuadrant(p_choose, distance, cutDataSet, center, timesOfr = 2) :
    rowNum = cutDataSet.shape[0]
    colNum = cutDataSet.shape[1]
    # number of index in each quadrant
    numOfEachQuadrant = array([0 for i in range(2 ** colNum)])
    for j in range(rowNum) :
        cRowData = cutDataSet[j, :]
        # index of quadrant
        quadrantIndex = quadrantOfIndex(cRowData, center)
        euclidDist = distance[j]
        
        # euclidDist < 2r
        if (p_choose[quadrantIndex] != -1 and euclidDist < distance[p_choose[quadrantIndex]] * timesOfr) :
            numOfEachQuadrant[quadrantIndex] += 1
    return numOfEachQuadrant

if __name__ == '__main__' :
    iDataSet, cDataSet = createDataSet()
    colNum = cDataSet.shape[1]
    resultData, p_choose, dist_weight, numOfEachQuadrant = qenni_impl(iDataSet, cDataSet)
    print 'the nearest index of each quadrant :'
    print p_choose
    print '\nthe wight of each nearest index :'
    print dist_weight
    print '\nnumber of index in the 2r circle of earch quadrant :'
    print numOfEachQuadrant
    print '\nmissing data is : %f' %(resultData) 

