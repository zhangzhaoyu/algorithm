#! /usr/bin/env python

# Author    zhangzhaoyu
# Date      2015-01-24
# Description:
# To filter the abalone.data. The sex attribute is excluded and left the data
# whose sex value is M. The third attribute diameter is chosen as decision attribute.
# fetch the the test data
#
import random as random

# get the Abalone data set into a python List
# return the data List
def dataFilterOfAbalone(fileName, destFileName) :
    fr = open(fileName)
    fw = open(destFileName, "w+");
    returnMat = []
    for line in fr :
        positionIndex = line.index(",")
        # tempLine = line[positionIndex + 1:]
        attrArray = line.strip("\n").split(",")
        # choose attribute value 'M'
        if attrArray[0] == 'M' :
            tempAttrArr = attrArray[1:]
            # move the desision attr to the last
            lengthOfArr = len(tempAttrArr)
            tempAttrValue = tempAttrArr[lengthOfArr-1]
            tempAttrArr[lengthOfArr-1] = tempAttrArr[1]
            tempAttrArr[1] = tempAttrValue
            # convert to string, join ","
            resultLine = ",".join(tempAttrArr)
            returnMat.append(tempAttrArr)
            fw.write(resultLine + "\n")
            #print tempLine.strip("\n")
    fr.close()
    fw.close()
    return returnMat

# get the Delta_Ailerons data into a python List from data file
# return the data List
def dataOfDeltaAilerons(fileName = "delta_ailerons.data") :
    fr = open(fileName)
    returnMat = []
    for line in fr :
        attrArray = line.strip("\n").split(" ")
        temp = [float(val) for val in attrArray]
        returnMat.append(temp)

    fr.close()
    return returnMat

def dataOfAbalone(fileName = "abalone_filtered.data") :
    fr = open(fileName)
    returnMat = []
    for line in fr :
        attrArray = line.strip("\n").split(",")
        temp = [float(val) for val in attrArray]
        returnMat.append(temp)

    fr.close()
    return returnMat


# random generate the complete data and incomplete data from the full data
# the default percentage of incomplete data is 0.05
def createRandomCompleteAndIncompleteDataSet(fullDataSet, percentage = 0.05) :
    sizeOfData = len(fullDataSet)
    sizeOfincompleteData = int(sizeOfData * percentage)
    dataIndex = range(sizeOfData)

    indexOfrandomincompleteData = random.sample(dataIndex, sizeOfincompleteData)
    completeDataSet = []
    incompleteDataSet = []

    for i in dataIndex :
        index = findIndex(indexOfrandomincompleteData, i)
        if index == -1 :
            completeDataSet.append(fullDataSet[i])
        else :
            incompleteDataSet.append(fullDataSet[i])
    return completeDataSet, incompleteDataSet


# find the index of the  value in L
# if find, return the index
# else return -1
def findIndex(L, value) :
    index = -1
    try :
        index = L.index(value)
    except :
        index = -1
    return index

if __name__ == "__main__" :
    resultMat = dataFilterOfAbalone("data/abalone.data", "abalone_filtered.data")
    print "abalone data's length is %d" %(len(resultMat))

    completeDataSet, incompleteDataSet = createRandomCompleteAndIncompleteDataSet(resultMat)
    print "length of complete Data Set is %s" %(len(completeDataSet))
    print "length of incomplete Data Set is %s" %(len(incompleteDataSet))

    resultMat = dataOfDeltaAilerons()
    print "delta_ailerons data's length is %d" %(len(resultMat))
    completeDataSet, incompleteDataSet = createRandomCompleteAndIncompleteDataSet(resultMat)
    print "length of complete Data Set is %s" %(len(completeDataSet))
    print "length of incomplete Data Set is %s" %(len(incompleteDataSet))
