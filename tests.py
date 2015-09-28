__author__ = 'elena'
from my_random import Random
from time import time
import math


def moments_test(n):
    delta = 1.96
    c1 = (12.0 * n) ** 0.5
    c2 = (1.0 * (n - 1) / n) * (0.0056 / n + 0.0028 / (n * n) + 0.0083 / (n * n * n)) ** (- 0.5)
    lst = random.list_of_random(n)
    mean_val = sum(lst) / n
    stand_dev = sum([(x - mean_val) ** 2 for x in lst]) / (n - 1)
    print(c1 * math.fabs(mean_val - 0.5) < delta, c2 * math.fabs(stand_dev - 1.0 / 12) < delta)
    return mean_val, stand_dev


def covariance_test(j, n):
    delta = 1.96
    lst = random.list_of_random(n)
    shifted_lst = lst[j:]
    # print(list(zip(lst, shifted_lst)))
    covariance = sum(map(lambda x: x[0] * x[1], zip(lst, shifted_lst)))
    covariance = covariance / (n - j - 1) - sum(lst) ** 2 / ((n - 1) * n)
    if j == 0:
        multiplier = 2 ** 0.5
        cov = 1. / 12
    else:
        multiplier = 1
        cov = 0
    print(abs(covariance - cov) < multiplier * delta / 12 / math.sqrt(n - 1))
    return covariance


def keno():
    max_num = 80
    num_table = list(range(1, max_num + 1))
    chosen = []
    for i in range(20):
        idx = random.int_random(0, max_num)
        chosen.append(num_table[idx])
        del num_table[idx]
        max_num -= 1
    return sorted(chosen)


random = Random()
random.seed(time())
print("Tests of the first and second moments:")
for i in [10, 100, 1000, 10000]:
    print("n = {0}".format(i), end=" ")
    moments_test(i)

print("Test of covariance:")
for n in [10, 100, 1000, 10000]:
    for j in [0, 1]:
        print("n = {0}, j = {1}".format(n, j), end=" ")
        covariance_test(j, n)

print("Keno lot:")
print(keno())