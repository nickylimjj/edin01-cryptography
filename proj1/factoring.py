import numpy as np
import sys
import os

def populate_table (T, N):
    """
    DESC:   generate suitable r values 
    INPUT:  T - 2-D table to populate, with columns
                i, r r^2 mod N, factors
    OUTPUT: filled table
    """
    # TODO
    return T

def generate_matrix (M):
    """
    DESC:   generate a matrix of 1s and 0s mod 2
    INPUT:  M - 2-D matrix to populate,
                size L x |F|
    OUTPUT: filled matrix
    """
    # TODO
    return M

def test_solution(solution, F, N):
    """
    DESC:   parses a bit-string across a factorbase and
            determine if it is a valid solution
    INPUT:  solution - bit string to test
            F - factor base
            N - number N = pq to factor
    OUTPUT: p,q - valid solution to factor N,
            0,0 if not valid
    """
    return 0, 0

if __name__ == "__main__":

     # our N
    N = 89692892645583511288289L
    test_N1 = 323       # 17 * 19
    test_N2 = 307561    # 457 * 673
    test_N3 = 31741649  # 4621 * 6969

    # factorbase our choice is size 10
    # TODO f = open('prim_2_24.txt', 'r')
    F = [2,3,5,7,11,13,17,19,23,29]
    # f.close()

    # L = |F| + 2
    L = len(F) + 2
    
    # generate L relations
    table = np.empty([L, len(F)]) 
    
    # find suitable r values
    populate_table(table, N)

    # matrix for gaussian elimination
    M = np.empty([L, len(F)])
    M = generate_matrix(table)

    # save matrix to M.txt
    f = open("M.txt", "w")
    # TODO: write to M.txt
    f.close()

    # find a nullspace of M that works
    # we run Gauss.exe
    os.system("./GaussBin.exe M.txt X.txt")

    f = open("X.txt","r")
    for solution in f.readlines():
        #TODO test solution
        p, q = test_solution(solution, N)
        if (p != 0 and q != 0):
            print "p=%\tq=%".format(p,q)
        
