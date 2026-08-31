#Implementation from scratch of the adaptive hedge algorithm with a dynamic learning rate
#TODO: rimozione T

import math
import numpy
import numpy as np
import matplotlib.pyplot as plt




def algo():
    print('Configure Adaptive Hedge Algorithm\n')

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

    #initialization
    delta = 0
    psi = 1.62
    budget = 0
    mixability_gap = 0
    learning_rate = psi
    index_selection = [i for i in range(k)]
    weights = [1/k] * k
    probabilities = [0] * k
    regret = [0] * t_max
    cumulative_loss = [0] * t_max
    expert_losses = [0] * k

    for t in range(t_max):
        #if is the first round or the cumulative mixability gap exceeded the budget
        if t == 0 or delta >= budget:
            ##start new segment

            #update learning rate, budget, cumulative mixability gap, weights vector
            learning_rate = learning_rate/psi
            budget = (1/(math.e - 1) + 1/learning_rate)*math.log(k)
            delta = 0
            weights = [1/k] * k

        ##make a decision

        # define the distribution p
        somma = sum(weights)

        for i in range(k):
            probabilities[i] = weights[i]/somma

        # draw I according to p
        chosen = np.random.choice(index_selection, None, True, probabilities)

        # cumulative loss update
        cumulative_loss[t] = cumulative_loss[t - 1] + losses[t][chosen]

        #expert losses update
        for i in range(k):
            expert_losses[i] = expert_losses[i] + losses[t][i]

        # regret
        regret[t] = cumulative_loss[t]/(t + 1) - min(expert_losses)/(t + 1)


        ##prepare for next round

        #update the value of  the cumulative mixabilty gap TODO: check che funzioni
        mixability_gap = 0
        for i in range(k):
            mixability_gap = mixability_gap + weights[i] * math.exp(- learning_rate * losses[t][i])
        delta = delta + numpy.inner(weights, losses[t]) + 1/learning_rate * math.log(mixability_gap)

        #update weights vector TODO: check che funzioni
        for i in range(k):
            weights[i] = weights[i] * math.exp(- learning_rate * losses[t][i])/mixability_gap

    print(regret[t_max - 1])
    print(min(expert_losses))
    print(cumulative_loss[t_max - 1])

    plt.plot([(i + 1) for i in range(t_max)], cumulative_loss, "b-", label="cumulative loss")
    plt.plot([(i + 1) for i in range(t_max)], regret, "r.", label="regret")
    plt.legend(loc='upper left')
    plt.show()

