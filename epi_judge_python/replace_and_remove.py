import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    write_index = 0
    a_count = 0
    for i in range(size):
        if s[i] != 'b':
            s[write_index] = s[i]
            write_index += 1
        if s[i] == 'a':
            a_count += 1
    print(s)

    read_pointer = write_index
    write_index2 = write_index + a_count
    write_index2 -= 1

    for i in reversed(range(read_pointer)):
        if s[i] == 'a':
            s[write_index2] = 'd'
            s[write_index2 -1] = 'd'
            write_index2 -=2
        else:
            s[write_index2] = s[i]
            write_index2 -=1

    return write_index + a_count

def replace_and_remove2(size, s):
    # TODO - you fill in here.
    for i in reversed(range(len(s))):
        if s[i]=='b':
            s[i]=''
    for i in reversed(range(len(s))):
        if s[i]=='a':
            index = i
            while s[index+1] != "":
                index += 1
            while index > i:
                s[index+1] = s[index]
                index -= 1
            s[i] = 'd'
            s[i+1] = 'd'
    s = [elt for elt in s if elt]
    print(s)

    return len(s)


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
