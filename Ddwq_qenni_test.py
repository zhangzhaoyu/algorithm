#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import DataFilter as df
import DDWQ as DDWQ
import QENNI as QENNI

def test_DDWQ_QENNI(coefficient) :
    #deltaDataList = df.dataOfDeltaAilerons()
    deltaDataList = df.dataOfAbalone()
    completeDataSet, incompleteDataSet = df.createRandomCompleteAndIncompleteDataSet(deltaDataList)
    lenghtOfincompleteData = len(incompleteDataSet)

    impute_data_result = []
    for iDataSet in incompleteDataSet :
        resultData, p_phoose, dist_weight, numOfEachQ, volumeOfEachQ = DDWQ.wqenni_impl(np.array(iDataSet[:-1]), np.array(completeDataSet), coefficient)
        #print "the result is " + resultData
        impute_data_result.append(resultData)
        print resultData
        # print "total times %d" %(i)

    # compute the RMSE
    m = len(impute_data_result)
    sum = 0.0
    for j in range(m) :
        sum += abs(incompleteDataSet[j][-1] - impute_data_result[j])
    ddwq_rmse = sum / m
    #print "sum is %f, m is %d " %(sum, m)
    #print "the ddwq rmse is %f" %(rmse)

    qenni_impute_data_result = []
    for iDataSet in incompleteDataSet :
        resultData, p_phoose, dist_weight, numOfEachQ, volumeOfEachQ = QENNI.qenni_impl(np.array(iDataSet[:-1]), np.array(completeDataSet))
        #print "the result is " + resultData
        qenni_impute_data_result.append(resultData)
        print resultData
        # print "total times %d" %(i)

    # compute the RMSE
    m = len(qenni_impute_data_result)
    sum = 0.0
    for i in range(m) :
        sum += abs(incompleteDataSet[i][-1] - qenni_impute_data_result[i])
    qenni_rmse = sum / m
    #print "sum is %f, m is %d " %(sum, m)
    #print "the ddwq rmse is %f" %(rmse)
    return ddwq_rmse, qenni_rmse

if __name__ == "__main__" :
    ddwq_data, qenni_data = test_DDWQ_QENNI(0.1)
    print "ddwq is " 
    print ddwq_data
    print "qenni is"
    print qenni_data
