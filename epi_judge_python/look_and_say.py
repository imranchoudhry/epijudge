from test_framework import generic_test


def look_and_say(n):
    # TODO - you fill in here.
    result = "1"
    while n>1:
        S2 = ""
        prev = result[0]
        count = 1
        for i in result[1:]:
            if i==prev:
                count +=1
            if i!= prev:
                S2 += str(count) + str(prev)
                count = 1
            prev = i
        S2 += str(count) + str(prev)
        result = S2
        n-=1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
