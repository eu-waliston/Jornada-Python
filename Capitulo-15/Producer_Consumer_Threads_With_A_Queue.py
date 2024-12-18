# SuperFastPython.com
# example of producer and consumer threads with a shared queue
from time import sleep
from random import random
from threading import Thread
from queue import Queue

from jinja2.utils import consume


#generate work
def producer(queue):
    print("Producer: RUNNING!!!")
    #generate work
    for i in range(10):
        #generate a value
        value = random()
        #block
        sleep(value)
        #add to the queue
        queue.put(value)
    # all done
    queue.put(None)
    print('Producer: DONE!!!')

#all done
def consumer(queue):
    print("Consumer: RUNNING!!!")
    #consu8mer work
    while True:
        #get a unit of work
        item = queue.get()
        #check for stop
        if item is None:
            break
        #report
        print(f">got {item}")
    #all done
    print("Consumer: DONE!!!")

# create the shared queue
queue = Queue()
# start the consumer
consumer = Thread(target=consumer, args=(queue,))
consumer.start()
# start the producer
producer = Thread(target=producer, args=(queue,))
producer.start()
# wait for all threads to finish
producer.join()
consumer.join()