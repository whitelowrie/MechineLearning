package sparkML.vectorTrain

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.mllib.linalg.{Matrices, Vector, Vectors}
import org.apache.spark.mllib.linalg.distributed._
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.stat.{MultivariateOnlineSummarizer, MultivariateStatisticalSummary, Statistics}
import org.apache.spark.mllib.util.MLUtils
import org.apache.tools.ant.taskdefs.optional.testing.Funtest
import org.scalatest.FunSuite

import scala.util.Random

/**
  * Created by ASUS on 2017/3/14.
  */
class VertorTest01 extends FunSuite {

  val sc = new SparkContext(new SparkConf().setAppName("goods").setMaster("local[*]"))

  test("testVector") {
    val dense:Vector = Vectors.dense(1.0, 0.0, 3.0,0,0,0,0,0,0,0,3,0)
    val sparse:Vector = Vectors.sparse(3, Array(0,2), Array(1.0, 3.0))
    val sparse1:Vector = Vectors.sparse(3, Seq((0,1.0), (2, 3.0)))
    val point = LabeledPoint(1.0, Vectors.dense(1.0, 0.0, 3.0))
    val point1 = LabeledPoint(2.0, Vectors.sparse(3, Array(0, 2), Array(1.0, 3.0)))

    println(dense.argmax)
    //进行压缩
    println(dense.compressed)

//  	val file = MLUtils.loadLibSVMFile(sc, "D:\\workspace\\git\\MachineLearning\\MechineLearning\\src\\main\\scala\\sparkML\\vectorTrain\\MyDatas.txt")
  }

  test("testMatrices"){
    val dense = Matrices.dense(3, 2 ,Array(1.0, 3.0, 5.0, 2.0, 4.0, 6.0))



    val parallelize = sc.parallelize(Array(Vectors.dense((0.0 to 10000.0 by 1).toArray)), 5)

    val matrix = new RowMatrix(parallelize)



    println(matrix.numRows())
    println(matrix.numCols())
  }

  test("testMatrices1"){
    val parallelize = sc.parallelize(0 to 100 map(_ => Vectors.dense((0.0 to 10000.0 by 1).toArray)), 5)

    val rows = sc.parallelize(0 to 100 map(x => IndexedRow(x, Vectors.dense((0.0 to 10000.0 by 1).toArray))))

    val IndexRDD:IndexedRowMatrix = new IndexedRowMatrix(rows)



    println(IndexRDD.numRows())
    println(IndexRDD.numCols())
  }

  test("testMatrices2"){
    val parallelize = sc.parallelize(0 to 100 map(_ => Vectors.dense((0.0 to 10000.0 by 1).toArray)), 5)

    val rows = sc.parallelize(0 to 100 map(x => IndexedRow(x, Vectors.dense((0.0 to 10000.0 by 1).toArray))))

    val IndexRDD:IndexedRowMatrix = new IndexedRowMatrix(rows)

   IndexRDD.toCoordinateMatrix()

    println(IndexRDD.numRows())
    println(IndexRDD.numCols())
  }

  test("bodsf"){
  	val parallelize = sc.parallelize(0 to 100 flatMap(x => 0 to 100 map(y => MatrixEntry(x,y,x*y))), 5)


    val mat = new CoordinateMatrix(parallelize)
    mat.numCols()
    val m = mat.numRows()
    val n = mat.numCols()

    println(m)

    println(n)
  }

  test("hsdf"){

//     val vectorRDD = sc.parallelize(Seq.fill(101)(Vectors.dense(Seq.fill(1000)(Random.nextDouble() * 100).toArray)))

    val vectorRDD = sc.parallelize(Seq.fill(4)(Vectors.dense(5,3,6)))

     val stats:MultivariateStatisticalSummary = Statistics.colStats(vectorRDD)
     println(stats.normL2)
  }

  test("pearson"){

    //     val vectorRDD = sc.parallelize(Seq.fill(101)(Vectors.dense(Seq.fill(1000)(Random.nextDouble() * 100).toArray)))

    val vectorRDD1 = sc.parallelize(Array(5.0,3,6))
    val vectorRDD2 = sc.parallelize(Array(7.0,3,6))

    //使用皮尔逊相关系数
    val stats:Double = Statistics.corr(vectorRDD1,vectorRDD2,"pearson")
    println(stats)
  }

  test(""){

  }
}
