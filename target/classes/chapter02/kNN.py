#-*-coding:utf-8-*-

from numpy import *
import operator

def createDateSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

#(1)计算已知类别的数据集中的点与当前点之间的距离；

#(2)按照距离递增次序排序

#(3)选取与当前点距离最小的K个点

#(4)确定前K个点所在类别的出现频次

#(5)返回前K个点出现频率最高的类别作为当前的预测分类

'''
    inx:分类向量
    dataSet:训练样本集合dataSet
    labels:标签向量
    k:最近的邻居数据

    计算距离：
    d^2 = (y1 - y0)^2 + (x1 - x0)^2
'''
def classify(inX,dataSet,labels,k):
    #获得矩阵的维度数量，将纵向量的个数作为第一列，横向量的个数作为第二列:[4,2] -> dataSetSize = 4
    dataSetSize = dataSet.shape[0]
    #tile的含义是使用inx作为横向量模板复制 inx = [0,0]
    #title([0,0],(4,1)) => [[0,0],
    #                       [0,0]
    #                       [0,0]
    #                       [0,0]]
    #矩阵的减法就是相同位置的进行相减
    #dataSet = [[ 1.   1.1]
    #           [ 1.   1. ]
    #           [ 0.   0. ]
    #           [ 0.   0.1]]
    #结果就是
    #           [[-1.  -1.1]
    #           [-1.  -1. ]
    #           [ 0.   0. ]
    #           [ 0.  -0.1]]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    print tile(inX, (dataSetSize, 1))
    print diffMat

    sqDiffMat = diffMat ** 2
    # sqDistances = sqDiffMat.sum(axis=1)
    # dinstances = sqDistances ** 0.5
    # sortedDistIndicies = dinstances.argsort()
    # classCount = {}
    # for i in range(k):
    #     voteILabel = labels[sortedDistIndicies]
    #     classCount[voteILabel] = classCount.get(voteILabel, 0) + 1
    # sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    #
    # return sortedClassCount[0][0]



groups,label = createDateSet()
#
# data = array([[[1,2,7],[3,4,2]],[[3,5,4],[7,9,5]]])
#
# print data.shape #(2, 2, 3)
#
# print tile(1,2) #[1,1]
#
# a = [1,2]


# print tile(a,3) #[1 2 1 2 1 2]
#
# # [1,1]的的表示就是二维矩阵，横向量一列，纵轴一列
# # 将[1,2] 填充进去就是 | 1, 2 |
# print tile(a, [1,1])
#
# #[1,2]的表示就是一行两列，两列是指a被复制两次
# #结果就是[[1,2,1,2]]
# print tile(a, [1,2])
#
# #[3,2]的表示就是三行两列，三行是指共有三行，两列是指复制两次
# print tile(a, [3,2])
#
# #[3,2] 三维的，三行，两列
# print tile(a, [3,2,2])


print groups

print classify([0,0], groups, label, 3)





