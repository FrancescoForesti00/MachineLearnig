#Implementation from scratch of the hedge algorithm with a fixed learning rate


import math
import numpy as np
#import matplotlib.pyplot as plt




def algo():
    print('Configure Hedge Algorithm\n')

    print('Select losses type:\n1)Stochastic_losses\n2)Adversarial_losses\n3)Low-gap_losses\n')
    loss_choice = int(input())

    #learning rate selection
    #print('Select learning rate\n')
    learning_rate = 0.5#float(input())

    print('Enter the number K of desired experts\n')
    k =  int(input())

    print('Enter the number of turns T\n')
    T = int(input())


    #initialization
    index_selection = [i for i in range(k)]
    weights = [1 for i in range(k)]
    probabilities = [0 for i in range(k)]
    losses = np.loadtxt((loss_choice == 1)*'Stochastic_losses.txt' + (loss_choice == 2)*'Adversarial_losses.txt' + (loss_choice == 3)*'Low-gap_losses.txt', usecols=range(k))

    info_for_plot = []
    expert_losses = [0 for i in range(k)]
    cumulative_loss = 0

    for t in range(T):
        somma = 0
        #define the distribution p
        for i in range(k):
            somma = somma + weights[i]
        for i in range(k):
            probabilities[i] = weights[i]/somma

        #draw I according to p
        chosen = np.random.choice(index_selection, None, True ,probabilities)
        print(chosen)

        #cumulative loss update
        cumulative_loss = cumulative_loss + losses[t][chosen]

        #expert losses update
        for i in range(k):
            expert_losses[i] = expert_losses[i] + losses[t][i]

        # regret
        regret = cumulative_loss/t - min(expert_losses)/t

        #update info for plot
        info_for_plot.append((t, cumulative_loss, regret))

        #update the weights
        for i in range(k):
            weights[i] = weights[i]*math.exp(-(learning_rate*losses[t][i]))


    #TODO plot cumulative loss, regret vs time