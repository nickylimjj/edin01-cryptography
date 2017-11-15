import numpy as np
import string
import sys
import os
import argparse
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
            B - integer to check against
    OUTPUT: fac - dict of factors to exponent. -1 on failure
    """
    curr = r2
    fac = {} 
    for i in range(2,B):
        while curr % i == 0:
            curr /= i
            try:
                fac[i] += 1
            except KeyError:
                fac[i] = 1

    if curr == 1:
        return fac
    return -1
        

def generate_matrix (table,F):
    """
    anthony-input: F
    DESC:   generate a matrix of 1s and 0s mod 2
    INPUT:  Table
    OUTPUT: filled matrix
    """
    # TODO
    L,_ = table.shape
    M = np.zeros((L,len(F)))
    rownum = 0
    for row in table:
	r2 = row[3]
	B = F[-1]+1
	d = checkSmooth_(r2,B)
	for key,value in d.iteritems():
	    ind = F.index(key)
	    M[rownum][ind] = value%2
	rownum += 1
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
    # TODO
    return 0, 0

if __name__ == "__main__":

    # parse cmdline args
    parser = argparse.ArgumentParser(description='Factoring Algorithm')
    parser.add_argument('--generate','-g', action='store_true',
                        help='generates r values')

    args = parser.parse_args()

    # our N
    project_N = 89692892645583511288289L
    test_N1 = 323       # 17 * 19
    test_N2 = 307561    # 457 * 673
    test_N3 = 31741649  # 4621 * 6969

    N = test_N1

    prime_file = "prim_2_24.txt"
    in_file = "in.mat"
    out_file = "out.mat"

    print("factoring project")
    print("----------------")
    print("N =\t{}".format(N))

    # factorbase our choice is size 1000
    F_size = 1000
    F = []

    if(args.generate):
        print("\tloading factorbase {}...".format(prime_file))
        with open(prime_file, 'r') as f:
            size = 0
            while size < F_size:
                line = f.readline()         # 10 per line
                for word in line.split():
                    F += [int(word)]
                    size += 1
                    
        # L size specified on website
        L = 1024
        B = F[-1] + 1

        print "\t|F| = {}".format(len(F))
        print "\t{}-smooth".format(B)
        print "\tL = {}".format(len(F))

        # generate L relations
        table = np.empty([L, 4]) 
        
        # find suitable r values
        populate_table(table, N, B)
        print "\t[*] table populated"

        # matrix for gaussian elimination
        M = generate_matrix(table,F)
        print "\t[*] matrix generated"

        # save matrix to in.mat
        with open(in_file, 'w') as f:
            # save header info
            m,n = M.shape
            f.write("{} {}\n".format(m,n))
            # save matrix M
            np.savetxt(f, M, fmt='%d', delimiter=' ')
        print "\t[*] matrix saved to {}".format(in_file)

        # find a nullspace of M that works
        # we run gauss program
        os.system("./gauss {} {}".format(in_file, out_file))
        print "\t[*] gauss program executed. output at {}".format(out_file)

    with open(out_file,"r") as f:

        num_soln = f.readline()

        for solution in f.readlines():
            #TODO test solution
            p, q = test_solution(solution, F, N)
            if (p != 0 and q != 0):
                print "p={}\tq={}".format(p,q)
        
