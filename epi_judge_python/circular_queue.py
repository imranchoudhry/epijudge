from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity):
        # TODO - you fill in here.
        self.capacity = capacity
        self.data = [None] * capacity
        self.tail = -1
        self.head, self.size1 = 0, 0
        return

    def enqueue(self, x):
        # TODO - you fill in here.

        if self.size1>= self.capacity:
            #time to resize
            new_array = [None] * (self.capacity*2)
            if self.tail >= self.head:
                tail = 0
                for i in range(self.head, self.tail+1):
                    new_array[i -self.head] = self.data[i]
                    tail = i -self.head
            else: # self.tail< self.head
                tail = 0
                for i in range(self.head, len(self.data)):
                    new_array[i -self.head] = self.data[i]
                    tail = i - self.head
                for j in range(0, self.tail+1):
                    new_array[tail+1] = self.data[j]
                    tail +=1
            self.data = new_array
            self.capacity = self.capacity*2
            self.head = 0
            self.tail = tail


        self.tail = (self.tail+1)%self.capacity
        self.data[self.tail] = x
        self.size1 +=1
        return

    def dequeue(self):
        # TODO - you fill in here.
        head_object = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head+1)%self.capacity
        self.size1-=1
        return head_object

    def size(self):
        # TODO - you fill in here.
        return self.size1


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
