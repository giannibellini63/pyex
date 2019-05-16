from threading import Thread, Condition
import time


shared = []
condition = Condition()


class Producer(Thread):
    def __init__(self, interval):
        Thread.__init__(self)
        self.interval = interval

    def run(self):
        for i in range(0, 20):
            time.sleep(self.interval)
            self.__produce()

    def __produce(self):
        global condition
        global shared

        condition.acquire()
        if len(shared) == 10:
            condition.wait()
        shared.append(1)
        print("Produzione. #Elementi: " + str(len(shared)))
        condition.notify()
        condition.release()


class Consumer(Thread):
    def __init__(self, interval):
        Thread.__init__(self)
        self.interval = interval

    def run(self):
        for i in range(0, 20):
            time.sleep(self.interval)
            self.__consume()

    def __consume(self):
        global condition
        global shared

        condition.acquire()
        if len(shared) == 0:
            condition.wait()
        shared.pop()
        print("Consumazione. #Elementi: " + str(len(shared)))
        condition.notify()
        condition.release()


if __name__ == "__main__":

    tlist = []

    producer = Producer(1)
    consumer = Consumer(2)
    producer.start()
    consumer.start()
    tlist.append(producer)
    tlist.append(consumer)

    producer.join()
    consumer.join()
