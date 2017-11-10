import numpy as np
import sys
import os

def populate_table (table):
    # TODO
    return 0

def generate_matrix (table):
    # TODO
    return 0

def test_solution(solution, N):
    return 0, 0

if __name__ == "__main__":

     # our N
    N = 89692892645583511288289L

    # factorbase our choice is size 10
    # TODO f = open('prim_2_24.txt', 'r')
    F = [2,3,5,7,11,13,17,19,23,29]
    # f.close()

    # L = |F| + 2
    L = len(F) + 2
    
    # generate L relations
    table = np.empty([L, len(F)]) 
    
    # find suitable r values
    populate_table(table)

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
        
