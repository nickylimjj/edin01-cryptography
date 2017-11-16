import numpy as np
import string
import sys
import os
import argparse
import math
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
    Thres = 10

    # fill up entire table
    while i < L:


        r = int(math.floor(math.sqrt(k*N)) + j)
        if r > 50000:
            print k,N, j
        r2 = (r**2) % N

        # check if r2 is B-smooth
        if checkSmooth_(r2,B) != -1:
            T[i] = (k, j, r, r2)
            i += 1
    
        k += 1
        if k >= Thres:
            k %= Thres
            j += 1

    print('\tmax k={}, j={}'.format(Thres,j))
    print('\tmax r,r2 = {},{}'.format(np.amax(T,axis=0)[2],
            np.amax(T,axis=0)[3]))
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

def test_solution(x, table, F, N):
    """
    DESC:   parses a bit-string across a factorbase and
            determine if it is a valid solution
    INPUT:  x - bit string to test
            table - table of r and r^2 values
            F - factor base
            N - number N = pq to factor
    OUTPUT: p,q - valid solution to factor N,
            0,0 if not valid
    """
    # TODO
    LHS = 1                         # tracks r values
    RHS = 1                        # track r^2
    B = F[-1] + 1
    hello = {} 
    soln =  x.rstrip().split(' ')
    if soln.count('1') > 30:
        # print('sol count:{}'.format(soln.count('1')))
        return 1,1

    for idx, val in enumerate(soln):
        # select row
        if val == '1':
            LHS *= table[idx][-2]                   # get r
            factors = checkSmooth_(table[idx][-1],B)  # get dict of factors
	    for keyy,value in factors.iteritems():
		if (hello.has_key(keyy)):
		    hello[keyy] += factors[keyy]/2
		else:
		    hello[keyy] = factors[keyy]/2
            # RHS = merge_dict(RHS,factors)
            #RHS *= int(table[idx][-1])
    for keyy,value in hello.iteritems():
	RHS *= keyy**hello[keyy]

    # calculate p
    p = gcd(abs(RHS-LHS), N)
    q = N/p

    return p, q

def gcd(a,b):
    """
    DESC:   Euclidean algorithm
    INPUT:  a - int
            b - int
    OUTPT:  greatest common divisor
    """
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b%a, a
    return b

if __name__ == "__main__":

    # parse cmdline args
    parser = argparse.ArgumentParser(description='Factoring Algorithm')
    parser.add_argument('--generate','-g', action='store_true',
                        help='generates r values')
    parser.add_argument('--n','-n', type=int,
                        default=323, help='modulus N values')

    args = parser.parse_args()

    # our N
    project_N = 89692892645583511288289L
    test_N1 = 323       # 17 * 19
    test_N2 = 307561    # 457 * 673
    test_N3 = 31741649  # 4621 * 6969

    N = args.n

    prime_file = "prim_2_24.txt"
    in_file = "in.mat"
    out_file = "out.mat"

    print("factoring project")
    print("----------------")
    print("N =\t{}".format(N))

    # factorbase our choice is size 1000
    F_size = 1000
    F = []

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
    table = np.zeros([L, 4], dtype=int) 
    
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

    # finds the solution p, q
    with open(out_file,"r") as out_f:

        num_soln = out_f.readline()

        for x in out_f.readlines():
            p, q = test_solution(x, table, F, N)
            if (p != 1 and q != 1):
                break


    # print answer
    if (p != 1 and q != 1):
        print "p={}\tq={}".format(p,q)
    else:
        print("solution not found")
        
