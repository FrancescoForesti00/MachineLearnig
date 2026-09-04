#test usato per sperimentare

import numpy as np



all_regrets = [[0.0] * 2 for _ in range(10)]

for i in range(10):
    for j in range(2):
        if j == 0:
            all_regrets[i][j] = 100
        else:
            all_regrets[i][j] = 1


regret = [0.0]*2

for i in range(2):
    for j in range(10):
        regret[i] = regret[i] + all_regrets[j][i]
    regret[i] = regret[i] / 10
print(all_regrets)
print(regret)