# Kyle Chung <alienatio@pixnet.net>
# 2013-10-06
# Commando War



# setup
import os
import random
os.chdir('C:/Dropbox/Python/algo/input')
cwd = os.getcwd()


# read input sample
fname = cwd + '\\commando_war.txt'
with open(fname, 'r') as infile:
    data = [line.strip('\n') for line in infile.readlines()]


# solve
def commando(data):
    nj = 0
    for ln, line in enumerate(data):
        if not ' ' in line: # first line of a case: n = # of warriors
            nj += 1
            n = int(line)
            if n == 0:
                break
            bj = [map(int, d.split(' ')) for d in data[ln+1:ln+1+n]]
            bj = sorted(bj, key=lambda x : x[1], reverse=True)
            elapsed = 0
            max_time = sum(bj[0])
            for job in range(len(bj)):
                elapsed += bj[job][0]
                max_time = max(max_time, elapsed+bj[job][1])
            print('Case ' + str(nj) + ': ' + str(max_time))

    return(None)

commando(data)


# test for random input
ncase = 5
random_input = []
for nc in range(ncase):
    njob = random.randint(1,5)
    random_input.append(str(njob))
    for i in range(njob):
        random_bj = str(random.randint(1,5)), str(random.randint(1,5))
        random_input.append(' '.join(random_bj))
random_input.append('0')

for ln, line in enumerate(random_input):
    print(line)

commando(random_input)