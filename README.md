# kafka-intro
Official website: https://kafka.apache.org/documentation

Kafka is installed using docker. For Mac, run the following command in the terminal.
```
docker run --rm -it \
           -p 2181:2181 -p 3030:3030 -p 8081:8081 \
           -p 8082:8082 -p 8083:8083 -p 9092:9092 \
           -e ADV_HOST=127.0.0.1 \
           landoop/fast-data-dev
```
Kafka CLI tools. Run the following in a new terminal.

```
docker run --rm -it --net=host landoop/fast-data-dev bash 
```

To create a topic [A topic in Kafka is similar to a table]. Replication factor depends on how many brokers are available.
```
kafka-topics --zookeeper 127.0.0.1:2181 --create --topic my_first_topic --partitions 3 --replication-factor 1
```

To list all the topics.
```
kafka-topics --zookeeper 127.0.0.1:2181 --list
```
To delete a topic [To do this, delete.topic.enable must be set to true.]
```
kafka-topics --zookeeper 127.0.0.1:2181 --topic my_first_topic --delete
```
To get a description of a topic.
```
kafka-topics --zookeeper 127.0.0.1:2181 --describe --topic my_first_topic
```
# Publish data to a topic
```
kafka-console-producer --broker-list 127.0.0.1:9092 --topic first_topic
```
# Consume data from a topic.
Do not include --zookeeper option.
```
kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic first_topic
```
To consume data from the very beginning.
```
kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic first_topic --from-beginning
```
To consume data from a specific partition.
```
kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic first_topic --from-beginning --partition 0
```
To specify a group.id.
```
kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic first_topic --consumer-property group.id=mygroup1 --from-beginning
```
# Here are important concepts to remember:

* Producer: Application that sends the messages.
* Consumer: Application that receives the messages.
* Message: Information that is sent from the producer to a consumer through Apache Kafka.
* Connection: A connection is a TCP connection between your application and the Kafka broker.
* Topic: A Topic is a category/feed name to which messages are stored and published.
* Topic partition: Kafka topics are divided into a number of partitions, which allows you to split data across multiple brokers.
* Replicas A replica of a partition is a "backup" of a partition. Replicas never read or write data. They are used to prevent data loss.
* Consumer Group: A consumer group includes the set of consumer processes that are subscribing to a specific topic.
* Offset: The offset is a unique identifier of a record within a partition. It denotes the position of the consumer in the partition.
* Node: A node is a single computer in the Apache Kafka cluster.
* Cluster: A cluster is a group of nodes i.e., a group of computers.

