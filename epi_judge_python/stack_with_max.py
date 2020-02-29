from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def empty(self):
        # TODO - you fill in here.
        return len(self.stack)==0


    def max(self):
        # TODO - you fill in here.
        return self.max_stack[-1] 

    def pop(self):
        # TODO - you fill in here.
        try:
            t = self.stack.pop()
            if self.max()==t:
                self.max_stack.pop()
        except IndexError:
            raise
        return t

    def push(self, x):
        # TODO - you fill in here.
        self.stack.append(x)
        if len(self.max_stack)==0:
            self.max_stack.append(x)
        elif self.max() <= x:
            self.max_stack.append(x)
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
