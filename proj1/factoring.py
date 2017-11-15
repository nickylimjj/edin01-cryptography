import numpy as np
import sys
import os
import math as m
import time

def populate_table (T, N, B):
    """
    DESC:   generate suitable r values 
    INPUT:  T - 2-D table to populate, with columns
                i, r r^2 mod N
            B - B-smooth value
    OUTPUT: filled table
    """
    # TODO
    L, _ = T.shape
    i = 0
    k = 1
    j = 0
    Thres = 100

    # fill up entire table
    while i < L:

        r = m.floor(m.sqrt(k*N)) + j
        r2 = r**2 % N

        # check if r2 is B-smooth
        if checkSmooth_(r2,B) != -1:
            T[i] = (k, j, r, r2)
            i += 1
    
        j += 1
        if j >= Thres:
            j %= Thres
            k += 1
    return T

def checkSmooth_(r2,B):
    """
    DESC:   checks if the number r2 is B-smooth
    INPUT:  r2 - integer to be checked
            B - integer to check againsr
    OUTPUT: fac - array of factors. -1 on failure
    """

    # TODO
    curr = r2
    fac = []
    for i in range(2,B):
        if curr % i == 0:
            curr /= i
            fac += [i]

    if curr == 1:
        return fac
    return -1
        

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
    project_N = 89692892645583511288289L
    test_N1 = 323       # 17 * 19
    test_N2 = 307561    # 457 * 673
    test_N3 = 31741649  # 4621 * 6969

    N = test_N1

    print("factoring project")
    print("----------------")
    print("N =\t{}".format(N))

    # factorbase our choice is size 1000
    F_size = 1000
    F = []

    filename = "prim_2_24.txt"
    print("\tloading factorbase {}...".format(filename))

    with open(filename, 'r') as f:
        size = 0
        while size < F_size:
            line = f.readline()         # 10 per line
            for word in line.split():
                F += [word]
                size += 1
                
    f.close()

    B = int(F[-1]) + 1
    print "\t|F| = {}".format(len(F))
    print "\t{}-smooth".format(B)

    # L size specified on website
    L = 1024

    print "\tL = {}".format(len(F))
    
    # generate L relations
    table = np.empty([L, 4]) 
    
    # find suitable r values
    populate_table(table, N, B)
    print "\t table populated..."

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
            print "p={}\tq={}".format(p,q)
        
