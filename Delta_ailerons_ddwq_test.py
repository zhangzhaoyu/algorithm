#! /usr/bin/env python

# Test the data set of Delta_ailerons by algorithm QENNI and WWDQ
# show the result by matplotlib
import numpy as np
import matplotlib.pyplot as plt
import DataFilter as df
import DDWQ as DDWQ
import QENNI as QENNI

def test_DDWQ_onDeltaAilerons(coefficient) :
    print "**************in ddwq test***********"
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
    return ddwq_rmse

def test_QENNI_onDeltaAilerons() :
    print "**************in qenni test***********"
    deltaDataList = df.dataOfDeltaAilerons()
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
    #coefficient = 0.5
    coe_arr = [0.1]
    for coefficient in coe_arr :
        #fw = open("result/ddwq/ddwq_rmse_result_"+ str(test_size) + "_" + str(coefficient) + ".data", "w+")
        fw = open("result/abalone/ddwq/ddwq_rmse_result_"+ str(test_size) + "_10e10.data", "w+")
        qenni_sum = 0.0
        qenni_result = []
        for j in range(test_size) :
            qenni_rmse = test_DDWQ_onDeltaAilerons(coefficient)
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

    #t = np.arange(0., 5., 0.2)
    #plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, "g^")
    #plt.show()
