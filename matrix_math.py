"""Implement these linear algebra functions:"""

import math

class ShapeException(Exception):
    pass

# raise ShapeException("Wrong shape")

##TODO
def shape(vector_or_matrix):
    """shape takes a vector or matrix and returns a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    #if a vector, return
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
    if shape(first_vector) != shape(second_vector):
        raise ShapeException("Shape error.")
    return [first_vector[x] + second_vector[x] for x in range(len(first_vector))]
    #idx = 0
    #added_vector = []
    #print(first_vector)
    #for num in first_vector:
    #    added_vector.append((first_vector[idx] + second_vector[idx]))
    #    idx += 1
    #return added_vector


def vector_sub(first_vector, second_vector):
    if shape(first_vector) != shape(second_vector):
        raise ShapeException("Shape error.")
    return [first_vector[x] - second_vector[x] for x in range(len(first_vector))]


def vector_sub_checks_shapes():
    #in test_vector_sub_checks_shapes(), it looks like it doesn't need this function and just uses vector_sub()
    pass

def weird_sum(a_vector):
    """Given a list(vector) of unknown size, returns sum of that list.Expected input is the nth item of each arg vector"""
    if len(a_vector) == 1:
        return a_vector[0]
    else:
        return a_vector[0] + weird_sum(a_vector[1:])


def vector_sum(*vectors):
    idx = 0
    while idx < (len(vectors)-1):
        if shape(vectors[idx]) != shape(vectors[idx+1]):
            raise ShapeException("Shape error.")
        idx += 1
    return \
        [
            sum([vector[x] for vector in vectors])
        for x in range(len(vectors[0]))
        ]


def vector_sum_checks_shapes():
    pass


def dot(a_vector, b_vector):
    multiplied_list = [
        (a_vector[i] * b_vector[i])
        for i in range(len(a_vector))
    ]

    return sum(multiplied_list)


def dot_checks_shapes():
    pass


def vector_multiply(a_vector, multiplier):
    """
    [a b]  *  Z     = [a*Z b*Z]
    Vector * Scalar = Vector
    """
    return [(a_vector[x] * multiplier) for x in range(len(a_vector))]


def vector_mean(*vectors):
    """Take sum of all vectors and divide that by the number of vectors"""
    # use the functions you have!
    return vector_multiply(vector_sum(*vectors), (1/(len(vectors))))


def magnitude(a_vector):
    squares = [
        (a_vector[idx] ** 2) for idx in range(len(a_vector))
        ]
    sum_of_squares = sum(squares)
    return math.sqrt(sum_of_squares)


def shape_matrices(vector_or_matrix):

    return shape(vector_or_matrix)


def matrix_row(a_matrix, row_index):
    """     0 1  <- rows
        0 [[a b]]
        1 [[c d]]
        ^
      columns"""
    return a_matrix[row_index]


def matrix_col(a_matrix, column_index):
    return [a_vector[column_index] for a_vector in a_matrix]

def matrix_scalar_multiply(a_matrix, multiplier):
    return [
        [(num * multiplier) for num in a_matrix[x]]
            for x in range(len(a_matrix))
        ]


def matrix_vector_multiply(a_matrix, a_vector):
    w = [0] * len(a_matrix)
    sum = 0
    for idx in range(len(a_matrix)):
        for i in range(len(a_vector)):
            sum += (a_matrix[idx][i]) * a_vector[i]
        w[idx] = sum
        sum = 0
    return w


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


