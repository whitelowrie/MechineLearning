# -*-coding:utf-8-*-

from numpy import *
import operator
import random as rm


def createDateSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

# (1)计算已知类别的数据集中的点与当前点之间的距离；

# 2)按照距离递增次序排序

# 3)选取与当前点距离最小的K个点

# 4)确定前K个点所在类别的出现频次

# 5)返回前K个点出现频率最高的类别作为当前的预测分类

#
#    inx:分类向量
#    dataSet:训练样本集合dataSet
#    labels:标签向量
#    k:最近的邻居数据

#    计算距离：
#    d^2 = (y1 - y0)^2 + (x1 - x0)^2


def classify(inX, dataSet, labels, k):
    # 获得矩阵的维度数量，将纵向量的个数作为第一列，横向量的个数作为第二列:[4,2] -> dataSetSize = 4
    dataSetSize = dataSet.shape[0]
    # tile的含义是使用inx作为横向量模板复制 inx = [0,0]
    # title([0,0],(4,1)) => [[0,0],
    #                       [0,0]
    #                       [0,0]
    #                       [0,0]]
    # 矩阵的减法就是相同位置的进行相减
    # dataSet = [[ 1.   1.1]
    #           [ 1.   1. ]
    #           [ 0.   0. ]
    #           [ 0.   0.1]]
    # 结果就是
    #           [[-1.  -1.1]
    #           [-1.  -1. ]
    #           [ 0.   0. ]
    #           [ 0.  -0.1]]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # print tile(inX, (dataSetSize, 1))
    # print diffMat

    # 这表示进行各自的平方
    # 结果是
    '''
        [[ 1.    1.21]
         [ 1.    1.  ]
         [ 0.    0.  ]
         [ 0.    0.01]]
    '''
    sqDiffMat = diffMat ** 2

    # print sqDiffMat
    # sum()是全部相加
    # sum(a，axis=0) 仅仅表示按行的相加
    # sum(a, axis=1) 表示按列相加
    # 结果是
    '''
        [ 2.1  2.   0.   0.1]
    '''
    sqDistances = sqDiffMat.sum(axis=1)

    '''
        表示开平方
    '''
    dinstances = sqDistances ** 0.5

    # print dinstances

    # 就是一种排序,argsort()函数是将x中的元素从小到大排列，提取其对应的index(索引)，然后输出到y，所以
    # 结果是[2 3 1 0] 下标为2的是最小的，第二小的是下标为3的
    sortedDistIndicies = dinstances.argsort()

    # print sortedDistIndicies
    classCount = {}
    for i in range(k):
        # 得到的是sortedDistIndicies[i]中的依次元素，再用这个元素作为下标在label中的到对应的元素
        voteILabel = labels[sortedDistIndicies[i]]

        classCount[voteILabel] = classCount.get(voteILabel, 0) + 1

    # 表示取出元组，然后使用元组的值进行排序
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]


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


# print groups

# print classify([0,0], groups, label, 3)

# #表示
# print groups.sum(axis=1)

# help(numpy.argsort)


def file2matrix(filename):
    # 打开文件
    fr = open(filename)
    # 获得内容的
    arrayOlines = fr.readlines()
    # 获得有多少行
    numberOfLines = len(arrayOlines)
    # 生成和文件相同行的矩阵
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOlines:
        # 去除头尾空字符串
        line = line.strip()
        # print line
        #
        listFromLine = line.split('\t')
        # print listFromLine

        # print listFromLine[0:3]
        returnMat[index] = listFromLine[0:3]

        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


dataMa, label = file2matrix(
    "/Users/bigdata/Documents/MyData/mldata/Ch02/datingTestSet2.txt")


# maxs = array([[1,2,3,4],[3,4,5,6]])
# maxs[0,:] = [3,2,4,5]

# print maxs

