from math import gcd
import math
import cx_Oracle
import random

counter = 0
n = 10000000
for i in range(n):
    first = random.randint(1, 1000)
    second = random.randint(1, 1000)
    if gcd(first, second) == 1:
        counter += 1
prob = counter / n
print(prob)
pi = math.sqrt(6 / prob)
print(pi)
