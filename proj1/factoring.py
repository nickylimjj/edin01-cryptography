import numpy as np

def populate_table (table):
    return 0

def generate_matrix (table, matrix):
    return 0

if __name__ == "__main__":

     # our N
    N = 89692892645583511288289L

    # factorbase our choice is size 10
    f = open('prim_2_24.txt', 'r')
    F = []



    # L = |F| + 2
    L = len(F) + 2
    
    # generate L relations
    table = np.empty([L, len(F)]) 
    
    populate_table(table)

    M = generate_matrix(table, M)

    # find a nullspace of M that works
    while true:
        x = A.nullspace()