# numpy有自己的数组，它的数组天然是矩阵
# 类似于range(10),但是生成的是
# a = arange(10)
# #使用 ： 来做切片,[3:5]的意思就是从下标3开始，截止到5之前
# print a[3:5]
# #使用[-1]表示倒数第一个的下标
# print a[-1]
# #表示从头开始截止到最后一个之前
# print a[:-1]
# #表示从最后一个开始到第一个之前，下标为负仍然是相同的每次加上起始位置
# print a[-1:0:-1]
# #表示转置
# print a[::-1]
# #步长为负数的时候，开始的下标必须大于结束下标
# print a[5:1:-2]
# #使用一个数组作为下标，表示取出数组中对应下标的所有元素
# print a[[2,3,4,2]]


# #多维数组
# 向量的的下标永远是使用“:”分割的，因为向量是一个数组，元组的“，”会分割矩阵的轴，如果是二维矩阵，就使用一个“，”
# b = arange(0,60,10).reshape(-1,1) + arange(0,6)
# #表示去的是a[0,1]
# print b[(0,1,2,3,4),(1,2,3,4,5)]
# [ [ 0 for i in range(6) ] for j in range(6) ]

def autoNorm(dataSet):
    # 按列获取最小值
    minVals = dataSet.min(0)
    # 按列获取最大值
    maxVals = dataSet.max(0)
    # 求出每一列的范围
    ranges = maxVals - minVals
    # 简历矩阵
    normDataSet = zeros(shape(dataSet))
    # 获得列向量元素的个数
    m = dataSet.shape[0]
    # 使用最小的向量填充，使用当前值减去最小值
    normDataSet = dataSet - tile(minVals, (m, 1))
    # 差值除以范围
    normDataSet = normDataSet * 1.0 / tile(ranges, (m, 1))
    # 或者normDataSet = normDataSet * 1.0/ranges 结果相同
    # 返回值
    return normDataSet, ranges, minVals

# def autoNorms(dataSet):
#     #按列获取最小值
#     minVals = dataSet.min(0)
#     #按列获取最大值
#     maxVals = dataSet.max(0)
#     #求出每一列的范围
#     ranges = maxVals - minVals
#     #简历矩阵
#     normDataSet = zeros(shape(dataSet))
#     #获得列向量元素的个数
#     m = dataSet.shape[0]
#     #使用最小的向量填充，使用当前值减去最小值
#     normDataSet = dataSet - tile(minVals,(m,1))
#     #差值除以范围
#     normDataSet = normDataSet * 1.0/ranges
#     #返回值
#     return normDataSet,ranges,minVals


# 生成6*6矩阵
# datas = array([[int(rm.random() * 1000) for i in range(2)] for i in range(4)])

# print datas

# 除法，可以除以矩阵的行向量个数相同的向量或者单个值，或者矩阵
# print datas / array([2,3])
# print zeros(shape(datas))

# normDataSet,ranges,minVals = autoNorm(datas)
# normDataSet1,ranges1,minVals1 = autoNorms(datas)

# print normDataSet
# print normDataSet1
# print ranges
# print minVals

# 按列获取最大值，将每一列的最大值作为一个数组，
# max()不加参数是所有值中的最大值，
# 0是按列取得最大值，1是按行取得最大值
# print datas.max(0)

def dataClassTest():
    # 使用测试样本比例
    hoRatio = 0.10
    # 得到数据
    datingDataMat, datingDataLabel = file2matrix("/Users/bigdata/Documents/MyData/mldata/Ch02/datingTestSet2.txt")
    # 归一化
    normMat, ranges, minVals = autoNorm(datingDataMat)
    # 得到列向量的长度
    m = normMat.shape[0]
    # 得到样本的长度，这里numTestVecs=100
    numTestVecs = int(m * hoRatio)
    errorCount = 0
    for i in range(numTestVecs):
        classifierResult = classify(normMat[i, :], normMat[numTestVecs:m, :], datingDataLabel[numTestVecs:m], 3)
        print "the classifier came back with:%d, the real answer is : %d" % (classifierResult, datingDataLabel[i])
        if (classifierResult != datingDataLabel[i]):
            errorCount += 1.0

    print "the totle error rate is : %f" %(errorCount / float(numTestVecs))

dataClassTest()
