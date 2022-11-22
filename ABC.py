#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/22 10:25
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : ABC.py
# @Statement : Artificial Bee Colony algorithm
# @Reference : Karaboga D. An idea based on honey bee swarm for numerical optimization[J]. Technical Report-TR06, Kayseri, Turkey: Erciyes University; 2005.
import random
import math
import matplotlib.pyplot as plt


def obj(x):
    """
    The objective function of pressure vessel design
    :param x:
    :return:
    """
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    g1 = -x1 + 0.0193 * x3
    g2 = -x2 + 0.00954 * x3
    g3 = -math.pi * x3 ** 2 - 4 * math.pi * x3 ** 3 / 3 + 1296000
    g4 = x4 - 240
    if g1 <= 0 and g2 <= 0 and g3 <= 0 and g4 <= 0:
        return 0.6224 * x1 * x3 * x4 + 1.7781 * x2 * x3 ** 2 + 3.1661 * x1 ** 2 * x4 + 19.84 * x1 ** 2 * x3
    else:
        return 1e10


def boundary_check(x, lb, ub, dim):
    """
    Check the boundary
    :param x: a candidate solution
    :param lb: the lower bound (list)
    :param ub: the upper bound (list)
    :param dim: dimension
    :return:
    """
    for i in range(dim):
        if x[i] < lb[i]:
            x[i] = lb[i]
        elif x[i] > ub[i]:
            x[i] = ub[i]
    return x


def roulette_selection(prob):
    """
    The roulette selection
    :param pro: probability
    :return:
    """
    r = random.random()
    probability = 0
    sum_prob = sum(prob)
    for i in range(len(prob)):
        probability += prob[i] / sum_prob
        if probability >= r:
            return i


def main(pop, iter, lb, ub):
    """
    The main function of ABC
    :param pop: the number of bees
    :param iter: the iteration number
    :param lb: the lower bound (list)
    :param ub: the upper bound (list)
    :return:
    """
    # Step 1. Initialization
    dim = len(lb)  # dimension
    pos = []  # the position of bees
    score = []  # the score of bees
    iter_best = []  # the best-so-far score of each iteration
    trial = [0 for _ in range(pop)]  # the non-improvement number of each solution
    for _ in range(pop):
        temp_pos = [random.uniform(lb[i], ub[i]) for i in range(dim)]
        pos.append(temp_pos)
        score.append(obj(temp_pos))
    gbest = min(score)  # the global best score
    gbest_pos = pos[score.index(gbest)].copy()  # the global best position
    con_iter = 0
    trial_limit = round(0.6 * dim * pop)

    # Step 2. The main loop
    for t in range(iter):

        # Step 2.1. Produce new food sources
        for i in range(pop):
            k = random.randint(0, pop - 1)
            while k == i:
                k = random.randint(0, pop - 1)
            new_pos = [pos[i][j] + random.uniform(-1, 1) * (pos[i][j] - pos[k][j]) for j in range(dim)]
            new_pos = boundary_check(new_pos, lb, ub, dim)
            new_score = obj(new_pos)
            if new_score < score[i]:
                score[i] = new_score
                pos[i] = new_pos
            else:
                trial[i] += 1
        mean_score = sum(score) / len(score)
        prob = [math.exp(-score[i] / mean_score) for i in range(pop)]

        # Step 2.2. Onlooker bees procedure
        for i in range(pop):
            ind = roulette_selection(prob)
            k = random.randint(0, pop - 1)
            while k == ind:
                k = random.randint(0, pop - 1)
            new_pos = [pos[ind][j] + random.uniform(-1, 1) * (pos[ind][j] - pos[k][j]) for j in range(dim)]
            new_pos = boundary_check(new_pos, lb, ub, dim)
            new_score = obj(new_pos)
            if new_score < score[i]:
                score[i] = new_score
                pos[i] = new_pos
            else:
                trial[i] += 1

        # Step 2.3. Scout bees procedure
        for i in range(pop):
            if trial[i] >= trial_limit:
                pos[i] = [random.uniform(lb[j], ub[j]) for j in range(dim)]
                score[i] = obj(pos[i])
                trial[i] = 0

        # Step 2.4. Update gbest
        if min(score) < gbest:
            gbest = min(score)
            gbest_pos = pos[score.index(min(score))].copy()
            con_iter = t + 1
        iter_best.append(gbest)

    # Step 3. Sort the results
    x = [i for i in range(iter)]
    plt.figure()
    plt.plot(x, iter_best, linewidth=2, color='blue')
    plt.xlabel('Iteration number')
    plt.ylabel('Global optimal value')
    plt.title('Convergence curve')
    plt.show()
    return {'best score': gbest, 'best solution': gbest_pos, 'convergence iteration': con_iter}


if __name__ == '__main__':
    # Parameter settings
    pop = 50
    iter = 300
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    print(main(pop, iter, lb, ub))
