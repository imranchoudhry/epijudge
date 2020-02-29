from test_framework import generic_test


def shortest_equivalent_path(path):
    # TODO - you fill in here.
    stack = []

    if path[0]=='/':
        stack.append('/')

     
    for symbol in (path.split('/')):
        if not symbol:
            continue
        elif symbol==".":
            continue
        elif symbol=="..":
            if not stack or stack[-1]=="..": stack.append(symbol)
            elif stack: stack.pop()
        else:
            stack.append(symbol)



    if stack and stack[0]=='/':
        stack.pop(0)
        beginwithslash = True
    else:
        beginwithslash = False

    if beginwithslash:
        return '/' + "/".join(stack)
    else:
        return "/".join(stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
