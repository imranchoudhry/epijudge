from test_framework import generic_test


class Queue:
    def __init__(self):
        self.deq = []
        self.enq = []

    def enqueue(self, x):
        # TODO - you fill in here.
        self.enq.append(x)
        #return

    def dequeue(self):
        # TODO - you fill in here.
        if not self.deq:
            self.deq = self.enq[::-1]
            self.enq = []
        return self.deq.pop()


def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))
