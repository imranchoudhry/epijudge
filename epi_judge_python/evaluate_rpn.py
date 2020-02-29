from test_framework import generic_test


def evaluate(expression):
    # TODO - you fill in here.
    operators = {'*':'*', "/":"//" ,"-":"-", "+":"+"}
    stack = []
    for e in expression.split(","):
        #print(e)
        if e != ",":
            if e in operators:
                b = stack.pop()
                a = stack.pop()
                #print(f"{a}{e}{b}")
                op = operators[e]
                new_term = eval(f"{a}{op}{b}")
                #print(new_term)
                stack.append(new_term)
            else:
                stack.append(e)

    return int(stack.pop())


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
