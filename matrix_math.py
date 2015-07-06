"""Implement these linear algebra functions:
    vector addition and subtraction
    vector multiplication by a scalar
    mean of multiple vectors
    dot product
    magnitude
    matrix addition and subtraction
    matrix multiplication by a scalar
    matrix multiplication by a vector
    matrix multiplication by a matrix"""

import math

class ShapeException(Exception):
    pass


def shape(vector_or_matrix):
    """shape takes a vector or matrix and returns a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    #if a vector, return (#rows,)
    # matrixxx = [[1, 2],
    #       [2, 1],
    #       [1, 2]]
    # should return (3,2)
    # vectorrr = [3,2]
    # should return (2,)
    if type(vector_or_matrix[0]) is int:
        return ((len(vector_or_matrix)),)
    if type(vector_or_matrix[0]) is list:
        return ((len(vector_or_matrix),len(vector_or_matrix[0])))


def vector_add(first_vector, second_vector):
    """
    [a b]  + [c d]  = [a+c b+d]

    Matrix + Matrix = Matrix
    v = [1, 3, 0]
    w = [0, 2, 4]
    vector_add(v, w) == [1, 5, 4]
    """
    idx = 0
    added_vector = []
    print(first_vector)
    for num in first_vector:
        added_vector.append((first_vector[idx] + second_vector[idx]))
        idx += 1
    return added_vector


def vector_add_is_communicative():
    pass


def vector_sub(first_vector, second_vector):
    idx = 0
    added_vector = []
    print(first_vector)
    for num in first_vector:
        added_vector.append((first_vector[idx] - second_vector[idx]))
        idx +=1
    return added_vector

    pass


def vector_sub_checks_shapes():
    pass


def vector_sum():
    pass


def vector_sum_checks_shapes():
    pass


def test_dot():
    pass


def dot_checks_shapes():
    pass


def vector_multiply():
    pass


def vector_mean():
    pass


def magnitude():
    pass


def shape_matrices():
    pass


def matrix_row():
    pass


def matrix_col():
    pass


def matrix_scalar_multiply():
    pass


def matrix_vector_multiply():
    pass


def matrix_vector_multiply_checks_shapes():
    pass


def matrix_matrix_multiply():
    pass


def matrix_matrix_multiply_checks_shapes():
    pass

if __name__ == '__main__':
    print(shape([3,4]))
    print(type(shape([3,4])))
    print(shape([[1,2,3],[2,3,4],[5,6,7]]))
    print(vector_add([1,2,3],[5,6,7]))
    print(vector_sub([1,2,3],[5,6,7]))

