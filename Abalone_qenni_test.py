#! /usr/bin/env python

# Test the data set of Abalone by algorithm QENNI and WWDQ
# show the result by matplotlib
import numpy as np
import DataFilter as df
import QENNI as QENNI

def test_QENNI_onAbalone() :
    print "**************in qenni test***********"
    deltaDataList = df.dataOfAbalone()
    completeDataSet, incompleteDataSet = df.createRandomCompleteAndIncompleteDataSet(deltaDataList)
    lenghtOfincompleteData = len(incompleteDataSet)

    impute_data_result = []
    for iDataSet in incompleteDataSet :
        resultData, p_phoose, dist_weight, numOfEachQ, volumeOfEachQ = QENNI.qenni_impl(np.array(iDataSet[:-1]), np.array(completeDataSet))
        #print "the result is " + resultData
        impute_data_result.append(resultData)
        print resultData
       # print "total times %d" %(i)

    # compute the RMSE
    m = len(impute_data_result)
    sum = 0.0
    for j in range(m) :
        sum += abs(incompleteDataSet[j][-1] - impute_data_result[j])
    qenni_rmse = sum / m
    #print "sum is %f, m is %d " %(sum, m)
    #print "the qenni rmse is %f" %(rmse)
    return qenni_rmse

if __name__ == "__main__" :
    test_size = 100
    fw = open("result/abalone/qenni/qenni_rmse_result_" + str(test_size)+ "_new.data", "w+")
    qenni_sum = 0.0
    qenni_result = []
    for j in range(test_size) :
        qenni_rmse = test_QENNI_onAbalone()
        qenni_result.append(qenni_rmse)
        print "rmse is "
        print str(qenni_rmse)
        fw.write(str(qenni_rmse) + "\n")
        qenni_sum += qenni_rmse

    qenni_average_rmse = qenni_sum / test_size
    print "average rmse is"
    print str(qenni_average_rmse)
    fw.write(str(qenni_average_rmse) + "\n")
    fw.close()
