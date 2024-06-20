# One of the fastest ways to compute Fn100000 is by matrix exponentiation
# It is important to use an exponentiation by squaring algorithm
def columns(M):
    # I am not sure which is more readable here, zip or enumerate.
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
         return 1
    elif n % 2 ==0:
        return exp_by_squaring(msq(x), n/2)
    else:
        val=exp_by_squaring(msq(x), (n-1)/2)
        return mmult(x, val)

mat1=[[1, 2], [3, 4]]
mat2=[[1, 2], [3, 4]] #test matrices

print(mmult(mat1, mat2)) #test that matrix_multi works

fibMat=[[1, 1], [1, 0]]

print(mmult(fibMat, fibMat))

print(exp_by_squaring(fibMat, 5)) #test that the matrix works

#fnMatrix=exp_by_squaring(fibMat, 70)

#fnMillion=fnMatrix[0][1]
#print(fnMillion)