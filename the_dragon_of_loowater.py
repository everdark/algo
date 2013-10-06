# Kyle Chung <alienatio@pixnet.net>
# 2013-10-05
# The Dragon of Loowater



# setup
import os
import random
os.chdir('C:/Dropbox/Python/algo/input')
cwd = os.getcwd()


# read input sample
fname = cwd + '\\the_dragon_of_loowater.txt'
with open(fname, 'r') as infile:
    data = [line.strip('\n') for line in infile.readlines()]


# solve
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

def save_loowater(data):
    for ln, line in enumerate(data):
        if ' ' in line: # first line of a case: n = # of dragon, m = # of knight
            n, m = [int(number) for number in line.split(' ')]
            if n == m == 0:
                break
            dragons = map(int, data[ln+1:ln+1+n])
            insertion_sort(dragons)
            knights = map(int, data[ln+n+1:ln+n+1+m])
            insertion_sort(knights)
            cost = killed = 0
            for k in range(m):
                if knights[k] >= dragons[killed]:
                    cost += knights[k]
                    killed += 1
                    if killed == n:
                        print(cost)
                        break
            if killed < n:
                print('Loowater is doomed!')

    return(None)

save_loowater(data)


# test for random input
ncase = 5
random_input = []
for nc in range(ncase):
    n, m = random.randint(1,8), random.randint(1,8)
    random_input.append(str(n) + ' ' + str(m))
    for i in range(n):
        random_dragon = str(random.randint(1,10))
        random_input.append(random_dragon)
    for j in range(m):
        random_knight = str(random.randint(1,10))
        random_input.append(random_knight)
random_input.append('0 0')

for ln, line in enumerate(random_input):
    print(line)

save_loowater(random_input)


