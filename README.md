At first go to your Kafka directory.

1. At first start Zookeeper Server using this command: "bin/zookeeper-server-start.sh config/zookeeper.properties"
2. Run Kafka Server using this command: "bin/kafka-server-start.sh config/server.properties"

After successfuly running this two server, follow these same commands in two different terminals inside your project directory.
* pip install confluent_kafka

Now run "python producer_updated.py" in a terminal and run "python consumer_updated.py" in another terminal.
The first terminal will be used as a producer end and the second one will be used as a consumer end.
