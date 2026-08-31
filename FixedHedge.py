#Implementation from scratch of the hedge algorithm with a fixed learning rate
#TODO: rimozione T

import math
import numpy as np
import matplotlib.pyplot as plt

def algo():
    print('Configure Hedge Algorithm\n')

    print('Select losses type:\n1)Stochastic_losses\n2)Adversarial_losses\n3)Low-gap_losses\n')
    loss_choice = int(input())

    print('Enter the number K of desired experts\n')
    k = int(input())

    print('Enter the number of turns T\n')
    t_max = int(input())

    if loss_choice == 1:
        losses = np.loadtxt((loss_choice == 1) * 'Losses//Stochastic_losses', usecols=range(k))
    elif loss_choice == 2:
        losses = np.loadtxt((loss_choice == 2) * 'Losses//Adversarial_losses', usecols=range(k))
    elif loss_choice == 3:
        losses = np.loadtxt((loss_choice == 3) * 'Losses//Low-gap_losses', usecols=range(k))
    else:
        print('Invalid choice')
        return

    #learning rate selection
    #print('Select learning rate\n')
    learning_rate = 0.5#float(input())




    #initialization
    index_selection = [i for i in range(k)]
    weights = [1] * k
    probabilities = [0] * k
    regret = [0] * t_max
    cumulative_loss = [0] * t_max
    expert_losses = [0] * k


    for t in range(t_max):
        #define the distribution p
        somma = sum(weights)
        for i in range(k):
            probabilities[i] = weights[i]/somma

        #draw I according to p
        chosen = np.random.choice(index_selection, None, True ,probabilities)


        #cumulative loss update
        cumulative_loss[t] = cumulative_loss[t-1] + losses[t][chosen]

        #expert losses update
        for i in range(k):
            expert_losses[i] = expert_losses[i] + losses[t][i]

        # regret
        regret[t] = cumulative_loss[t]/(t + 1) - min(expert_losses)/(t + 1)

        #update the weights
        for i in range(k):
            weights[i] = weights[i]*math.exp(-(learning_rate*losses[t][i]))

    print(regret[t_max - 1])
    print(min(expert_losses))
    print(cumulative_loss[t_max - 1])


    plt.plot([(i + 1) for i in range(t_max)], cumulative_loss, "b-", label= "cumulative loss")
    plt.plot( [(i + 1) for i in range(t_max)], regret, "r.", label = "regret")
    plt.legend(loc = 'upper left')
    plt.show()