# Kyle Chung <alienatio@pixnet.net>
# 2013-10-06
# Spreadinh the Wealth



# setup
import os
import random
import operator
import numpy as np
os.chdir('C:/Dropbox/Python/algo/input')
cwd = os.getcwd()


# read input sample
fname = cwd + '\\spreading_the_wealth.txt'
with open(fname, 'r') as infile:
    data = [line.strip('\n') for line in infile.readlines()]


# solve
def spread(data):
    catch = []
    bound = -1
    for ln, line in enumerate(data):
        if bound == -1:
            bound = int(line)
        catch.append(int(line))
        bound -= 1
        if bound == -1:
            case = catch[1:]
            catch = []
            C = map(lambda x: x - np.mean(case), case)
            cum = list(np.cumsum(C))[:-1]
            cum.append(0)
            x1 = round(np.median(cum)) # the optimal number of give-away for #1
            del cum[-1]
            allx = [x1] + map(lambda x: x1 - x, cum)
            print(int(sum(map(abs, allx))))

    return(None)

spread(data)


# test for random input
ncase = 5
random_input = []
while ncase > 0:
    ncase -= 1
    n = random.randint(1,5)
    total_money = n * random.randint(10, 50)
    random_input.append(str(n))
    random_split = [random.randint(1, total_money) for i in range(n-1)]
    random_split.sort()
    random_split = [0] + random_split + [total_money]
    random_split = map(operator.sub, random_split[1:], random_split[:-1])
    for i in random_split:
        random_input.append(i)

for ln, line in enumerate(random_input):
    print(line)

spread(random_input)