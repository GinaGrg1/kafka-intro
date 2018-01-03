# kafka-intro

Kafka is installed using docker. For Mac, run the following command in the terminal.
```
docker run --rm -it \
           -p 2181:2181 -p 3030:3030 -p 8081:8081 \
           -p 8082:8082 -p 8083:8083 -p 9092:9092 \
           -e ADV_HOST=127.0.0.1 \
           landoop/fast-data-dev
```
Kafka CLI tools.

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
