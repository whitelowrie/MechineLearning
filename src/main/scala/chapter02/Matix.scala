package chapter02

/**
  * Created by bigdata on 2017/3/11.
  */
class Matix(val array: Array[Int], val y:Int) {

  if(array.length % y != 0) throw new RuntimeException("array lenth mast sub n !!!")

  def this(array:Array[Array[Int]]) = {
    this(array.foldLeft(Array[Int]())(_ ++ _), array.length)
  }


  var x = array.length / y

  private val matix0:Array[Array[Int]] = array.sliding(y, y).toArray

  def getShape = {
    Array(y,x)
  }

  def getX(n:Int) = {
    matix0.map(_(n))
  }

  def getY(n:Int) = {
    matix0(n)
  }

  def add(other:Matix) = {
    validate(other:Matix)
    new Matix(other.array.zip(this.array).map(x => x._1 + x._2),this.y)
  }

  def sub(other:Matix) = {
    validate(other:Matix)
    new Matix(other.array.zip(this.array).map(x => x._1 - x._2),this.y)
  }

  def muti(other:Matix) = {
    validateMuti(other:Matix)
    val map: Array[Array[Int]] = matix0.map(xArr => {
      other.array.sliding(this.x).map(_.zip(xArr).foldLeft(0) { case (num, (n1, n2)) => num + n1 * n2 }).toArray
    })
    new Matix(map)
  }

  def validateMuti(other:Matix) = {
    if(other.y != this.x)
      throw new RuntimeException("now equals")
  }



  def validate(other:Matix): Unit ={
    if(other.x != this.x || other.y != this.y)
      throw new RuntimeException("now equals")
  }

  override def toString: String = {
      this.matix0.map(_.mkString(",")).toArray.mkString("[","][","]")
  }

}

object Matix{
  def main(args: Array[String]): Unit = {
    val m = new Matix(Array(1,2,3,4,5,6), 3)

    val m2 = new Matix(Array(3,4,5,6,7,8), 2)
    println(m.muti(m2))
  }
}
