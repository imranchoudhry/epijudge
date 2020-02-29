from test_framework import generic_test
import string

def is_palindrome(s):
    # TODO - you fill in here.
    start = 0
    end = len(s) - 1
    while end > start:
        if not s[start].isalnum():
            start +=1
            continue
        if not s[end].isalnum():
            end -=1
            continue
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
