### Fill in each function below. Each function should be a one-liner.
import numpy as np

# Part One:  Matrix vs Vectors
#==============================

def one():
    '''
    INPUT: NONE
    OUTPUT: A numpy row vector of 100 sequential numbers starting at zero and ending at 99. (matrix)

    Create a row vector with numpy (1 x 100).

    Example:
    >>>
    >>> answer = one()
    >>> print answer
    >>> [[ 0  1  2  3  4 ... 99 ]]
    '''
    return np.arange(0, 100).reshape(1, 100)


def two():
    '''
    INPUT: NONE
    OUTPUT: A column vector of 100 sequential floats all between 0 and 50. (matrix)

    Create a column vector with numpy (100 x 1).

    Example:
    >>>
    >>> cv = two()
    >>> print cv
    >>> [[  0.        ]
         [  0.50505051]
         [  1.01010101]
         ...
          [ 50.        ]]
    '''
    return np.linspace(0.0, 50.0, num=100).reshape(100, 1)


def three():
    '''
    INPUT: NONE
    OUTPUT: A 6 x 6 numpy matrix

    Create a square 6 by 6 matrix

    Example:
    >>>
    >>> M = three()
    >>> print M
    >>> [[ 0  1  2  3  4  5]
         [ 6  7  8  9 10 11]
         [12 13 14 15 16 17]
         [18 19 20 21 22 23]
         [24 25 26 27 28 29]
         [30 31 32 33 34 35]]
    '''
    return np.arange(0, 36).reshape(6, 6)


def four():
    '''
    INPUT: NONE
    OUTPUT: A random 2 x 3 numpy matrix

    Create a random 2 x 3 matrix.
    You should be able to do this with one command  (look at the numpy random module).

    Example:
    >>>
    >>> M = four()
    >>> print M
    >>> [[7 8 2]
         [9 4 3]]
    '''
    return np.random.randint(10, size=(2, 3))


def five():
    '''
    Create a 6 x 6 identity matrix.

    INPUT: NONE
    OUTPUT: 6 x 6 identity matrix

    Example:
    >>> I = five()
    >>> print I
    >>> [[ 1.  0.  0.  0.  0.  0.]
         [ 0.  1.  0.  0.  0.  0.]
         [ 0.  0.  1.  0.  0.  0.]
         [ 0.  0.  0.  1.  0.  0.]
         [ 0.  0.  0.  0.  1.  0.]
         [ 0.  0.  0.  0.  0.  1.]]
    '''
    return np.identity(6)


def six():
    '''
    Create a (10 x 10) matrix with sequential ints 0 through 99.

    Example:
    >>> print answer
    >>>> [[ 0  1  2  3  4  5  6  7  8  9]
          [10 11 12 13 14 15 16 17 18 19]
          [20 21 22 23 24 25 26 27 28 29]
          [30 31 32 33 34 35 36 37 38 39]
          [40 41 42 43 44 45 46 47 48 49]
          [50 51 52 53 54 55 56 57 58 59]
          [60 61 62 63 64 65 66 67 68 69]
          [70 71 72 73 74 75 76 77 78 79]
          [80 81 82 83 84 85 86 87 88 89]
          [90 91 92 93 94 95 96 97 98 99]]
    '''
    return np.arange(0, 100).reshape(10, 10)


def seven(M=six()):
    '''
    INPUT: Matrix output from function six.
    OUTPUT:  First three columns of Matrix from function six.

    Call function six() and save it as M,
    Return just the first 3 columns of M

    Example:
    >>> M = six()
    >>> print seven(M)
    >>> [[ 0  1  2]
         [10 11 12]
         [20 21 22]
         [30 31 32]
         [40 41 42]
         [50 51 52]
         [60 61 62]
         [70 71 72]
         [80 81 82]
         [90 91 92]]
    '''

    return M[:, 0:3]


def eight(M=six()):
    '''
    INPUT: Matrix output from function six.
    OUTPUT:  Last two ROWS of Matrix from function six.

    Example:
    >>> M = six()
    >>> print eight(M)
    >>> [[80 81 82 83 84 85 86 87 88 89]
         [90 91 92 93 94 95 96 97 98 99]]
    '''
    return M[-2:, :]


# PART 2: SCALAR OPERATIONS
# =========================

def nine():
    '''
    INPUT: None
    OUTPUT: A numpy array with values [ [0,1,2,3,4,5,6,7,8,9] ]

    Create this numpy array (called V): [ [0,1,2,3,4,5,6,7,8,9] ]
    '''
    V = np.arange(0, 10)
    return V


