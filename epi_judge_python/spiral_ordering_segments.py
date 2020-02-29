from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    # TODO - you fill in here.
    if not square_matrix:
        return []
    n = len(square_matrix[0])
    # we have a n x n matrix
    result = []
    def print_row(row_index, elements, start=0, end=0, rev = False):
        curr_row = square_matrix[row_index]
        if rev:
            our_iterable = range(elements, end, -1)
        else:
            our_iterable = range(start, elements)
        for i in our_iterable:
            result.append(curr_row[i])

    def print_col(col_index, elements, start=0, end=0, rev = False):
        if rev:
            our_iterable = range(elements, end, -1)
        else:
            our_iterable = range(start, elements)

        for i in our_iterable:
            elt = square_matrix[i][col_index]
            result.append(elt)

    layer = n
    x = -1
    cells = n
    if (n%2==0):
        terminal_case = 2
    elif (n%2==1):
        terminal_case = 1
    while cells > terminal_case:
        x += 1
        print_row(n - layer, layer - 1, start=x)
        print_col(layer-1, layer - 1, start=x)
        print_row(layer-1, layer-1, end=x, rev= True)
        print_col(n - layer, layer - 1, end=x, rev=True)
        layer -= 1
        cells -= 2
    
    if terminal_case == 2:
        result.append(square_matrix[(n//2)-1][(n//2)-1])
        result.append(square_matrix[(n//2)-1][(n//2)])
        result.append(square_matrix[(n//2)][(n//2)])
        result.append(square_matrix[(n//2)][(n//2)-1])
    else:
        result.append(square_matrix[n//2][n//2])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
