from confluent_kafka import Producer
import socket

while (1):
    def acked(err, msg):
        if err is not None:
            print("Failed to deliver message: {0}: {1}"
                  .format(msg.value(), err.str()))
        else:
            print("Message produced: {0}".format(msg.value()))

    p = Producer({'bootstrap.servers': '192.168.1.107:9092'})

    try:
            host='192.168.***.***' #client/consumer ip
            port = 9092
            server = ('192.168.***.***', 9092)    #server/producer ip
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind((host,port))

            # while (1):
            #     message = input("-> ")
            #     s.sendto(message.encode('utf-8'), server)
            # s.close()

            tt = input()
            p.produce('testtopic','{0}'
                      .format(tt), callback=acked)
            p.poll(0.5)

    except KeyboardInterrupt:
        pass

    p.flush(30)
    s.close
