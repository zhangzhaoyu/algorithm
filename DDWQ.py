#! /usr/bin/env python

# author  zhangzhaoyu
# Date    2015-01-03
# Description:
# DDWQ is depended on QENNI(quadrant encapsidated nearest based imputation)
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
def wqenni_impl(iDataSet, cDataSet, coefficient, divisor) :
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

    p_choose = np.array([-1 for i in range(2 ** colNum)])
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

    #print "p_choose"
    #print p_choose
    #print "distance"
    #print len(distance)
    numOfEachQ = countNumOfEachQuadrant(p_choose, distance, cutDataSet, iDataSet)
    #print "numOfEachQ"
    #print numOfEachQ
    dist_weight = compute_dist_wight(p_choose, distance, colNum)
    #print "dis_weight"
    #print dist_weight
    volumeOfEachQ = compute_volume(p_choose, distance, colNum)
    #print "volumeOfEachQ"
    #print volumeOfEachQ
    resultData = imputationMissingData(p_choose, numOfEachQ, dist_weight, volumeOfEachQ, cDataSet, coefficient, divisor)
    #print "resultData"
    #print resultData
    return resultData, p_choose, dist_weight, numOfEachQ, volumeOfEachQ

# imputation missing data
# p_choose    : the selected point of each quadrant
# numOfEachQ  : number of point in each quadrant when r <= 2 min dist(Neari, center)
# dist_weight : weight of each nearest point
# volumeOfEachQ: volume of each quadrant where r = 2 min dist(Neari, center)
# coefficient : percentage of each weight
def imputationMissingData(p_choose, numOfEachQ, dist_weight, volumeOfEachQ, cDataSet, coefficient = -1.0, divisor = 10) :
    sumOfIndex = numOfEachQ.sum()
    sizeOfQ = len(dist_weight)

    tempA = 0.0
    tempB = 0.0
    for i in range(sizeOfQ) :
        if dist_weight[i] != 0.0 :
            cDataRow = cDataSet[p_choose[i]]
            # the decision attribute
            yData = cDataRow[-1]
            weightOfDensity = numOfEachQ[i] / (volumeOfEachQ[i] * (10.0 ** divisor))
            middle = 0.0
            print "coefficient is %s" %(coefficient)
            print "divisor is %d" %(divisor)
            if coefficient > -1.0 :
                middle = ((1.0 - coefficient) * dist_weight[i] + coefficient * weightOfDensity)
            else :
                print 'no coefficient'
                middle  = dist_weight[i] + weightOfDensity
            print "weight of distance : %f" %(dist_weight[i])
            print "middle weight : %f" %(middle)
            print "weight of density : %f" %(weightOfDensity)
            
            tempA += middle * yData
            tempB += middle
        #else :
           # print "i is %s, weight is %s" %(i, dist_weight[i])
    #print 'tempA %f' %(tempA)
    #print 'tempB %f' %(tempB)
    return tempA / tempB

# compute the distance wight
def compute_dist_wight(p_choose, distance, colNum) :
    sizeOfArray = 2 ** colNum
    dist_weight = np.array([0.0 for i in range(sizeOfArray)])

    for j in range(sizeOfArray) :
        if p_choose[j] != -1 :
            dist_weight[j] = 1.0 / (distance[p_choose[j]]) ** 2
    return dist_weight

# compute volume of each quadrant
def compute_volume(p_choose, distance, colNum) :
    sizeOfArray = 2 ** colNum
    volumeOfEachQ = np.array([0.0 for i in range(sizeOfArray)])
    for j in range(sizeOfArray) :
        if p_choose[j] != -1 :
            # 2.0 * dist as the radius
            radius = 2.0 * distance[p_choose[j]]
            # compute the volume of each quadrant of n-sphere
            volumeOfEachQ[j] = volumeOfnSphere(colNum, radius) / sizeOfArray

    return volumeOfEachQ

# count number of every quadrant
def countNumOfEachQuadrant(p_choose, distance, cutDataSet, center, timesOfr = 2.0) :
    rowNum = cutDataSet.shape[0]
    colNum = cutDataSet.shape[1]
    # number of index in each quadrant
    numOfEachQuadrant = np.array([0 for i in range(2 ** colNum)])
    for j in range(rowNum) :
        cRowData = cutDataSet[j, :]
        # index of quadrant
        quadrantIndex = quadrantOfIndex(cRowData, center)
        euclidDist = distance[j]

        # euclidDist < 2r
        if (p_choose[quadrantIndex] != -1 and euclidDist < distance[p_choose[quadrantIndex]] * timesOfr) :
            numOfEachQuadrant[quadrantIndex] += 1
    return numOfEachQuadrant

# compute the volume of n-sphere
def volumeOfnSphere(nDimension, radius) :
    param = nDimension / 2.0 + 1.0
    resultOfGamma = math.gamma(param)
    #print "result of gamma : %s" %(resultOfGamma)
    volumeTemp = (math.pi ** (nDimension / 2.0)) * (radius ** nDimension)
    #print "valume of temp : %s" %(volumeTemp)
    volume = volumeTemp / resultOfGamma
    return volume

if __name__ == '__main__' :
    iDataSet, cDataSet = createDataSet()
    colNum = cDataSet.shape[1]
    resultData, p_choose, dist_weight, numOfEachQuadrant, volumeOfEachQ  = wqenni_impl(iDataSet, cDataSet)
    print 'the nearest index of each quadrant :'
    print p_choose
    print '\nthe wight of each nearest index :'
    print dist_weight
    print '\nnumber of index in the 2r circle of earch quadrant :'
    print numOfEachQuadrant
    print '\nmissing data is : %f' %(resultData)
    print "\nvolume of each quadrant :"
    print volumeOfEachQ

    volume = volumeOfnSphere(3, 1.0)
    print "\nvolume is (3 dimension, 1.0 radius) %s " %(volume)
