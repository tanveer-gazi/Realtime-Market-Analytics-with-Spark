name := "SparkStreamingProject"

version := "1.0"

scalaVersion := "2.12.15"

val sparkVersion = "3.5.0"
val elasticsearchVersion = "7.17.0"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.apache.spark" %% "spark-sql" % sparkVersion,
  "org.apache.spark" %% "spark-streaming" % sparkVersion,
  "org.elasticsearch" % "elasticsearch-spark-20_2.12" % elasticsearchVersion,
  "com.typesafe" % "config" % "1.4.1"
)
dependencyOverrides += "org.apache.yetus" % "audience-annotations" % "0.13.0"
dependencyOverrides += "io.airlift" % "aircompressor" % "0.25"
dependencyOverrides += "io.netty" % "netty-transport-native-epoll" % "4.1.96.Final"
