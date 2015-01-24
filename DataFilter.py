#! /usr/bin/env python

# Author    zhangzhaoyu
# Date      2015-01-24
# Description:
# To filter the abalone.data. The sex attribute is excluded and left the data
# whose sex value is M. The third attribute diameter is chosen as decision attribute.

def dataFilter(fileName, destFileName) :
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

if __name__ == "__main__" :
    resultMat = dataFilter("data/abalone.data", "abalone_filtered.data");

    for item in resultMat :
        print item
    print "length of resultMat is %d" %(len(resultMat))
