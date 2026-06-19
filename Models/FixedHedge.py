import numpy as np
def algo():
    print('Configure Hedge Algorithm\n')
    print('Enter the number K of desired experts\n')

    k =  int(input())
    weights = [[1 for _ in range(k)]]

    "weights.append([2 for _ in range(k)])"

    print('Enter the number of turns T\n')
    T = int(input())

    for t in range(T):
        somma = 0
        for i in range(k):
            somma = somma + weights[i][t]
        print(somma)