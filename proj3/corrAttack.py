#Project 3
from __future__ import division


def genStream1(K, n):
    """
    INPUT:  K (Key)
            n (lenth of keystream)
    OUTPUT: Stream for LFSR1 (len 13) for corresponding K
    """

    res = ''
    curr_state = K

    for i in range(n):
        # primitive 1+x+x2+x4+x6+x7+x10+x11+x13
        curr_state = curr_state[1:] + [str((int(curr_state[0]) + 
                                      int(curr_state[1])      +
                                      int(curr_state[3])      +
                                      int(curr_state[5])      +
                                      int(curr_state[6])      +
                                      int(curr_state[9])      +
                                      int(curr_state[10])     +
                                      int(curr_state[12])) % 2)]
        res += curr_state[-1]

    return res


def genStream2(K, n):
    """
    INPUT:  K (Key)
            n (lenth of keystream)
    OUTPUT: Stream for LFSR2 (len 15) for corresponding K
    """

    res = ''
    curr_state = K

    for i in range(n):
        # primitive 1+x2+x4+x6+x7+x10+x11+x13+x15
        curr_state = curr_state[1:] + [str((int(curr_state[1]) + 
                                      int(curr_state[3])      +
                                      int(curr_state[5])      +
                                      int(curr_state[6])      +
                                      int(curr_state[9])      +
                                      int(curr_state[10])     +
                                      int(curr_state[12])     +
                                      int(curr_state[14])) % 2)]
        res += curr_state[-1]

    return res

def genStream3(K, n):
    """
    INPUT:  K (Key)
            n (lenth of keystream)
    OUTPUT: Stream for LFSR3 (len 17) for corresponding K
    """ 

    res = ''
    curr_state = K

    for i in range(n):
        # primitive 1+x2+x4+x5+x8+x10+x13+x16+x17
        curr_state = curr_state[1:] + [str((int(curr_state[1]) + 
                                      int(curr_state[3])      +
                                      int(curr_state[4])      +
                                      int(curr_state[7])      +
                                      int(curr_state[7])      +
                                      int(curr_state[9])      +
                                      int(curr_state[12])     +
                                      int(curr_state[15])     +
                                      int(curr_state[16])) % 2)]
        res += curr_state[-1]

    return res

def HamDist(genSeq, givenSeq, n):

#   INPUT: genSeq (Generated Sequence from LFSR)
#          givenSeq 
#          length n of keystream

#   OUTPUT: Hamming Distance

    dist = 0
    for i in range(0,n):
        if genSeq[i] != givenSeq[i]:
            dist += 1

    return dist

def highestP1(givenSeq, n):

#   INPUT:  Given Sequence
#           length of keystream

#   OUTPUT: Highest probability for LFSR 1, corresponding Key

#   Outline: Inside a loop, generate a key K, call genStream1(K,n), call HamDist(...), 
#            calculate p*, compare with max p*, update max p* and corresponding Key K then output.
    p_star = 0.5
    maxdev = 0
    maxK = None

    for i in range(1 , 2**13):
        K = [x for x in format(i, '013b')]
        genSeq = genStream1(K,n)
        dist = HamDist(genSeq, givenSeq, n)
        p = 1.0 - (dist/n)
        dev = abs(p - 0.5)
        if dev > maxdev:
            print (dev)
            p_star = p
            maxdev = dev
            maxK = K

    return  p_star, maxK

def highestP2(givenSeq, n):

#   INPUT:  Given Sequence
#          n (lenth of keystream)

#   OUTPUT: Highest probability for LFSR 2, corresponding Key

#   Outline: same as highestP1

    p_star = 0.5
    maxdev = 0
    maxK = None

    for i in range(1 , 2**15):
        K = [x for x in format(i, '015b')]
        genSeq = genStream1(K,n)
        dist = HamDist(genSeq, givenSeq, n)
        p = 1.0 - (dist/n)
        dev = abs(p - 0.5)
        if dev > maxdev:
            print (dev)
            p_star = p
            maxdev = dev
            maxK = K

    return  p_star, maxK

def highestP3(givenSeq, n):

#   INPUT:  Given Sequence
#          n (lenth of keystream)

#   OUTPUT: Highest probability for LFSR 3, corresponding Key

#   Outline: same as highestP1

    p_star = 0.5
    maxdev = 0
    maxK = None

    for i in range(1 , 2**17):
        K = [x for x in format(i, '017b')]
        genSeq = genStream1(K,n)
        dist = HamDist(genSeq, givenSeq, n)
        p = 1.0 - (dist/n)
        dev = abs(p - 0.5)
        if dev > maxdev:
            print (dev)
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
    p1 , k1 = highestP1(givenSeq, n)
    p2 , k2 = highestP2(givenSeq, n)
    p3 , k3 = highestP3(givenSeq, n)

    print(k1,k2,k3)
    print(p1,p2,p3)

    s1 = genStream1(k1, n)
    s2 = genStream2(k2 ,n)
    s3 = genStream3(k3, n)
    z = []
    for i in range(0, n):

        if (int(s1[i]) + int(s2[i]) + int(s3[i])) > 1:
            z += [1]
        else:
            z += [0]
    print(z)
    print(givenSeq)
