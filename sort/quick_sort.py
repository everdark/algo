import random

# quicksort (in-replace)
# the algorithm takes expected time O(nlogn), and (n^2) for the worst case
# based on the assumption that all permutations are equally likely.

def partition(inst, p, r):
    '''
    Given a sequence of length r+1(0-indexed), split it into two subsequence.
    The first sequence has all elements no greater than list[r].
    The second sequence has all elements no less than list[r].
    Function returns new index of splitter, done in replace.
    '''
    splitter = inst[r]
    i = p - 1
    for j in range(p, r):
        if inst[j] < splitter:
            i += 1
            swap = inst[i]
            inst[i] = inst[j]
            inst[j] = swap
    swap = inst[i+1]
    inst[i+1] = inst[r]
    inst[r] = swap

    return i + 1

def quicksort(inst, p, r):
    '''
    Sort sequence by recursive quicksort algorithm.
    '''
    if p < r:
        q = partition(inst, p, r)
        quicksort(inst, p, q-1)
        quicksort(inst, q+1, r)

    return None

# randomized quicksort
# the randomization aims to increase the average performance of quicksort

def random_partition(inst, p, r):
    '''
    Partitioning with
    '''
    random_index = random.randint(p, r)
    swap = inst[random_index]
    inst[random_index] = inst[r]
    inst[r] = swap

    return partition(inst, p, r)

def random_quicksort(inst, p, r):
    '''
    Sort sequence by recurssion.
    '''
    if p < r:
        q = random_partition(inst, p, r)
        random_quicksort(inst, p, q-1)
        random_quicksort(inst, q+1, r)

    return None

# check the sorting correctness for quicksort
for i in range(0,100):
    random_len = random.randint(0,50)
    samp = [random.randint(0,100) for num in range(random_len)]
    quicksort(samp, 0, len(samp)-1)
    check = [j-k for k, j in zip(samp[:-1], samp[1:]) if j-k < 0]
    if len(check) != 0:
        print 'Bug detected!'
    if i == 99:
        print 'Check completed.'

# check the sorting correctness for randomized quicksort
for i in range(0,100):
    random_len = random.randint(0,50)
    samp = [random.randint(0,100) for num in range(random_len)]
    random_quicksort(samp, 0, len(samp)-1)
    check = [j-k for k, j in zip(samp[:-1], samp[1:]) if j-k < 0]
    if len(check) != 0:
        print 'Bug detected!'
    if i == 99:
        print 'Check completed.'