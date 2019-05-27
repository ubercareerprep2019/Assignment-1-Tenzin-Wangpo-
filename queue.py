"""
    Tenzin Wangpo
"""
from stack import *

class Queue:
    def __init__(self):
        self.__queue = Stack()

    def enqueue(self, data):
        self.__queue.push(data)


    def dequeue(self):
        return self.__queue.pop(typeDS="Queue")

    def mini(self):
        return self.__queue.mini()

    def printAll(self):
        return self.__queue.printAll()

if __name__ == "__main__":
    myQueue = Queue()
    myQueue.enqueue(10)
    myQueue.enqueue(1)
    myQueue.enqueue(1)
    myQueue.enqueue(3)
    myQueue.enqueue(9)
    myQueue.enqueue(6)
    myQueue.enqueue(111)
    myQueue.enqueue(2)
    print("Queue: {} and Minimum is : {}".format(myQueue.printAll(), myQueue.mini()))
    print("Deque : {}".format(myQueue.dequeue()))
    print("Queue: {} and Minimum is : {}".format(myQueue.printAll(), myQueue.mini()))
    print("Deque : {}".format(myQueue.dequeue()))
    print("Queue: {} and Minimum is : {}".format(myQueue.printAll(), myQueue.mini()))
    print("Deque : {}".format(myQueue.dequeue()))
    print("Queue: {} and Minimum is : {}".format(myQueue.printAll(), myQueue.mini()))
    print("Deque : {}".format(myQueue.dequeue()))
    print("Queue: {} and Minimum is : {}".format(myQueue.printAll(), myQueue.mini()))
    print("Deque : {}".format(myQueue.dequeue()))
    print("Queue: {} and Minimum is : {}".format(myQueue.printAll(), myQueue.mini()))
    myQueue.enqueue(0)
    print("Queue: {} and Minimum is : {}".format(myQueue.printAll(), myQueue.mini()))
    myQueue.enqueue(-1)
    print("Queue: {} and Minimum is : {}".format(myQueue.printAll(), myQueue.mini()))
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    print("Queue: {} and Minimum is : {}".format(myQueue.printAll(), myQueue.mini()))
    myQueue.dequeue()
    myQueue.dequeue()
    print("Queue: {} and Minimum is : {}".format(myQueue.printAll(), myQueue.mini()))
    myQueue.enqueue(8)
    print("Queue: {} and Minimum is : {}".format(myQueue.printAll(), myQueue.mini()))

"""   --------------------------- OUTPUT ------------------------------------
Queue: [10, 1, 1, 3, 9, 6, 111, 2] and Minimum is : 1
Deque : 10
Queue: [1, 1, 3, 9, 6, 111, 2] and Minimum is : 1
Deque : 1
Queue: [1, 3, 9, 6, 111, 2] and Minimum is : 1
Deque : 1
Queue: [3, 9, 6, 111, 2] and Minimum is : 2
Deque : 3
Queue: [9, 6, 111, 2] and Minimum is : 2
Deque : 9
Queue: [6, 111, 2] and Minimum is : 2
Queue: [6, 111, 2, 0] and Minimum is : 0
Queue: [6, 111, 2, 0, -1] and Minimum is : -1
Queue: [0, -1] and Minimum is : -1
Queue: [] and Minimum is : None
Queue: [8] and Minimum is : 8
"""







