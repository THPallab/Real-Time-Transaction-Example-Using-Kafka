from confluent_kafka import Producer

while (1):
    def acked(err, msg):
        if err is not None:
            print("Failed to deliver message: {0}: {1}"
                  .format(msg.value(), err.str()))
        else:
            print("Message produced: {0}".format(msg.value()))

    p = Producer({'bootstrap.servers': 'localhost:9092'})

    try:
            tt = input()
            p.produce('mytopic','{0}'
                      .format(tt), callback=acked)
            p.poll(0.5)

    except KeyboardInterrupt:
        pass

    p.flush(30)
