import random
from numpy import cumsum

# Counting sort
# Assume that all elements are integers in the range [0,k].
# It determines for each element x the number of elements less than x.
# Need at least double space of the original sequence. (i.e., not in-place)

def counting_sort(inst):
    if len(inst) == 0:
        return inst

    k = max(inst)
    C = [0] * (k + 1)
    sorted = [0] * len(inst)

    # count frequencies
    for j in range(0, len(inst)):
        C[inst[j]] += 1

    # do cumulative sum
##    for i in range(1, k+1):
##        C[i] = C[i] + C[i-1]
    C = list(cumsum(C))

    # sort
    for j in range(len(inst)-1, -1, -1):
        sorted[C[inst[j]]-1] = inst[j]
        C[inst[j]] = C[inst[j]] - 1

    return sorted

# check the sorting correctness
for i in range(0,100):
    random_len = random.randint(0,50)
    samp = [random.randint(0,100) for num in range(random_len)]
    sorted = counting_sort(samp)
    check = [j-k for k, j in zip(sorted[:-1], sorted[1:]) if j-k < 0]
    if len(check) != 0:
        print 'Bug detected!'
    if i == 99:
        print 'Check completed.'