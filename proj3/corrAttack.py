#Project 3
from __future__ import division


def genStream1(K, n):
    """
    INPUT:  K (Key)
            n (lenth of keystream)
    OUTPUT: Stream for LFSR1 (len 13) for corresponding K
            newer symbols on right
            string
    """

    res = ''.join(K)
    curr_state = K

    for i in range(n - len(K)):
        # primitive 1+x+x2+x4+x6+x7+x10+x11+x13
        curr_state = curr_state[1:] + [str((int(curr_state[0]) +
                                      int(curr_state[2])      +
                                      int(curr_state[3])      +
                                      int(curr_state[6])      +
                                      int(curr_state[7])      +
                                      int(curr_state[9])      +
                                      int(curr_state[11])     +
                                      int(curr_state[12])) % 2)]
        
        res += curr_state[-1]

    return res


def genStream2(K, n):
    """
    INPUT:  K (Key)
            n (lenth of keystream)
    OUTPUT: Stream for LFSR2 (len 15) for corresponding K
            newer symbols on right
            string
    """

    res = ''.join(K)
    curr_state = K

    for i in range(n - len(K)):
        # primitive 1+x2+x4+x6+x7+x10+x11+x13+x15
        curr_state = curr_state[1:] + [str((int(curr_state[0]) +
                                      int(curr_state[2])      +
                                      int(curr_state[4])      +
                                      int(curr_state[5])      +
                                      int(curr_state[8])      +
                                      int(curr_state[9])      +
                                      int(curr_state[11])     +
                                      int(curr_state[13])) % 2)]
        res += curr_state[-1]

    return res

def genStream3(K, n):
    """
    INPUT:  K (Key)
            n (lenth of keystream)
    OUTPUT: Stream for LFSR3 (len 17) for corresponding K
            newer symbols on right
            string
    """ 

    res = ''.join(K)
    curr_state = K

    for i in range(n - len(K)):
        # primitive 1+x2+x4+x5+x8+x10+x13+x16+x17
        curr_state = curr_state[1:] + [str((int(curr_state[0]) +
                                      int(curr_state[1])      +
                                      int(curr_state[4])      +
                                      int(curr_state[7])      +
                                      int(curr_state[9])      +
                                      int(curr_state[12])     +
                                      int(curr_state[13])     +
                                      int(curr_state[15])) % 2)]
        res += curr_state[-1]

    return res

def hamDist(genSeq, givenSeq, n):
    """
    INPUT:  genSeq (Generated Sequence from LFSR)
            givenSeq 
            length n of keystream

    OUTPUT: Hamming Distance
    Note:   comparing strings
    """
    genSeq = [x for x in genSeq]

    dist = 0
    for i in range(0,n):
        assert type(genSeq[i]) == type(givenSeq[i]), "ham type error"

        if genSeq[i] != givenSeq[i]:
            dist += 1

    return dist

def highestP1(givenSeq):

#   INPUT:  Given Sequence

#   OUTPUT: Highest probability for LFSR 1, corresponding Key

#   Outline: Inside a loop, generate a key K, call genStream1(K,n), call HamDist(...), 
#            calculate p*, compare with max p*, update max p* and corresponding Key K then output.
    p_star = 0.5
    maxdev = 0
    maxK = None

    n = len(givenSeq)

    for i in range(1 , 2**13):
        K = [x for x in format(i, '013b')]
        genSeq = genStream1(K,n)
        dist = hamDist(genSeq, givenSeq, n)
        p = 1.0 - (dist/n)
        dev = abs(p - 0.5)
        if dev > maxdev:
            p_star = p
            maxdev = dev
            maxK = K

    return  p_star, maxK

def highestP2(givenSeq):

#   INPUT:  Given Sequence

#   OUTPUT: Highest probability for LFSR 2, corresponding Key

#   Outline: same as highestP1

    p_star = 0.5
    maxdev = 0
    maxK = None

    n = len(givenSeq)
    for i in range(1 , 2**15):
        K = [x for x in format(i, '015b')]
        genSeq = genStream2(K,n)
        dist = hamDist(genSeq, givenSeq, n)
        p = 1.0 - (dist/n)
        dev = abs(p - 0.5)
        if dev > maxdev:
            p_star = p
            maxdev = dev
            maxK = K

    return  p_star, maxK

def highestP3(givenSeq):

#   INPUT:  Given Sequence

#   OUTPUT: Highest probability for LFSR 3, corresponding Key

#   Outline: same as highestP1

    p_star = 0.5
    maxdev = 0
    maxK = None

    n = len(givenSeq)

    for i in range(1 , 2**17):
        K = [x for x in format(i, '017b')]
        genSeq = genStream3(K,n)
        dist = hamDist(genSeq, givenSeq, n)
        p = 1.0 - (dist/n)
        dev = abs(p - 0.5)
        if dev > maxdev:
            p_star = p
            maxdev = dev
            maxK = K

    return  p_star, maxK

if __name__ == "__main__":
    
    fn = 'task02.txt'

    # Import our Sequence 
    with open(fn, 'r') as f:
        givenSeq = [ x for x in "".join(
                     [line.strip() for line in f.readlines()])]

    n = len(givenSeq)

    # calculate most probably key for each LFSR
    print('calc p1...')
    p1 , k1 = highestP1(givenSeq)
    print(k1,p1)
    print('calc p2...')
    p2 , k2 = highestP2(givenSeq)
    print(k2,p2)
    print('calc p3...')
    p3 , k3 = highestP3(givenSeq)
    print(k3,p3)


    # verifying
    # k1 = [c for c in '1101111011110']   # paul
    # k1 = [c for c in '0010111100110']   # ours
    # k2 = [c for c in '001100000110001']
    # k3 = [c for c in '10101000100101010']

    assert len(k1) == 13
    assert len(k2) == 15
    assert len(k3) == 17

    s1 = genStream1(k1, n)
    s2 = genStream2(k2 ,n)
    s3 = genStream3(k3, n)
    z = []
    for i in range(0, n):

        if (int(s1[i]) + int(s2[i]) + int(s3[i])) > 1:
            z += ['1']
        else:
            z += ['0']

    print s1
    print s2
    print s3
    print z
    print givenSeq

    diff = hamDist(z, givenSeq, n)

    print("{}% match".format((1 - diff/n*1.0) * 100))
    
