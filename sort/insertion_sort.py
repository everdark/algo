import random

# insertion sort
'''
For each end of the j-th loop, series [1,...,j-1,j] is completely sorted.
Thus the j+1 element may require a swap for at most j times.
'''
def insertion_sort(inst, decreasing=False):
    '''Do insertion sort in place.'''
    for j in range(1, len(inst)):
        key = inst[j]
        i = j - 1
        if not (decreasing):
            while (i > -1) & (inst[i] > key):
                inst.insert(i, inst.pop(i+1))
                i -= 1
        else:
            while (i > -1) & (inst[i] < key):
                inst.insert(i, inst.pop(i+1))
                i -= 1
    return None

samp = [random.randint(0,9) for i in range(6)]
insertion_sort(samp, decreasing=True)
samp