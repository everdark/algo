import random

# heapsort
# the algorithm takes time O(nlogn)
# in-place implementation pending

def max_heapify(inst, i):
    '''
    Maintain a max heap property in place.
    That is, parent node must be no less than its child nodes.
    It assumes that the trees rooted at left and right child are max-heaps.
    '''
    left_index = 2*i + 1
    right_index = 2*i + 2
    heap_size = len(inst) - 1
    largest_index = i
    # compare with the left child, index the winner
    if left_index <= heap_size:
        if inst[left_index] > inst[i]:
            largest_index = left_index
    else:
        largest_index = i
    # compare the above winner with the right child, index the winner
    if right_index <= heap_size:
        if inst[right_index] > inst[largest_index]:
            largest_index = right_index
    # do swap if any of the children wins
    if largest_index != i:
        swap = inst[i]
        inst[i] = inst[largest_index]
        inst[largest_index] = swap
        max_heapify(inst, largest_index)

    return None

def build_maxheap(inst):
    '''
    Build a max-heap from a list.
    For a binary tree index starting from len(inst)/2 are all leaves.
    '''
    # loop over all non-leaf nodes of the binary tree
    for i in range(len(inst)/2-1, -1, -1):
        max_heapify(inst, i)

    return None

def heapsort(inst):
    '''
    Sort the max-heap object.
    Currently not operate in place!
    '''
    build_maxheap(inst)
    sorted = [0] * len(inst)
    for i in range(len(inst)-1, -1, -1):
        sorted[i] = inst[0]
        inst[0] = inst[i]
        inst = inst[0:i]
        max_heapify(inst, 0)

    return sorted

# check the sorting correctness
for i in range(0,100):
    random_len = random.randint(0,50)
    samp = [random.randint(0,100) for num in range(random_len)]
    sorted = heapsort(samp)
    check = [j-k for k, j in zip(sorted[:-1], sorted[1:]) if j-k < 0]
    if len(check) != 0:
        print 'Bug detected!'
    if i == 99:
        print 'Check completed.'