spark-shell --jars json-serde-1.3.8.jar
import org.apache.spark.sql.SparkSession
val temp = sqlContext.sql("select * from final_out")
val q = sqlContext.sql("select hour,count(*) as words_per_hour from temp1 group by hour")
q.saveAsTable("end_result")
  
