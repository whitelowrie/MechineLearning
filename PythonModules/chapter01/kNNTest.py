from numpy import *
import operator
import kNN


def createDataSets(inX, group, label, k):
    groupDataSize = group.shape[0]
    inxs = tile(inX, (groupDataSize, 1)) - group
    disInx = inxs ** 2
    disSum = disInx.sum(axis=1)
    disbis = disSum ** 0.5
    disSort = disbis.argsort()

    result = {}
    for i in range(k):
        labels = label[disSort[i]]
        result[labels] = result.get(labels, 0) + 1
    resultSort = sorted(result.iteritems(), key=operator.itemgetter(1), reverse=True)
    return resultSort[0][0]
group, label = kNN.createDateSet()

print createDataSets([0, 0], group, label, 3)
