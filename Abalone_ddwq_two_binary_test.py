#! /usr/bin/env python

# Test the data set of Abalone by algorithm QENNI and WWDQ
# show the result by matplotlib
import numpy as np
import matplotlib.pyplot as plt
import DataFilter as df
import DDWQ as DDWQ
import QENNI as QENNI

def test_DDWQ_onAbalone(coefficient) :
    print "**************in ddwq test***********"
    deltaDataList = df.dataOfAbalone()
    completeDataSet, incompleteDataSet = df.createRandomCompleteAndIncompleteDataSet(deltaDataList)
    lenghtOfincompleteData = len(incompleteDataSet)

    impute_data_result = []
    for iDataSet in incompleteDataSet :
        resultData, p_phoose, dist_weight, numOfEachQ, volumeOfEachQ = DDWQ.wqenni_impl(np.array(iDataSet[:-1]), np.array(completeDataSet), coefficient)
        #print "the result is " + resultData
        impute_data_result.append(resultData)
        #print resultData
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

def return_rmse_size_coefficient(test_size, coefficient) :
    sum = 0.0
    for j in range(test_size) :
        ddwq_rmse = test_DDWQ_onAbalone(coefficient)
        sum += ddwq_rmse
    average_rmse = sum / test_size
    return average_rmse

if __name__ == "__main__" :
    test_size = 100
    min_coefficient = 0.10
    max_coefficient = 0.50
    min_average_rmse = return_rmse_size_coefficient(test_size, min_coefficient)
    max_average_rmse = return_rmse_size_coefficient(test_size, max_coefficient)
    current_coefficient = 0.0

    running_flag = True
    while running_flag :
        print "min_average_rmse is %.8f, min_coefficient is %.8f " %(min_average_rmse, min_coefficient)
        print "max_average_rmse is %.8f, max_coefficient is %.8f " %(max_average_rmse, max_coefficient)

        if min_average_rmse < max_average_rmse :
            max_coefficient = (min_coefficient + max_coefficient) / 2.0
            max_average_rmse = return_rmse_size_coefficient(test_size, max_coefficient)
            #if max_temp >= max_average_rmse :
            #    running_flag = False
            #else :
            #    max_average_rmse = max_temp
        else :
            min_coefficient = (min_coefficient + max_coefficient) / 2.0
            min_average_rmse = return_rmse_size_coefficient(test_size, min_coefficient)
            #if min_temp >= min_average_rmse :
            #    running_flag = False
            #else :
            #    min_average_rmse = min_temp

    print 'algorithm is finished!!!'