def ten(V=nine()):
    '''
    INPUT: V ( matrix from nine() )
    OUTPUT: [[ 0.5  1.5  2.5  3.5  4.5  5.5  6.5  7.5  8.5  9.5]]

    Do a scalar addition by 0.5 to V.
    '''
    return np.add(V, 0.5)


def eleven(V=nine()):
    '''
    INPUT: V (matrix from nine() )
    Do a scalar multiple by -2.
    OUTPUT:  [[  0  -2  -4  -6  -8 -10 -12 -14 -16 -18]]
    '''
    return np.multiply(V, -2.0)


def twelve(V=nine(), VB=ten()):
    '''
    INPUT: V ( matrix from nine() )
    OUTPUT: answer = V+B

    Create a 1 by 10 vector 'B',
    that when added to V,  will yeild the same results as function ten
    V + B = [[ 0.5  1.5  2.5  3.5  4.5  5.5  6.5  7.5  8.5  9.5]]

    Return your answer
    '''
    B = VB - V
    return B


# PART 3: MATRIX / VECTOR Multiplication
# ======================================
def thirteen(n=3):
    '''
    Create column vector with 3 ints, called as column_vector.
    Create a row vector with 3 ints, called as row_vector.
    Create 3 x 3 square matrix called and square_matrix:
    Return as column_vector, row_vector, square_matrix (IN THAT ORDER)
    '''
    column_vector = np.random.randint(1, 100, size=(n)).reshape(n, 1)
    row_vector = np.random.randint(1, 100, size=(n)).reshape(1, n)
    square_matrix = np.random.randint(1, 100, size=(n, n))
    return column_vector, row_vector, square_matrix


def fourteen(column_vector=thirteen()[0], row_vector=thirteen()[1]):
    '''
    INPUT: Using column_vector and row_vector from thirteen() as the inputs
    OUTPUT:  n x m shaped vector where n is number of rows in row_vector and m is number of cols in col_vec

    Perform a vector vector multiply on column_vector and row_vector.
    This should output a n x m matrix where n is the number of rows in row_vector and m is the number of columns in column_vector.
    Say column_vector is a 2 x 1 and row_vector is a 1 x 3, output will be a 2 x 3 matrix.

    '''
    return np.multiply(row_vector, column_vector)


def fifteen(column_vector=thirteen()[0], row_vector=thirteen()[1],
            square_matrix=thirteen()[2]):
    '''
    INPUT: Using column_vector and row_vector from thirteen() as the inputs
    OUTPUT:  return c_answer, r_answer

    c_answer is the matrix multiplication of column_vector and square_matrix
    r_answer is the matrix multiplication of row_vector and square_matrix


    For both column_vector and row_vector, matrix multiply by square_matrix.
    One will have to go on the left and one will have to go on the right.
    If it lets you do both directions,
        you probably are doing elementwise multiplication instead of matrix multiplication!

    Make sure you return c_answer first
    return c_answer, r_answer
    '''
    c_answer = np.dot(square_matrix, column_vector)
    r_answer = np.dot(row_vector, square_matrix)
    return c_answer, r_answer


def sixteen(column_vector=thirteen()[0], row_vector=thirteen()[1]):
    '''
    Compute the dot product of row_vector and column_vector.
    '''
    dot = sum([column_vector[i, 0] * row_vector[0, i]
              for i in range(len(column_vector))])
    return dot


# PART 4: MATRIX MATRIX MULTIPLICATION
# ====================================
def seventeen():
    '''
    question one:  If A is a 3 x 2 and B is a 4 x 3, can you matrix multiply them (AB)?
    If question_one is true, set variable 'answer_one' equal to True, if false, set 'answer_one' equal to False

    question two: If so, what is the shape?
    If answer_one is True, set variable 'answer_two' equal to the shape of the matrix, if False, set 'answer_two' equal to None

    question three:  Can you matrix multiply them in the other direction (BA)?
        If true, set variable 'answer_three' equal to True, if false, set 'answer_three' equal to False

    four:  If so, what's the shape of that?
        If answer_three is True, set variable 'answer_four' to be the shape of the matrix in answer_three, if False set 'answer_four' equal to None

    OUTPUT: answer_one BOOLEAN,
            answer_two Tuple or None,
            answer_three BOOLEAN,
            answer_four Tuple or None
    '''

    return False, None, True, (4, 2)


