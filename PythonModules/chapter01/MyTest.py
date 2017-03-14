# -*- coding:utf-8 -*-

import kNN
from numpy import *

def classifyPerson():
	resultList = ['not at all','in small doses','in large doses']
	percentTats = float(raw_input("percentage of time spent playing video games ? "))
	ffMiles = float(raw_input("frequ year ? ")) 
	iceCream = float(raw_input("liters year ? "))
	datingDataMat,datingLabels = file2matrix("text.txt")
	normMat, ranges, minVals = autoNorm(datingDataMat)
	inArr = array([ffMiles, percentTats, iceCream])
	classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)
	print "You will probably like this person: ",resultList[classifierResult - 1]

classifyPerson()