from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    # TODO - you fill in here. 
    # recieved 9 x 9 array
    def check_row(row_index):
        d = {}
        row = partial_assignment[row_index]
        for num in row:
            if num in d and num!=0:
                return False
            d[num]=1
        return True

    def check_row2(nums):
        d = {}
        for num in nums:
            if num in d and num!=0:
                return False
            d[num]=1
        return True

    def check_col(col_index):
        d = {}
        for i in range(9):
            num = partial_assignment[i][col_index]
            if num in d and num!=0:
                return False
            d[num]=1
        return True

    def get_subarray(partial,row,col):
        nums = []
        for i in range(row,row+3):
            for j in range(col, col+3):
                nums.append(partial[i][j])
        return nums
    
    def check_subarray(partial):
        indexs = set()
        for i in range(0,9,3):
            for j in range(0,9,3):
                indexs.add((i,j))
        for index in indexs:
            subarray = get_subarray(partial,index[0],index[1])
            if not check_row2(subarray):
                return False
        return True
    print(type(all(check_row(i) for i in range(9))))
    print(type((all(check_row(i) for i in range(9)), all(check_col(j) for j in range(9)), check_subarray(partial_assignment))))
    return all((all(check_row(i) for i in range(9)), all(check_col(j) for j in range(9)), check_subarray(partial_assignment)))

    """
    vals = []
    print('wtf')
    for i in range(9):
        print(i)
        print(check_row(i))
    print('bo')
    
    vals.append(all(check_row(i) for i in range(9)))
    vals.append(all(check_col(j) for j in range(9)))
    vals.append(check_subarray(partial_assignment))
    """

    #return all(vals)

    #def check_subarray(partial):
        #all(check_row(i) for i in range(9), check_col(i) for range(9), )
        #for i in range(9):



    #return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
