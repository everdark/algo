import random

# merge sort
def merge(inst, p, q, r):
    '''
    A subroutine for merge sort.
    The partial list inst[p:r+1] is merge-sorted once.
    '''
    left = inst[p:q+1]
    left.append(float('inf'))
    right = inst[q+1:r+1]
    right.append(float('inf'))
    i = 0
    j = 0
    for k in range(p, r+1):
        if left[i] <= right[j]:
            inst[k] = left[i]
            i += 1
        else:
            inst[k] = right[j]
            j += 1
    return None

def merge_sort(inst, p, r):
    '''Do recursive merge sort in place.'''
    if p < r:
        q = (p + r) / 2
        merge_sort(inst=inst, p=p, r=q)
        merge_sort(inst=inst, p=q+1, r=r)
        merge(inst=inst, p=p, q=q, r=r)
    return None

samp = [random.randint(0,9) for i in range(7)]
merge_sort(inst=samp, p=0, r=len(samp)-1)