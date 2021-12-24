import sys

dims = [10, 20, 30, 40, 30, 50, 60]
count = [0]


def matrix_chain_multiplication(dimensions):
    # first we define our cost matrix which will be of dimensions nxn, where n = number of matrices
    n = len(dimensions)
    cost = [[0 for i in range(n)] for j in range(n)]
    s = [['' for i in range(n)] for j in range(n)]

    # fill the trivial solution. i.e cost of multiplying single matrix is 0
    for i in range(n):
        cost[i][i] = 0

    # Now we calculate cost of non-trivial solutions. i.e optimal cost of multiplying >=2 matrices
    for length in range(2, n + 1):
        # we've to calculate this cost from every starting position in the multiplication string
        for i in range(1, n - length + 1):
            # from i, we multiply number of matrices given by length i.e from i to i+length
            j = i + length - 1  # if i=0, then j=2 i.e we multiply A0 and A1. we don't consider A2.
            # initialize cost[i][j] to + infinity
            cost[i][j] = sys.maxsize
            # to calculate the solution for sub problem Ai to Aj, we have to further divide to Ai..Ak and Ak..Aj for
            # all k between i and j such that i<=k<j
            for k in range(i, j):
                cur_cost = cost[i][k] + cost[k + 1][j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                if cur_cost < cost[i][j]:
                    cost[i][j] = cur_cost
                    s[i][j] = k
    print_matrix(cost)
    return cost[1][n - 1], s


def print_optimal_parens(s, i, j):
    if i == j:
        return 'A{}'.format(i)
    else:
        return "({}{})".format(print_optimal_parens(s, i, s[i][j]), print_optimal_parens(s, s[i][j] + 1, j))


def print_matrix(matrix):
    for row in matrix:
        print(row)


def brute_force_mcm(dimensions, i, j, s):
    if i == j:
        return 0
    cost = sys.maxsize
    for k in range(i, j):
        count[0] += 1
        cur_cost = brute_force_mcm(dimensions, i, k, s) + brute_force_mcm(dimensions, k + 1, j, s) + \
                   dimensions[i - 1] * \
                   dimensions[k] * dimensions[j]
        if cur_cost < cost:
            cost = cur_cost
            s[i][j] = k
    return cost


def memoization_mcm(dimensions, i, j, s, m):
    if i == j:
        m[i][j] = 0
        return m[i][j]
    elif m[i][j] < sys.maxsize:
        return m[i][j]
    for k in range(i, j):
        count[0] += 1
        cur_cost = memoization_mcm(dimensions, i, k, s, m) + memoization_mcm(dimensions, k + 1, j, s, m) + \
                   dimensions[i - 1] * dimensions[k] * dimensions[j]
        if cur_cost < m[i][j]:
            m[i][j] = cur_cost
            s[i][j] = k
    return m[i][j]


if __name__ == '__main__':
    min_cost, s = matrix_chain_multiplication(dims)
    n = len(dims) - 1
    print(min_cost, print_optimal_parens(s, 1, n))
    count = [0]
    s = [['' for i in range(n+1)] for j in range(n+1)]
    print("brute_force solution = ", brute_force_mcm(dims, 1, n, s), print_optimal_parens(s, 1, n))
    print("brute force calculated ", count, "sub problems")
    s = [['' for i in range(n+1)] for j in range(n+1)]
    m = [[sys.maxsize for i in range(n+1)] for j in range(n+1)]
    count = [0]
    print("memoization solution = ", memoization_mcm(dims, 1, n, s, m), print_optimal_parens(s, 1, n))
    print("memoization calculated ", count, "sub problems")
