from test_framework import generic_test


def matrix_search(A, x):
    # TODO - you fill in here.

    def get_elt(row,col):
        return A[row][col]
    
    number_of_cols = len(A[0]) # this is how many elements are in a row
    number_of_rows = len(A) # this is how many elements are in a column

    curr_index = (0, number_of_cols-1)

    while curr_index[0] < number_of_rows and 0<= curr_index[1]:
        curr_elt = get_elt(*curr_index)
        if curr_elt < x:
            curr_index = (curr_index[0]+1, curr_index[1])
        elif curr_elt==x:
            return True
        else: #curr_elt > x
            curr_index = (curr_index[0], curr_index[1]-1)



    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
