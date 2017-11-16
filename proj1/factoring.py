import numpy as np
import string
import sys
import os
import argparse
import math
import time

def generate_matrix (N, L, B, F):
    """
    DESC:   generate suitable r values
            and store it in a matrix
    INPUT:  N - modulus N
            L - number of relations
            B - B-smooth value
            F - factor base
    OUTPUT: M filled matrix to save to file
    """

    # generate L relations
    T = np.zeros([L, 4], dtype=np.int64) 
    i = 0

    # fill up entire table
    for k in range(1,100):
        for j in range(k):
            if i == L:
                break
            # generate a test r and r^2
            r = int(math.floor(math.sqrt(k*N)) + j)
            r2 = (r**2) % N
            
            dict_of_fac = checkSmooth_(r2,B)

            # check if r2 is B-smooth and not duplicate
            if dict_of_fac != -1:

                # generate matrix representation
                # '[1,1,0,0,1,...]'
                r2_mat_repr = np.zeros([1,len(F)], dtype=int)

                for key,value in dict_of_fac.iteritems():
                    ind = F.index(key)
                    r2_mat_repr[0][ind] = value%2

                # if not duplicate, we add it in
                try: 
                    if not((M == r2_mat_repr).all(1).any()):
                        # add table and matrix row
                        T[i] = (k, j, r, r2)
                        M = np.vstack([M,r2_mat_repr])
                        i += 1
                except UnboundLocalError:
                    T[i] = (k, j, r, r2)
                    M = r2_mat_repr
                    i += 1

    print('\tmax r,r2 = {},{}'.format(np.amax(T,axis=0)[2],
            np.amax(T,axis=0)[3]))

    return T, M

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
        
def is_smooth(n, F):
    if n == 0:
        return -1

    for factor in F:
        while n % factor == 0:
            n /= factor
            try:
                fac[i] += 1
            except KeyError:
                fac[i] = 1
    if n == 1:
        return fac
    return -1

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
    LHS = np.int64(1)                       # tracks r values
    RHS = np.int64(1)                        # track r^2
    B = F[-1] + 1
    hello = {} 
    soln =  x.rstrip().split(' ')

    for idx, val in enumerate(soln):
        # select row
        if val == '1':
            LHS = LHS * table[idx][-2] % N                   # get r
            factors = checkSmooth_(table[idx][-1],B)  # get dict of factors
	    # for keyy,value in factors.iteritems():
		# if (hello.has_key(keyy)):
		    # hello[keyy] += factors[keyy]/2
		# else:
		    # hello[keyy] = factors[keyy]/2
            RHS = RHS * int(table[idx][-1]) % N
    # for keyy,value in hello.iteritems():
	# RHS *= keyy**hello[keyy]

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
    print "\tL = {}".format(L)

    
    # find suitable r values
    T, M = generate_matrix(N, L, B, F)
    print "\t[*] matrix generated"

    # matrix for gaussian elimination

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
            print("\t[*]testing a candidate...")
            p, q = test_solution(x, T, F, N)
            if (p != 1 and q != 1):
                break

    # print answer
    if (p != 1 and q != 1):
        print "p={}\tq={}".format(p,q)
    else:
        print("solution not found")
        
