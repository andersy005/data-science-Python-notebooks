A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]


def shape(A):
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows, num_cols


print(shape(A))


def get_row(A, i):
    return A[i]


def get_col(A, j):
    return [A_i[j]
            for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):

    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]