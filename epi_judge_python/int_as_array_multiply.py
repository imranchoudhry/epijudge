from test_framework import generic_test



def multiply(num1, num2):
    p = [0 for i in range(len(num1) + len(num2))]
    r = [list(p) for i in range(len(num2))]
    if (num1[0] * num2[0])<0:
        sign = -1
    else:
        sign = 1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])
    p_index = len(p)
    r_index = -1
    for i in reversed(range(len(num2))):
        factor1 = num2[i]
        p_index -= 1
        r_index += 1
        p_offset = p_index
        for j in reversed(range(len(num1))):
            factor2 = num1[j]
            product = factor1 * factor2
            r[r_index][p_offset] = product
            p_offset -= 1
    result = [sum(i) for i in zip(*r)]

    carry = 0
    rem = 0
    for i in reversed(range(len(result))):
        val = result[i]
        val += carry
        rem = val % 10
        carry = val // 10
        result[i] = rem

    index = 0
    while True:
        #print(result)
        if len(result)==1:
            break
        if result[index]!= 0:
            break
        del result[index]


    result[0] = result[0] * sign
    return result
"""
def multiply2(num1, num2):
    # TODO - you fill in here.
    results = [[] * ]
    max_len = 0
    for i in range(len(num2)):
        result = [0] * i
        [0] * i
        for j in reversed(range(len(num1))):
            result = [num2[i] * num1[j]] + result
        max_len = max(len(result), max_len)
        results.append(result)
    for i in reversed(range(max_len)):
        for result in results:
            if i < len(result)

    return []
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
