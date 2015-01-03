#! /usr/bin/python

# author zhangzhaoyu
# Date   2014-01-03
# Description:
# This module is used to compute the different kinds of 
# distance. include :
# * Euclid Distance

from numpy import *

def createDataSet() :
    one = array([1, 2])
    two = array([1, 2])
    return one, two


def euclidDistance(one, two) :
    tempData = one - two
    sqTempData = tempData ** 2
    sqDistances = sqTempData.sum()    
    print sqDistances ** 0.5


if __name__ == '__main__' :
    one, two = createDataSet()
    euclidDistance(one, two)
