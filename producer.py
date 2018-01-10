import threading, logging, time
import multiprocessing

from kafka-python import KafkaProducer

class Producer(threading.Thread):
    daemon = True

    def run(self):
        producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
	
	while True:
	    producer.send('hello', 'world!')
	    time.sleep(1)

def main():
    tasks = [
	Producer()
    ]

    for i in tasks:
        t.start()
    
    time.sleep(10)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO)
    main()
