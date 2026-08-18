#Implementation from scratch of the adaptive edege algorithm


import math
import numpy as np

def algo():
    print('Configure AdaptiveHedge Algorithm\n')
    print('Select losses type:\n1)Stochastic_losses\n2)Adversarial_losses\n3)Low-gap_losses\n')
    loss_choice = int(input())

    print('Enter the number K of desired experts\n')
    k =  int(input())

    print('Enter the number of turns T\n')
    T = int(input())

    #weights initialization
    index_selection = [i for i in range(k)]
    weights = [1 for i in range(k)]
    probabilities = [0 for i in range(k)]
    losses = [[]]
    losses = np.loadtxt((loss_choice == 1)*'Stochastic_losses.txt' + (loss_choice == 2)*'Adversarial_losses.txt' + (loss_choice == 3)*'Low-gap_losses.txt', usecols=range(k))

    learning_rate = 1
    for t in range(T):
        somma = 0

        #define the distribution p
        for i in range(k):
            somma = somma + weights[i]
        for i in range(k):
            probabilities[i] = weights[i]/somma

        #draw I according to p
        chosen = np.random.choice(index_selection, 1 ,probabilities)
        print(chosen)

        #update the weights
        for i in range(k):
            weights[i] = weights[i]*math.exp(-(learning_rate*losses[t][i]))



    print(probabilities)