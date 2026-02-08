# Realtime Market Analytics with Spark

> Streaming data platform for processing and analyzing web traffic patterns using Apache Spark, Elasticsearch, and Kibana

**Project Timeline:** January 15, 2025 

---

## 🎯 Project Summary

This platform demonstrates enterprise-grade streaming analytics capabilities by ingesting simulated web server logs, processing them through Apache Spark Streaming, and delivering insights through Elasticsearch and Kibana dashboards. The system handles continuous data flows with micro-batch processing while maintaining low latency and high throughput.

The implementation showcases production patterns for building fault-tolerant streaming pipelines that can scale horizontally to accommodate growing data volumes and user demands.

---

## 🏗️ System Architecture

### Data Flow Pipeline

Log Generator → File System → Spark Streaming → Elasticsearch → Kibana Dashboards

**Components:**

1. **Data Generation Layer**
   - Python-based log simulator producing realistic HTTP request logs
   - Generates randomized web traffic patterns (URLs, paths, IP addresses, status codes)
   - Continuous stream output with configurable batch intervals

2. **Ingestion & Processing**
   - Spark Streaming monitors log directories for new data files
   - Micro-batch processing (configurable intervals)
   - Data transformation and enrichment in-memory
   - Distributed computing across cluster nodes

3. **Storage & Indexing**
   - Elasticsearch cluster for fast document storage
   - Automatic indexing for sub-second search performance
   - Time-series data optimization

4. **Visualization Layer**
   - Kibana dashboards for real-time monitoring
   - Custom visualizations for traffic patterns
   - Interactive filtering and drill-down capabilities

## 💻 Technology Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Scala 2.12.15 |
| **Stream Processing** | Apache Spark 3.5.0 (Streaming, SQL, Core) |
| **Search Engine** | Elasticsearch 7.17.0 |
| **Visualization** | Kibana 7.17.0 |
| **Build Tool** | SBT (Simple Build Tool) |
| **Containerization** | Docker Compose |
| **Data Generation** | Python 3.x |

## 📊 Key Capabilities

- **High-Throughput Streaming:** Process thousands of events per second with configurable batch windows
- **Horizontal Scalability:** Add Spark workers to handle increased load without code changes
- **Real-Time Insights:** Near-instantaneous data availability in dashboards (sub-second latency)
- **Fault Recovery:** Automatic recovery from node failures with checkpointing
- **Flexible Schema:** Schema-on-read approach for evolving data structures
- **Interactive Analytics:** Ad-hoc queries through Kibana interface without pipeline modifications

## 🚀 Quick Start Guide

### Prerequisites

Ensure the following are installed on your system:

- Java Development Kit (JDK) 11 or higher
- Scala 2.12.x
- Apache Spark 3.5.0
- Docker and Docker Compose
- Python 3.8+
- SBT 1.x

