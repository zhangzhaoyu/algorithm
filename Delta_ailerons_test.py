#! /usr/bin/env python

# Test the data set of Delta_ailerons by algorithm QENNI and WWDQ
# show the result by matplotlib
import numpy as np
import DataFilter as df
import DDWQ as DDWQ

def test_DDWQ_onDeltaAilerons() :
    deltaDataList = df.dataOfDeltaAilerons()
    completeDataSet, incompleteDataSet = df.createRandomCompleteAndIncompleteDataSet(deltaDataList)
    lenghtOfincompleteData = len(incompleteDataSet)

    i = 0
    for iDataSet in incompleteDataSet :
        i += 1
        resultData, p_phoose, dist_weight, numOfEachQ, volumeOfEachQ = DDWQ.wqenni_impl(np.array(iDataSet[:-1]), np.array(completeDataSet))
        #print "the result is " + resultData
        print resultData
        print "total times %d" %(i)
if __name__ == "__main__" :
    test_DDWQ_onDeltaAilerons()
