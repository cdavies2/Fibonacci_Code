# One of the fastest ways to compute Fn100000 is by matrix exponentiation
# It is important to use an exponentiation by squaring algorithm
import sys
sys.set_int_max_str_digits(0) #this allows for the entire result of Fn1000000 to be output
def columns(M):
    # [list([list(val) for val in zip(*[col])]) for col in list(zip(*M))]
    return [
        [[M[i][j]] for (i, row) in enumerate(M)]
        for (j, val) in enumerate(M[0])
    ]


def dot(u, v):
    return sum([ui * v[i][0] for (i, ui) in enumerate(u)], 0)


def mmult(M1, M2):
    M2_cols = columns(M2)
    return [[dot(row, col) for col in M2_cols] for row in M1]

def msq(M):
    return mmult(M, M)

def exp_by_squaring(x, n):
    if n==0:
        return [[1,0], [0,1]] #this is the 2x2 identity matrix, if any matrix is multiplied by it, the result will be the given matrix
    elif(n%2==0):
        return exp_by_squaring(msq(x), n/2)
    else:
        return mmult(x, (exp_by_squaring(msq(x), (n-1)/2)))

mat1=[[1, 2], [3, 4]]
mat2=[[1, 2], [3, 4]] #test matrices

print(mmult(mat1, mat2)) #test that matrix_multi works

fibMat=[[1, 1], [1, 0]]

print(mmult(fibMat, fibMat))

print(exp_by_squaring(fibMat, 2)) #test that the matrix works

print(exp_by_squaring(fibMat, 5))

mat_1000=exp_by_squaring(fibMat, 1000)
print(mat_1000)

fn_1000=mat_1000[0][1]
print(fn_1000)

mat_1000000=exp_by_squaring(fibMat, 1000000)
print(mat_1000000)

fn_1000000=mat_1000000[0][1]

#the top right corner and bottom left corner of the matrix contains the fn of the power you're raising to

def get_length(fn):
    length=len(str(fn))
    return length

print("The length of fn1000 is", get_length(fn_1000), "digits")
print("The length of fn1000000 is", get_length(fn_1000000), "digits")