def eighteen():
    '''
    Create a random 3 x 6 matrix as 'rand_matrix'.
    Matrix multiply rand_matrix and the transpose of rand_matrix.

    INPUT: None
    OUTPUT: answer_one  NUMPY MATRIX

    '''
    rand_matrix = np.random.randint(1, 100, size=(3, 6))
    trans_rand_matrix = np.transpose(rand_matrix)
    np.dot(rand_matrix, trans_rand_matrix)
    return np.dot(rand_matrix, trans_rand_matrix)




# PART 5: Elementwise Matrix Operations
#======================================
def nineteen():
    '''
    Create 2 random 6 x 2 matrices as A and B.
    Square A (this will be the same shape).
    Add, subtract, multiply and divide A and B (This will be the same shape).

    INPUT: None
    OUTPUT: answer_square, answer_add, answer_subtract, answer_multiply,
            answer_divide
    '''
    A = np.random.randint(1, 100, size=(6, 2))
    B = np.random.randint(1, 100, size=(6, 2))
    return (np.square(A), np.add(A, B), np.subtract(A, B), np.multiply(A, B),
            np.divide(A, B))


def twenty():
    '''
    Create two matrices, A and B.
    Make Matrix 'A' a 4x1 shaped matrix with values 1 through 4.
    A = [ [1], [2], [3], [4] ]

    Make matrix B a 1x3 matrix that look like this:
    B = [[ 100.  200.  300.]]

    answer = use numpy to add Matrix A to Matrix B
    return answer
    '''
    A = np.arange(1, 5).reshape(4, 1)
    B = np.multiply(np.arange(1, 4), 100.).reshape(1, 3)
    return np.add(B, np.transpose(B))



def twenty_one():
    '''
    Create a 10 x 10 matrix of FLOATS that looks just like this
    DO NOT JUST COPY AND PASTE THIS MATRIX, YOU MUST CREATE THIS PROGRAMMATICALLY

    Hint, np.linspace()

    M = [[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.]
         [ 10.  11.  12.  13.  14.  15.  16.  17.  18.  19.]
         [ 20.  21.  22.  23.  24.  25.  26.  27.  28.  29.]
         [ 30.  31.  32.  33.  34.  35.  36.  37.  38.  39.]
         [ 40.  41.  42.  43.  44.  45.  46.  47.  48.  49.]
         [ 50.  51.  52.  53.  54.  55.  56.  57.  58.  59.]
         [ 60.  61.  62.  63.  64.  65.  66.  67.  68.  69.]
         [ 70.  71.  72.  73.  74.  75.  76.  77.  78.  79.]
         [ 80.  81.  82.  83.  84.  85.  86.  87.  88.  89.]
         [ 90.  91.  92.  93.  94.  95.  96.  97.  98.  99.]]
    '''
    M = np.multiply(100, np.round(np.linspace(0, 1, 100, endpoint=False), 2))
    return M.reshape(10, 10)



def twenty_two(M=twenty_one()):
    '''
    Calculate the sum, mean, and standard deviation of the matrix we created in function twent_one
    INPUT: M is matrix from function twenty_one
    OUTPUT:  M_sum, M_mean, M_std  (please return variables in that order)

    Example:
    M_sum = 4950.0
    '''
    M_sum = np.sum(M)
    M_mean = np.mean(M)
    M_std = np.std(M)
    return M_sum, M_mean, M_std



def twenty_three(M):
    '''
    Calculate the column wise sums, mean and standard deviation of the matrix.

    INPUT: M is matrix from function twenty_one
    OUTPUT:  col_sum, col_mean, col_std  (please return variables in that order)

    Example
    col_sum = [ 460.  470.  480.  490.  500.  510.  520.  530.  540.  550.]
    '''
    col_sum = np.sum(M, axis=0)
    col_mean = np.mean(M, axis=0)
    col_std = np.std(M, axis=0)
    return col_sum, col_mean, col_std



def twenty_four(M):
    '''
    Calculate the row wise sums, mean and standard deviation of the matrix.

    INPUT: M is matrix from function twenty_one
    OUTPUT:  row_sum, row_mean, row_std   (please return variables in that order)

    Example:
    row_sum = [  55.  155.  255.  355.  455.  555.  655.  755.  855.  955.]
    '''
    row_sum = np.sum(M, axis=1)
    row_mean = np.mean(M, axis=1)
    row_std = np.std(M, axis=1)
    return row_sum, row_mean, row_std
