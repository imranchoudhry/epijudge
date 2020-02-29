import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    # TODO - you fill in here.
    def reverse2(s, begin=None, end=None):
        if begin==None:
            begin = 0
        if end ==None:
            end = len(s) -1
        #for i in range(med):
        while begin <= end:
            s[begin], s[end] = s[end], s[begin]
            begin+=1
            end-=1
    
    reverse2(s)
    """
    start= 0
    while True:
        finish = start
        while finish < len(s) and s[finish] !=' ':
            finish += 1
        print(finish)
        if finish == len(s):
            break
        reverse2(s, begin=start, end=finish-1)
        start = finish + 1
    reverse2(s, begin=start, end=len(s)-1)
    """
    def find_spaces(s):
        space_indexs = []
        start = 0
        while True:
            finish = s.find(b' ', start)
            if finish < 0:
                break
            start = finish +1
            space_indexs.append(finish)
        return space_indexs
        """
        for i in range(len(s)):
            finish = s.find(b' ', start)

            print(s[i])
            if s[i]==b' ':
                space_indexs.append(i)
        return space_indexs
        """
    spaces = find_spaces(s)
    #print(spaces)
    begining_index = 0
    for i in spaces:
        reverse2(s,begin=begining_index, end=i-1)
        #print(s)
        begining_index = i +1
    
    reverse2(s,begin=begining_index, end=len(s)-1)

    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