### Installation Steps

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/realtime-market-analytics-spark.git
cd realtime-market-analytics-spark
```

**2. Start Elasticsearch and Kibana**
```bash
docker-compose -f elasticsearch-kibana_compose.yaml up -d
```

Wait approximately 30-60 seconds for services to initialize. Verify by accessing:
- Elasticsearch: http://localhost:9200
- Kibana: http://localhost:5601

**3. Prepare the data directory**
```bash
mkdir -p tmp
mkdir -p src/main/resources/data
```

**4. Start the log generator**
```bash
python log-generator-files.py
```
This creates `tmp/log-generator.log` with continuous simulated traffic.

**5. Run the data splitter** (in a new terminal)
```bash
python Data-splitter.py
```
This chunks the continuous log into 1000-line batches for Spark to consume.

**6. Compile and run the Spark application**
```bash
sbt clean compile
sbt run
```

**7. Access Kibana dashboards**

Navigate to http://localhost:5601 and create index patterns for your data to start visualizing.

---

## 📁 Project Structure

```
realtime-market-analytics-spark/
├── build.sbt                              # SBT build configuration
├── src/
│   └── main/
│       ├── scala/                         # Spark Streaming application code
│       └── resources/
│           └── data/                      # Input log files directory
├── Data-splitter.py                       # Log batch processor
├── log-generator-files.py                 # Synthetic log generator
├── elasticsearch-kibana_compose.yaml      # Docker services definition
├── tmp/                                   # Temporary log storage
└── README.md
```

---

## 🔧 Configuration Details

### Spark Application Settings

The Spark Streaming context is configured with the following parameters:

- **Batch Interval:** Micro-batches processed every few seconds
- **Checkpoint Directory:** Enables fault tolerance and state recovery
- **Executor Memory:** Allocate based on data volume (default: 2GB)
- **Parallelism:** Matches number of available cores

### Elasticsearch Configuration

Connection settings in the Spark application:

- **Host:** localhost:9200
- **Index Pattern:** Dynamic based on data source
- **Bulk Write:** Batch inserts for efficiency
- **Security:** Disabled for local development (enable for production)

### Log Generation Parameters

Customize `log-generator-files.py` to adjust:

- Traffic volume (events per second)
- URL distribution patterns
- HTTP status code probabilities
- IP address ranges

## 📈 Use Cases

This architecture pattern applies to numerous streaming scenarios:

- **Web Analytics:** Track user behavior, page views, session duration
- **Application Monitoring:** Real-time error detection and performance metrics
- **Security & Compliance:** Detect anomalies in access patterns
- **E-commerce Intelligence:** Monitor transaction flows and conversion funnels
- **IoT Data Processing:** Sensor data aggregation and alerting

## 🧪 Testing the Pipeline

**Verify data generation:**
```bash
tail -f tmp/log-generator.log
```

**Check batched files:**
```bash
ls -lh src/main/resources/data/
```

**Query Elasticsearch directly:**
```bash
curl -X GET "localhost:9200/_cat/indices?v"
```

**Monitor Spark streaming job:**
Check the Spark UI at http://localhost:4040 (when job is running)


## 🎓 Technical Highlights

### Micro-Batch Processing

Spark Streaming divides continuous data into discrete batches, enabling:
- Efficient distributed processing using Spark's RDD operations
- Exactly-once semantics through checkpointing
- Seamless integration with Spark SQL and DataFrame API

### Elasticsearch Integration

The Elasticsearch-Hadoop connector provides:
- Native Spark DataFrame support for Elasticsearch
- Automatic document mapping and index creation
- Bulk write optimization for high throughput

### Scala Functional Programming

Benefits demonstrated in this project:
- Immutable data structures prevent concurrent modification issues
- Higher-order functions enable concise transformations
- Strong static typing catches errors at compile time

## 🔒 Production Considerations

When deploying to production environments, implement:

1. **Security:** Enable Elasticsearch authentication and TLS encryption
2. **Monitoring:** Integrate with Prometheus/Grafana for cluster health metrics
3. **Resource Management:** Use YARN or Kubernetes for resource allocation
4. **Data Retention:** Configure index lifecycle policies in Elasticsearch
5. **Backup Strategy:** Regular snapshots of Elasticsearch indices
6. **Error Handling:** Dead letter queues for failed records

## 📚 Learning Resources that I used

**Apache Spark Documentation:**
- Official Guide: https://spark.apache.org/docs/latest/streaming-programming-guide.html
- Structured Streaming: https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html

**Elasticsearch Documentation:**
- Getting Started: https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html
- Elasticsearch for Apache Hadoop: https://www.elastic.co/guide/en/elasticsearch/hadoop/current/index.html

**Scala Resources:**
- Scala Documentation: https://docs.scala-lang.org/
- Functional Programming Principles: https://www.coursera.org/learn/scala-functional-programming

## 🛠️ Troubleshooting

**Issue: Elasticsearch connection refused**
- Solution: Ensure Docker containers are running (`docker ps`)
- Wait 60 seconds after starting containers for initialization

**Issue: Out of memory errors in Spark**
- Solution: Increase executor memory in `build.sbt` or run configuration
- Reduce batch size in `Data-splitter.py`

**Issue: No data appearing in Kibana**
- Solution: Verify index pattern matches Elasticsearch indices
- Check Spark logs for write errors
- Confirm data splitter is creating files in `src/main/resources/data/`

**Issue: SBT dependency resolution failures**
- Solution: Clear SBT cache: `rm -rf ~/.sbt ~/.ivy2/cache`
- Retry: `sbt clean update compile`
___________________________________________________________________________________

**Built with:** Scala, Apache Spark, Elasticsearch, Kibana, Docker  
**Status:** Production-ready architecture pattern