#! /usr/bin/env python

# author : zhangzhaoyu
# date : 2015-01-28
import numpy as np
import matplotlib.pyplot as plt

#plt.plot([5, 10, 15, 20, 25, 30], [0.00018, 0.00016, 0.00015, 0.00014, 0.00013, 0.0001256], 'ro')
#define the axis(x and y)
#plt.axis([0, 30, 0.00010, 0.00030])
#plt.ylabel("RMSE")
#plt.xlabel("k")
#plt.show()


def read_knni_data(filepath = "result/knni/") :
    sizeOftest = 30
    knni_data_list = []
    for i in range(sizeOftest) :
        filename = filepath + "knni_rmse_result_100_" + str(i+1) +".data"
        result_str = open(filename).readlines()[-1]
        temp = float(result_str.strip("\n"))
        knni_data_list.append(float('%.7f'%temp))
    return np.array(knni_data_list)

def read_qenni_data(filepath = "result/qenni/") :
    filename = filepath + "qenni_rmse_result_100.data"
    result_str = open(filename).readlines()[-1]
    temp = float(result_str.strip("\n"))
    qenni_average_data = float('%.7f'%temp)
    return np.array([qenni_average_data for i in range(30)])

def read_ddwq_data(filepath = "result/ddwq/") :
    filename = filepath + "ddwq_rmse_result_100_10e10.data"
    result_str = open(filename).readlines()[-1]
    temp = float(result_str.strip("\n"))
    ddwq_average_data = float('%.7f'%temp)
    return np.array([ddwq_average_data for i in range(30)])

#t = np.arange(0.0, 5.0, 0.2)
#line1, = plt.plot(t, t, 'ro-', marker='o', label="kNNI")
#line2, = plt.plot(t, t**2, 'bs-.', marker='s', label='QENNI')
#line3, = plt.plot(t, t**3, 'g^:', marker='^', label='DDWQ')
#line1.set_antialiased(False)
#plt.ylabel("RMSE")
#plt.xlabel("k")
#plt.title("DDWQ and DENNI and kNNI")
#plt.legend([line1, line2, line3], ['kNNI', 'QENNI', 'DDWQ'])
#plt.show()

if __name__ == "__main__" :

    plt.figure(figsize=(18, 10))

    plt.subplot(221)
    #plt.figure(figsize=(8, 4))
    #plt.axis([0, 30, 0.000120, 0.000170])

    knni_y_data =  read_knni_data("result/abalone/knni/")
    knni_x_data = np.arange(1, 31 , 1)
    line1, = plt.plot(knni_x_data, knni_y_data, 'y^-', marker = '^', label = 'kNNI', linewidth = 1.0)

    qenni_y_data = read_qenni_data("result/abalone/qenni/")
    qenni_x_data = np.arange(1, 31 , 1)
    line2, = plt.plot(qenni_x_data, qenni_y_data, 'bs-', marker = 's', label = 'QENNI', linewidth = 1.0)

    ddwq_y_data = read_ddwq_data("result/abalone/ddwq/")
    ddwq_x_data = np.arange(1, 31 , 1)
    line3, = plt.plot(ddwq_x_data, ddwq_y_data, 'ro-', marker = 'o', label = 'DDWQ', linewidth = 1.0)

    plt.xlabel('k')
    plt.ylabel('RMSE')
    #plt.legend([line1, line2, line3], ["kNNI", "QENNI", "DDWQ"])
    plt.legend()



    plt.subplot(222)
    plt.axis([0, 30, 0.000120, 0.000170])
    knni_y_data =  read_knni_data()
    knni_x_data = np.arange(1, 31 , 1)
    line1, = plt.plot(knni_x_data, knni_y_data, 'y^-', marker = '^', label = 'kNNI', linewidth = 1.0)

    qenni_y_data = read_qenni_data()
    qenni_x_data = np.arange(1, 31 , 1)
    line2, = plt.plot(qenni_x_data, qenni_y_data, 'bs-', marker = 's', label = 'QENNI', linewidth = 1.0)

    ddwq_y_data = read_ddwq_data()
    ddwq_x_data = np.arange(1, 31 , 1)
    line3, = plt.plot(ddwq_x_data, ddwq_y_data, 'ro-', marker = 'o', label = 'DDWQ', linewidth = 1.0)

    plt.xlabel('k')
    plt.ylabel('RMSE')
    #plt.legend([line1, line2, line3], ["kNNI", "QENNI", "DDWQ"])
    plt.legend()

    plt.show()
