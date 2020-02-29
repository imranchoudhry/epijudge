from test_framework import generic_test


def generate_pascal_triangle(n):
    # TODO - you fill in here.
    if n ==1:
        return [1]
    elif n ==2:
        return [[1],[1,1]]
    else:
        res = generate_pascal_triangle(n-1)
        last_row = res[-1]
        print(last_row)
        new_row = [1]+ [last_row[i-1] + last_row[i] for i in range(1,len(last_row))] + [1]
        res.append(new_row)
    return res

def generate_pascal_triangle2(n):
    result = [[1] * (i +1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            result[i][j] = result[i-1][j-1] + result[i-1][j]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))