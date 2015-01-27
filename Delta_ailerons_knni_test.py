#! /usr/bin/env python

# Test the data set of Delta_ailerons by algorithm KNNI
# show the result by matplotlib
import numpy as np
import matplotlib.pyplot as plt
import DataFilter as df
import KNNI as KNNI

def test_KNNI_onDeltaAilerons(k) :
    print "**************in knni test***********"
    deltaDataList = df.dataOfDeltaAilerons()
    completeDataSet, incompleteDataSet = df.createRandomCompleteAndIncompleteDataSet(deltaDataList)
    lenghtOfincompleteData = len(incompleteDataSet)

    impute_data_result = []
    for iDataSet in incompleteDataSet :
        resultData = KNNI.knni_impl(np.array(iDataSet[:-1]), np.array(completeDataSet), k)
        #print "the result is " + resultData
        impute_data_result.append(resultData)
        print resultData
       # print "total times %d" %(i)

    # compute the RMSE
    m = len(impute_data_result)
    sum = 0.0
    for j in range(m) :
        sum += abs(incompleteDataSet[j][-1] - impute_data_result[j])
    knni_rmse = sum / m
    #print "sum is %f, m is %d " %(sum, m)
    #print "the knni rmse is %f" %(rmse)
    return knni_rmse

if __name__ == "__main__" :
    test_size = 100
    # paramater of kNNI
    k = 7
    fw = open("result/knni_rmse_result_" + str(test_size) + "_" + str(k) +  ".data", "w+")
    knni_sum = 0.0
    knni_result = []
    for j in range(test_size) :
        knni_rmse = test_KNNI_onDeltaAilerons(k)
        knni_result.append(knni_rmse)
        print "rmse is "
        print str(knni_rmse)
        fw.write(str(knni_rmse) + "\n")
        knni_sum += knni_rmse

    knni_average_rmse = knni_sum / test_size
    print "average rmse is"
    print str(knni_average_rmse)
    fw.write(str(knni_average_rmse) + "\n")
    fw.close()

    t = np.arange(0., 5., 0.2)
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, "g^")
    plt.show()
