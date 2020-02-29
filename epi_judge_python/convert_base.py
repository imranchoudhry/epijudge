from test_framework import generic_test


def convert_base(num_as_string, b1, b2):
    # TODO - you fill in here.
    t = {10:"A", 11:'B', 12:"C", 13:"D", 14:"E", 15:"F", "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

    if num_as_string=='0' or num_as_string=='-0':
        return num_as_string
    result = 0

    is_neg = False
    if num_as_string[0]== '-':
        is_neg = True
        num_as_string = num_as_string[1:]
    power = len(num_as_string)

    for digit in num_as_string:
        power -=  1
        if digit in t:
            digit = t[digit]
        else:
            digit = int(digit)
        #digit = t.get(digit, int(digit))
        result += digit * b1**(power)

    # result is num_as_string in base 10
    b2_power = 0

    while True:
        if result // (b2**b2_power) <= 0:
            break
        b2_power += 1

    final_string_list = []
    for i in reversed(range(b2_power)):
        coeff = result//(b2**i)
        result = result - coeff*(b2**i)
        final_string_list.append(coeff)


    if is_neg:
        final_string = "-" 
    else:
        final_string=""
    for i in final_string_list:
        final_string = final_string + t.get(i,str(i))


    return final_string


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
