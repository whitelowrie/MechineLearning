package chapter02

import java.io.File

import org.apache.spark.rdd.RDD
import org.slf4j.{Logger, LoggerFactory}

import scala.reflect.ClassTag

/**
  * Created by ASUS on 2015/10/27.
  */
object HadoopUtil {
    private val logger: Logger = LoggerFactory.getLogger(SmyConstant.ORION_LOGGER)

    def setHadoopHome(): Unit = {
        val path = new File(".").getCanonicalPath()
        logger.info(s"set hadoop.home.dir=$path")
        System.getProperties().put("hadoop.home.dir", path);
    }

    var hdfs: FileSystem = null

    def setHDFS(p: String): FileSystem = {
        if (hdfs == null) {
            val hdfsURI=p.replaceFirst("(hdfs://[^/]*)/.*","$1")
            val conf = new org.apache.hadoop.conf.Configuration()
            conf.setBoolean("fs.hdfs.impl.disable.cache", true);
            hdfs = org.apache.hadoop.fs.FileSystem.get(new java.net.URI(hdfsURI), conf)
        }
        hdfs
    }

    def delete( path: String): Unit = {
        setHDFS(path)
        val p = new Path(path);
        if (hdfs.exists(p)) {
            hdfs.delete(p, true)
        }
    }

    def move(path1: String, path2: String): Unit = {
        setHDFS(path1)
        val p1 = new Path(path1);
        val p2 = new Path(path2);
        if (hdfs.exists(p1)) {
            hdfs.rename(p1, p2)
        }
    }

    def exists(path:String): Boolean ={
        setHDFS(path)
        hdfs.exists(new Path(path))
    }

    def createFile( path: String): Unit = {
        setHDFS(path)
        val p = new Path(path);
        hdfs.create(p, true)
    }

    def createFolder( path: String): Unit = {
        setHDFS(path)
        val p = new Path(path);
        if (!hdfs.exists(p)) {
            hdfs.mkdirs(p)
        }
    }

    def getModificationTime(path: String): Long = {
        var mt=0L
        setHDFS(path)
        val p = new Path(path)
        if(hdfs.exists(p)){
            val fileStatus=hdfs.getFileStatus(p)
            mt=fileStatus.getModificationTime
        }
        mt
    }

    /**
      * manually checkpoint rdd to cut the dependance chain, by storing rdd to disk, so need to delete the disk file after using the rdd
      * @param rdd
      * @param path
      * @tparam T
      * @return
      */
    def checkpointRDD[T:ClassTag](rdd:RDD[T],path:String): RDD[T] ={
        logger.info(s"-------checkpointRDD to:${path}---------")
        addTempFolder(path)
        delete(path)
        rdd.saveAsObjectFile(path)
        CoreMain.sc.objectFile[T](path)
    }

    var tempFolders=scala.collection.mutable.Set[String]()
    def addTempFolder(p:String): Unit ={
        tempFolders +=p
    }

    def deleteTempFolders(): Unit ={
        logger.info(s"-------start deleteTempFolders:${tempFolders.size}---------")
        tempFolders.foreach(p=>{
            delete(p)
            logger.info(s"-------deleteTempFolder:${p}---------")
        })
        tempFolders.clear()
        logger.info(s"-------end deleteTempFolders:${tempFolders.size}---------")
    }

    def saveRDD[T:ClassTag](rdd:RDD[T],path:String): Unit ={
        HadoopUtil.delete(path)
        rdd.saveAsObjectFile(path)
    }

//    def main(args: Array[String]) {
//        setHadoopHome
//        val t=getModificationTime(SmyConstant.INIT_GRAPH_PATH)
//        println(DateTimeUtil.long2str(t))
////        delete(SmyConstant.HDFS, SmyConstant.HDFS + "/user/admin/orion/test")
////        createFile(SmyConstant.HDFS, SmyConstant.HDFS + "/user/admin/orion/test/ray")
////        createFolder(SmyConstant.HDFS, SmyConstant.HDFS + "/user/admin/orion/test/bk")
////        move( SmyConstant.HDFS + "/user/admin/orion/test/ray", SmyConstant.HDFS + "/user/admin/orion/test/bk/ray")
//    }
}
