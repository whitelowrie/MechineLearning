package chapter02

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.SQLContext
import org.apache.spark.sql.hive.HiveContext
import HadoopUtil

/**
  * Created by ASUS on 2017/3/14.
  */
object MyTestHive {
  def main(args: Array[String]): Unit = {
    HadoopUtil.setHadoopHome()
    val sc = new SparkConf().setMaster("local[*]").setAppName("test")
    val context = new HiveContext(new SparkContext(sc))
    val names = context.tableNames()
    println(names.mkString(","))
  }
}
