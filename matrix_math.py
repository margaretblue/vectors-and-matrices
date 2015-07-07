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
    [x for x in range(10)]
    """
    return [first_vector[x] + second_vector[x] for x in range(len(first_vector))]
    #idx = 0
    #added_vector = []
    #print(first_vector)
    #for num in first_vector:
    #    added_vector.append((first_vector[idx] + second_vector[idx]))
    #    idx += 1
    #return added_vector


def vector_sub(first_vector, second_vector):
    return [first_vector[x] - second_vector[x] for x in range(len(first_vector))]


def vector_sub_checks_shapes():
    pass

def weird_sum(a_vector):
    """Given a list(vector) of unknown size, returns sum of that list.Expected input is the nth item of each arg vector"""
    if len(a_vector) == 1:
        return a_vector[0]
    else:
        return a_vector[0] + weird_sum(a_vector[1:])

def vector_sum(*args):
    summiest_vector = []
   # summiest_vector.append(first_vector[0]+ second_vector[0] + third_vector[0])
   # summiest_vector.append(first_vector[1]+ second_vector[1] + third_vector[1])
   # summiest_vector.append(first_vector[2]+ second_vector[2] + third_vector[2])
    index = 0
    summiest_vector = []
    # do something len(args) times
    for x in range(len(args)):
        temporary_vector = []
        for x in range(len(args)):
            
        #need list of xth in each vector
        temporary_vector =
        summiest_vector.append(args[x] + args[x+1] )
        print(x)
    #    summiest_vector.append(args[x]+ second_vector[x] + third_vector[x])
    #return summiest_vector
#    """vector_sum can take any number of vectors and add them together.
#    v = [1, 3, 0]
#    w = [0, 2, 4]
#    u = [1, 1, 1]
#    y = [10, 20, 30]
#    z = [0, 0, 0]
#    assert vector_sum(v, w, u, y, z) == [12, 26, 35]"""
    # [pow(2,x) for x in range(10) if x%2 ==0] # Collection, iteration, separation
    # take vector[0], add it to the vector[1], creating a summed_vector. then to the summed vector add vector[3]


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
    #    v = [1, 3, 0]
    #    w = [0, 2, 4]
    #    u = [1, 1, 1]
    print(vector_sum([1,3,0],[0,2,4],[1,1,1]))


